import numpy as np
import base64
import gzip
import pickle
from pygltflib import GLTF2, Buffer, BufferView, Accessor, Mesh, Node, Scene, Asset

# These are the glTF spec constants:
FLOAT = 5126  # 32-bit float
UNSIGNED_SHORT = 5123  # 16-bit unsigned int
ARRAY_BUFFER = 34962  # Vertex attributes
ELEMENT_ARRAY_BUFFER = 34963  # Indices


def convert_asset_to_glb(asset_data, output_file):
    """
    Convert an asset dictionary (with keys 'vertices', 'normals', 'uvs', 'triangles')
    into a binary glTF (.glb) file.
    """
    # Extract geometry data from the asset dictionary
    vertices_list = asset_data.get("vertices", [])
    normals_list = asset_data.get("normals", [])
    uvs_list = asset_data.get("uvs", [])
    triangles = asset_data.get("triangles", [])

    if not vertices_list or not triangles:
        raise ValueError("The asset must have at least vertices and triangles defined.")

    # Convert lists of dictionaries to numpy arrays
    vertices = np.array(
        [[v["x"], v["y"], v["z"]] for v in vertices_list], dtype=np.float32
    )
    normals = (
        np.array([[n["x"], n["y"], n["z"]] for n in normals_list], dtype=np.float32)
        if normals_list
        else None
    )
    uvs = (
        np.array([[uv["x"], uv["y"]] for uv in uvs_list], dtype=np.float32)
        if uvs_list
        else None
    )
    indices = np.array(triangles, dtype=np.uint16)

    # Convert numpy arrays to their byte representations
    vertices_bytes = vertices.tobytes()
    normals_bytes = normals.tobytes() if normals is not None else b""
    uvs_bytes = uvs.tobytes() if uvs is not None else b""
    indices_bytes = indices.tobytes()

    # Assign offsets into the single combined buffer:
    offset = 0
    vertices_offset = offset
    vertices_length = len(vertices_bytes)
    offset += vertices_length

    normals_offset = offset
    normals_length = len(normals_bytes)
    offset += normals_length

    uvs_offset = offset
    uvs_length = len(uvs_bytes)
    offset += uvs_length

    indices_offset = offset
    indices_length = len(indices_bytes)
    offset += indices_length

    total_buffer_length = offset

    # Combine all binary data into one buffer
    combined_buffer = vertices_bytes + normals_bytes + uvs_bytes + indices_bytes
    # Encode binary data for use in a data URI
    encoded_buffer = base64.b64encode(combined_buffer).decode("utf-8")

    # Create glTF2 object
    gltf = GLTF2()
    gltf.asset = Asset(version="2.0")

    # Create one buffer that contains all our binary data
    buffer = Buffer(
        byteLength=total_buffer_length,
        uri="data:application/octet-stream;base64," + encoded_buffer,
    )
    gltf.buffers.append(buffer)

    # Create BufferViews for each attribute
    # 1. Vertices
    vertices_bufferView = BufferView(
        buffer=0,
        byteOffset=vertices_offset,
        byteLength=vertices_length,
        target=ARRAY_BUFFER,
    )
    gltf.bufferViews.append(vertices_bufferView)
    vertices_bufferView_index = len(gltf.bufferViews) - 1

    # 2. Normals (if available)
    if normals is not None:
        normals_bufferView = BufferView(
            buffer=0,
            byteOffset=normals_offset,
            byteLength=normals_length,
            target=ARRAY_BUFFER,
        )
        gltf.bufferViews.append(normals_bufferView)
        normals_bufferView_index = len(gltf.bufferViews) - 1
    else:
        normals_bufferView_index = None

    # 3. UVs (if available)
    if uvs is not None:
        uvs_bufferView = BufferView(
            buffer=0, byteOffset=uvs_offset, byteLength=uvs_length, target=ARRAY_BUFFER
        )
        gltf.bufferViews.append(uvs_bufferView)
        uvs_bufferView_index = len(gltf.bufferViews) - 1
    else:
        uvs_bufferView_index = None

    # 4. Indices
    indices_bufferView = BufferView(
        buffer=0,
        byteOffset=indices_offset,
        byteLength=indices_length,
        target=ELEMENT_ARRAY_BUFFER,
    )
    gltf.bufferViews.append(indices_bufferView)
    indices_bufferView_index = len(gltf.bufferViews) - 1

    # Create Accessors for each attribute
    # A. Position accessor from vertices
    vertices_accessor = Accessor(
        bufferView=vertices_bufferView_index,
        byteOffset=0,
        componentType=FLOAT,
        count=vertices.shape[0],
        type="VEC3",
        max=[float(np.max(vertices[:, i])) for i in range(3)],
        min=[float(np.min(vertices[:, i])) for i in range(3)],
    )
    gltf.accessors.append(vertices_accessor)
    vertices_accessor_index = len(gltf.accessors) - 1

    # B. Normals accessor
    if normals is not None:
        normals_accessor = Accessor(
            bufferView=normals_bufferView_index,
            byteOffset=0,
            componentType=FLOAT,
            count=normals.shape[0],
            type="VEC3",
        )
        gltf.accessors.append(normals_accessor)
        normals_accessor_index = len(gltf.accessors) - 1
    else:
        normals_accessor_index = None

    # C. UV accessor
    if uvs is not None:
        uvs_accessor = Accessor(
            bufferView=uvs_bufferView_index,
            byteOffset=0,
            componentType=FLOAT,
            count=uvs.shape[0],
            type="VEC2",
        )
        gltf.accessors.append(uvs_accessor)
        uvs_accessor_index = len(gltf.accessors) - 1
    else:
        uvs_accessor_index = None

    # D. Indices accessor
    indices_accessor = Accessor(
        bufferView=indices_bufferView_index,
        byteOffset=0,
        componentType=UNSIGNED_SHORT,
        count=indices.shape[0],
        type="SCALAR",
    )
    gltf.accessors.append(indices_accessor)
    indices_accessor_index = len(gltf.accessors) - 1

    # Create a single mesh primitive using the accessors
    primitive = {
        "attributes": {"POSITION": vertices_accessor_index},
        "indices": indices_accessor_index,
    }
    if normals_accessor_index is not None:
        primitive["attributes"]["NORMAL"] = normals_accessor_index
    if uvs_accessor_index is not None:
        primitive["attributes"]["TEXCOORD_0"] = uvs_accessor_index

    mesh = Mesh(primitives=[primitive], name=asset_data.get("name", "Mesh"))
    gltf.meshes.append(mesh)
    mesh_index = len(gltf.meshes) - 1

    # Create a node to attach the mesh
    node = Node(mesh=mesh_index, name=asset_data.get("name", "Mesh"))
    gltf.nodes.append(node)
    node_index = len(gltf.nodes) - 1

    # Create a scene that contains this node
    scene = Scene(nodes=[node_index])
    gltf.scenes.append(scene)
    gltf.scene = 0

    # Save as a binary glTF (.glb) file
    gltf.save_binary(output_file)
    print(f"glTF binary saved as {output_file}")


if __name__ == "__main__":
    # Example: load a consolidated asset (compressed pickle) and convert it to .glb.
    asset_file = "/home/dxv2k/.objathor-assets/2023_09_23/assets/03541b2ad507439d84f91bf739a0c1b8/03541b2ad507439d84f91bf739a0c1b8.pkl.gz" 
    output_glb = "converted_asset.glb"

    with gzip.open(asset_file, "rb") as f:
        asset_data = pickle.load(f)

    convert_asset_to_glb(asset_data, output_glb)
