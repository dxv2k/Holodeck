import gzip
import pickle
import os
from pxr import Usd, UsdGeom, UsdShade, Sdf, Gf


def convert_to_GfVec3f(data):
    """
    Convert a dictionary with keys 'x', 'y', and 'z' into a Gf.Vec3f.
    """
    return Gf.Vec3f(data["x"], data["y"], data["z"])


def convert_to_GfVec2f(data):
    """
    Convert a dictionary with keys 'x' and 'y' into a Gf.Vec2f.
    """
    return Gf.Vec2f(data["x"], data["y"])


# Path to the asset file (.pkl.gz)
asset_file = "/home/dxv2k/.objathor-assets/2023_09_23/assets/03541b2ad507439d84f91bf739a0c1b8/03541b2ad507439d84f91bf739a0c1b8.pkl.gz"
with gzip.open(asset_file, "rb") as f:
    asset_data = pickle.load(f)

print("Asset Data Keys:", asset_data.keys())

# --- CONVERSION OF ASSET DATA ---

# Convert vertices: asset_data['vertices'] is a list of dicts with keys 'x', 'y', 'z'
vertices_data = asset_data.get("vertices", [])
converted_vertices = [convert_to_GfVec3f(v) for v in vertices_data]
print("Converted vertices count:", len(converted_vertices))

# Convert normals if available: asset_data['normals'] is a list of dicts with 'x', 'y', 'z'
normals_data = asset_data.get("normals", None)
converted_normals = None
if normals_data:
    converted_normals = [convert_to_GfVec3f(n) for n in normals_data]
    print("Converted normals count:", len(converted_normals))
else:
    print("No normals data found.")

# Convert UVs if available: asset_data['uvs'] is a list of dicts with 'x' and 'y'
uvs_data = asset_data.get("uvs", None)
converted_uvs = None
if uvs_data:
    converted_uvs = [convert_to_GfVec2f(uv) for uv in uvs_data]
    print("Converted UVs count:", len(converted_uvs))
else:
    print("No uvs data found.")

# Get triangles (face indices) as a flat list.
triangles = asset_data.get("triangles", [])
print("Triangles count (total indices):", len(triangles))
# For a triangle mesh, each face has exactly 3 vertices.
face_vertex_counts = [3] * (len(triangles) // 3)
print("Total triangle faces:", len(face_vertex_counts))

# --- CREATING THE USD STAGE AND MESH ---

# Create a new USD stage
usd_file = "converted_asset.usd"
stage = Usd.Stage.CreateNew(usd_file)

# Create a root transform prim for the asset
root_prim = stage.DefinePrim("/Asset", "Xform")

# Create the Mesh under /Asset
mesh_path = "/Asset/Mesh"
mesh = UsdGeom.Mesh.Define(stage, mesh_path)
mesh.GetPointsAttr().Set(converted_vertices)
mesh.GetFaceVertexIndicesAttr().Set(triangles)
mesh.GetFaceVertexCountsAttr().Set(face_vertex_counts)

# Optionally assign normals if available
if converted_normals:
    mesh.GetNormalsAttr().Set(converted_normals)

# Optionally assign UVs if available;
# Create a prim attribute "st" with type TexCoord2fArray for texture coordinates.
if converted_uvs:
    st_attr = mesh.GetPrim().CreateAttribute("st", Sdf.ValueTypeNames.TexCoord2fArray)
    st_attr.Set(converted_uvs)

# --- ASSIGNING A BASIC MATERIAL USING USD SHADE ---

# Create a material prim under /Asset/Material and set up a simple PBR shader.
material_path = "/Asset/Material"
material = UsdShade.Material.Define(stage, material_path)
shader_path = material_path + "/PBRShader"
shader = UsdShade.Shader.Define(stage, shader_path)
shader.CreateIdAttr("UsdPreviewSurface")

# Set a default diffuse color.
shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((1.0, 1.0, 1.0))

# Explicitly create the "surface" output attribute.
surface_output = shader.CreateOutput("surface", Sdf.ValueTypeNames.Token)

# Connect the shader's surface output to the material
material.CreateSurfaceOutput().ConnectToSource(surface_output)

# Bind the material to the mesh
UsdShade.MaterialBindingAPI(mesh.GetPrim()).Bind(material)

# --- SAVE THE USD FILE ---
stage.GetRootLayer().Save()
print(f"Conversion complete! USD file saved as {usd_file}")
