import glob
import os
import numpy as np
import base64
import gzip
import pickle
from pygltflib import (
    GLTF2,
    Buffer,
    BufferView,
    Accessor,
    Mesh,
    Node,
    Scene,
    Asset,
    Image,
    Texture,
    Material,
    PbrMetallicRoughness,
    TextureInfo,
)

# glTF spec constants
FLOAT = 5126  # 32-bit float
UNSIGNED_SHORT = 5123  # 16-bit unsigned int
ARRAY_BUFFER = 34962  # Vertex attributes
ELEMENT_ARRAY_BUFFER = 34963  # Indices


def convert_asset_to_glb(asset_data, asset_dir, output_file):
    """
    Convert an asset dictionary (loaded from a .pkl.gz file in asset_dir)
    into a binary glTF (.glb) file.
    This function processes both the geometry and texture information.
    """
    # --- GEOMETRY CONVERSION ---
    vertices_list = asset_data.get("vertices", [])
    normals_list = asset_data.get("normals", [])
    uvs_list = asset_data.get("uvs", [])
    triangles = asset_data.get("triangles", [])

    if not vertices_list or not triangles:
        raise ValueError("The asset must have at least vertices and triangles defined.")

    # Convert lists (of dicts) into NumPy arrays.
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

    # Get byte representations.
    vertices_bytes = vertices.tobytes()
    normals_bytes = normals.tobytes() if normals is not None else b""
    uvs_bytes = uvs.tobytes() if uvs is not None else b""
    indices_bytes = indices.tobytes()

    # Calculate offsets into a single concatenated buffer.
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

    # Combine all binary data into one buffer.
    combined_buffer = vertices_bytes + normals_bytes + uvs_bytes + indices_bytes
    encoded_buffer = base64.b64encode(combined_buffer).decode("utf-8")

    # --- INITIALIZE THE GLTF OBJECT ---
    gltf = GLTF2()
    gltf.asset = Asset(version="2.0")

    buffer = Buffer(
        byteLength=total_buffer_length,
        uri="data:application/octet-stream;base64," + encoded_buffer,
    )
    gltf.buffers.append(buffer)

    # --- CREATE BUFFERVIEWS ---
    vertices_bufferView = BufferView(
        buffer=0,
        byteOffset=vertices_offset,
        byteLength=vertices_length,
        target=ARRAY_BUFFER,
    )
    normals_bufferView = (
        BufferView(
            buffer=0,
            byteOffset=normals_offset,
            byteLength=normals_length,
            target=ARRAY_BUFFER,
        )
        if normals is not None
        else None
    )
    uvs_bufferView = (
        BufferView(
            buffer=0, byteOffset=uvs_offset, byteLength=uvs_length, target=ARRAY_BUFFER
        )
        if uvs is not None
        else None
    )
    indices_bufferView = BufferView(
        buffer=0,
        byteOffset=indices_offset,
        byteLength=indices_length,
        target=ELEMENT_ARRAY_BUFFER,
    )

    gltf.bufferViews.append(vertices_bufferView)
    vertices_bufferView_index = len(gltf.bufferViews) - 1
    if normals_bufferView is not None:
        gltf.bufferViews.append(normals_bufferView)
        normals_bufferView_index = len(gltf.bufferViews) - 1
    else:
        normals_bufferView_index = None
    if uvs_bufferView is not None:
        gltf.bufferViews.append(uvs_bufferView)
        uvs_bufferView_index = len(gltf.bufferViews) - 1
    else:
        uvs_bufferView_index = None
    gltf.bufferViews.append(indices_bufferView)
    indices_bufferView_index = len(gltf.bufferViews) - 1

    # --- CREATE ACCESSORS ---
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

    indices_accessor = Accessor(
        bufferView=indices_bufferView_index,
        byteOffset=0,
        componentType=UNSIGNED_SHORT,
        count=indices.shape[0],
        type="SCALAR",
    )
    gltf.accessors.append(indices_accessor)
    indices_accessor_index = len(gltf.accessors) - 1

    # --- CREATE MESH PRIMITIVE ---
    primitive_attributes = {"POSITION": vertices_accessor_index}
    if normals_accessor_index is not None:
        primitive_attributes["NORMAL"] = normals_accessor_index
    if uvs_accessor_index is not None:
        primitive_attributes["TEXCOORD_0"] = uvs_accessor_index

    primitive = {
        "attributes": primitive_attributes,
        "indices": indices_accessor_index,
        # Material will be assigned after creation.
    }
    mesh = Mesh(primitives=[primitive], name=asset_data.get("name", "Mesh"))
    gltf.meshes.append(mesh)
    mesh_index = len(gltf.meshes) - 1

    # --- BIND TEXTURES ---

    def load_texture(texture_path, mime_type="image/jpeg"):
        # Always load textures from asset_dir by taking only the basename
        filename = os.path.basename(texture_path)
        full_path = os.path.join(asset_dir, filename)
        if not os.path.exists(full_path):
            print(f"Warning: Texture file {full_path} not found.")
            return None
        with open(full_path, "rb") as img_file:
            img_data = img_file.read()
        img_b64 = base64.b64encode(img_data).decode("utf-8")
        data_uri = f"data:{mime_type};base64," + img_b64
        image = Image(uri=data_uri)
        gltf.images.append(image)
        image_index = len(gltf.images) - 1
        texture = Texture(source=image_index)
        gltf.textures.append(texture)
        texture_index = len(gltf.textures) - 1
        return texture_index

    # Load textures from the asset folder.
    albedo_texture_index = None
    normal_texture_index = None
    emission_texture_index = None
    metallic_texture_index = None  # if provided

    if asset_data.get("albedoTexturePath"):
        albedo_texture_index = load_texture(asset_data["albedoTexturePath"])
    if asset_data.get("normalTexturePath"):
        normal_texture_index = load_texture(asset_data["normalTexturePath"])
    if asset_data.get("emissionTexturePath"):
        emission_texture_index = load_texture(asset_data["emissionTexturePath"])
    if asset_data.get("metallicSmoothnessTexturePath"):
        metallic_texture_index = load_texture(
            asset_data["metallicSmoothnessTexturePath"]
        )

    # --- CREATE MATERIAL ---
    if (
        albedo_texture_index is not None
        or normal_texture_index is not None
        or emission_texture_index is not None
        or metallic_texture_index is not None
    ):
        mat = Material(
            name=asset_data.get("name", "MeshMaterial"),
            pbrMetallicRoughness=PbrMetallicRoughness(
                baseColorTexture=(
                    TextureInfo(index=albedo_texture_index)
                    if albedo_texture_index is not None
                    else None
                ),
                metallicFactor=0.0,  # Default: non-metallic
                roughnessFactor=1.0,  # Default: full roughness
            ),
            normalTexture=(
                TextureInfo(index=normal_texture_index)
                if normal_texture_index is not None
                else None
            ),
            emissiveTexture=(
                TextureInfo(index=emission_texture_index)
                if emission_texture_index is not None
                else None
            ),
            emissiveFactor=(
                [1.0, 1.0, 1.0] if emission_texture_index is not None else None
            ),
        )
    else:
        mat = Material(name=asset_data.get("name", "MeshMaterial"))
    gltf.materials.append(mat)
    material_index = len(gltf.materials) - 1

    # Set the material using dictionary assignment.
    gltf.meshes[mesh_index].primitives[0]["material"] = material_index

    # --- SET UP THE SCENE ---
    node = Node(mesh=mesh_index, name=asset_data.get("name", "Mesh"))
    gltf.nodes.append(node)
    node_index = len(gltf.nodes) - 1

    scene = Scene(nodes=[node_index])
    gltf.scenes.append(scene)
    gltf.scene = 0

    # --- SAVE THE GLB FILE ---
    gltf.save_binary(output_file)
    print(f"Conversion complete! glTF binary saved as {output_file}")


def convert_asset_folder_to_glb(asset_folder, output_file):
    """
    Read an asset folder that contains a single .pkl.gz asset file and the accompanying texture images.
    The .pkl.gz file is loaded, and then the asset (including texture bindings) is converted to a .glb file.
    """
    pkl_files = glob.glob(os.path.join(asset_folder, "*.pkl.gz"))
    if not pkl_files:
        raise ValueError(f"No .pkl.gz asset file found in folder: {asset_folder}")

    asset_file = pkl_files[0]
    print(f"Loading asset from: {asset_file}")
    with gzip.open(asset_file, "rb") as f:
        asset_data = pickle.load(f)

    convert_asset_to_glb(asset_data, asset_folder, output_file)


if __name__ == "__main__":
    # Example usage:
    asset_folder = "/home/dxv2k/.objathor-assets/2023_09_23/assets/03541b2ad507439d84f91bf739a0c1b8"
    output_glb = "converted_asset_with_texture.glb"
    convert_asset_folder_to_glb(asset_folder, output_glb)
