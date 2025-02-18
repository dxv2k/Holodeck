import matplotlib.pyplot as plt
import matplotlib.patches as patches
import re
import ast

def compute_polygon_centroid(vertices):
    """
    Compute the centroid of a polygon defined by 'vertices' using the 
    area-weighted centroid method. If the area is 0 (degenerate polygon),
    fall back to the arithmetic mean of vertices.
    """
    if len(vertices) < 3:
        # If less than 3 vertices, return the simple average.
        x = sum(v[0] for v in vertices) / len(vertices)
        y = sum(v[1] for v in vertices) / len(vertices)
        return x, y
    
    # Ensure the polygon is closed.
    closed_vertices = vertices
    if vertices[0] != vertices[-1]:
        closed_vertices = vertices + [vertices[0]]
    
    area = 0
    cx = 0
    cy = 0
    for i in range(len(closed_vertices) - 1):
        x0, y0 = closed_vertices[i]
        x1, y1 = closed_vertices[i+1]
        cross = x0 * y1 - x1 * y0
        area += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    area = area / 2.0
    if area == 0:
        # Fall back to simple average.
        x = sum(v[0] for v in vertices) / len(vertices)
        y = sum(v[1] for v in vertices) / len(vertices)
        return x, y
    cx = cx / (6 * area)
    cy = cy / (6 * area)
    return cx, cy

def visualize_floor_plan(raw_plan: str, output_file: str = None):
    """
    Parses the raw floor plan text and visualizes the rooms as filled polygons.
    
    Expected input lines have the following format:
      {id}. {Room Name} | {Floor design} | {Wall design} | {Polygon coordinates}
      
    Example line:
      3. Open Office Area (First Floor) | grey carpet tile, medium | light grey drywall, smooth | [(0, 10), (0, 25), (50, 25), (50, 10)]
    
    If output_file is provided, the visualization is saved to that file.
    Otherwise, the visualization is displayed in an interactive window.
    """
    # Regex pattern to match lines with room information.
    pattern = re.compile(r"^\s*(\d+)\.\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\[.*\])\s*$")
    rooms = []
    
    for line in raw_plan.splitlines():
        line = line.strip()
        if not line:
            continue
        # Skip any system or error lines.
        if line.startswith("AI:") or line.startswith("[ERROR]"):
            continue
        match = pattern.match(line)
        if match:
            room_id = int(match.group(1))
            room_name = match.group(2)
            floor_design = match.group(3)
            wall_design = match.group(4)
            polygon_str = match.group(5)
            try:
                polygon = ast.literal_eval(polygon_str)
            except Exception as e:
                print(f"Error parsing polygon for room {room_name}: {e}")
                continue
            rooms.append({
                "id": room_id,
                "name": room_name,
                "floor_design": floor_design,
                "wall_design": wall_design,
                "polygon": polygon
            })
        else:
            print(f"Skipping line (unrecognized format): {line}")
    
    if not rooms:
        print("No valid room data found.")
        return
    
    # Create the plot.
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect("equal")
    
    # Set different colors for each room.
    cmap = plt.get_cmap("tab10")
    
    # Determine plot limits based on all vertices.
    all_x = []
    all_y = []
    for room in rooms:
        xs = [pt[0] for pt in room["polygon"]]
        ys = [pt[1] for pt in room["polygon"]]
        all_x.extend(xs)
        all_y.extend(ys)
    margin = 5
    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
    
    # Plot each room and add a label at its centroid.
    for i, room in enumerate(rooms):
        poly_pts = room["polygon"]
        patch = patches.Polygon(
            poly_pts, 
            closed=True, 
            fill=True, 
            color=cmap(i % 10),
            alpha=0.3, 
            edgecolor='black', 
            linewidth=2
        )
        ax.add_patch(patch)
        # Compute centroid for the room label.
        cx, cy = compute_polygon_centroid(poly_pts)
        ax.text(cx, cy, room["name"], fontsize=10, ha='center', va='center', fontweight='bold')
    
    ax.set_title("Floor Plan Visualization")
    ax.set_xlabel("X Coordinate (meters)")
    ax.set_ylabel("Y Coordinate (meters)")
    plt.grid(True)
    
    # Dump the plot to a file or display it.
    if output_file:
        plt.savefig(output_file)
        print(f"Floor plan visualization saved to '{output_file}'")
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    # Sample raw floor plan text (as provided by the AI)
    raw_plan = """
1. Lobby | polished concrete, glossy | white drywall, smooth | [(0, 0), (0, 10), (10, 10), (10, 0)]
2. Reception Area | polished concrete, glossy | white drywall, smooth | [(10, 0), (10, 10), (20, 10), (20, 0)]
3. Open Office Area (First Floor) | grey carpet tile, medium | light grey drywall, smooth | [(0, 10), (0, 25), (50, 25), (50, 10)]
4. Workstation Zone (First Floor) | grey carpet tile, medium | light grey drywall, smooth | [(10, 10), (10, 25), (40, 25), (40, 10)]
5. Utility Room (Second Floor) | vinyl tile, smooth | white drywall, smooth | [(40, 10), (40, 15), (45, 15), (45, 10)]
6. Corridor (Second Floor) | grey carpet tile, medium | light grey drywall, smooth | [(0, 10), (0, 12), (50, 12), (50, 10)]
7. Open Office Area (Second Floor) | grey carpet tile, medium | light grey drywall, smooth | [(0, 12), (0, 25), (50, 25), (50, 12)]
8. Workstation Zone (Second Floor) | grey carpet tile, medium | light grey drywall, smooth | [(10, 12), (10, 25), (40, 25), (40, 12)]
9. Front Exit | polished concrete, glossy | white drywall, smooth | [(0, 0), (0, 5), (5, 5), (5, 0)]
10. Emergency Exit (Back) | polished concrete, glossy | white drywall, smooth | [(0, 25), (0, 30), (5, 30), (5, 25)]
"""
    # Specify the output file path for saving the visualization.
    output_filename = "floor_plan_visualization.png"
    visualize_floor_plan(raw_plan, output_file=output_filename)
