## Experiment 1

**Category:** Object Placement

**Query:** A warehouse with a chair in the exact center.

![Experiment 1](../../data/scenes/A_warehouse_with_a_chair_in_th-2025-02-14-23-18-26-194195/A_warehouse_with_a_chair_in_th.png)

---

## Experiment 2

**Category:** Object Placement

**Query:** A warehouse with a table placed precisely in the middle.

![Experiment 2](../../data/scenes/A_warehouse_with_a_table_place-2025-02-14-23-20-41-828767/A_warehouse_with_a_table_place.png)

---

## Experiment 3

**Category:** Object Placement

**Query:** A warehouse with a single bed positioned at the center of the room.

![Experiment 3](../../data/scenes/A_warehouse_with_a_single_bed_-2025-02-14-23-23-52-955986/A_warehouse_with_a_single_bed_.png)

---

## Experiment 4

**Category:** Object Placement

**Query:** A warehouse with a lamp placed in the center of the floor.

![Experiment 4](../../data/scenes/A_warehouse_with_a_lamp_placed-2025-02-14-23-27-13-586879/A_warehouse_with_a_lamp_placed.png)

---

## Experiment 5

**Category:** Object Placement

**Query:** A warehouse with a painting hanging at the center of the main wall.

![Experiment 5](../../data/scenes/A_warehouse_with_a_painting_ha-2025-02-14-23-29-59-299676/A_warehouse_with_a_painting_ha.png)

---

## Experiment 6

**Category:** Object Placement

**Query:** A warehouse with a rectangular carpet exactly centered.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 7

**Category:** Object Placement

**Query:** A warehouse with a vending machine positioned in the middle.

![Experiment 7](../../data/scenes/A_warehouse_with_a_vending_mac-2025-02-14-23-33-02-436891/A_warehouse_with_a_vending_mac.png)

---

## Experiment 8

**Category:** Object Placement

**Query:** A warehouse with a desk placed symmetrically in the center.

![Experiment 8](../../data/scenes/A_warehouse_with_a_desk_placed-2025-02-14-23-35-56-627690/A_warehouse_with_a_desk_placed.png)

---

## Experiment 9

**Category:** Object Placement

**Query:** A warehouse with a television mounted at the center of the wall.

![Experiment 9](../../data/scenes/A_warehouse_with_a_television_-2025-02-14-23-38-38-379570/A_warehouse_with_a_television_.png)

---

## Experiment 10

**Category:** Object Placement

**Query:** A warehouse with a statue standing at the room's center.

![Experiment 10](../../data/scenes/A_warehouse_with_a_statue_stan-2025-02-14-23-42-07-655740/A_warehouse_with_a_statue_stan.png)

---

## Experiment 11

**Category:** Object Relationship

**Query:** A warehouse with a chair facing a desk.

![Experiment 11](../../data/scenes/A_warehouse_with_a_chair_facin-2025-02-14-23-48-02-847426/A_warehouse_with_a_chair_facin.png)

---

## Experiment 12

**Category:** Object Relationship

**Query:** A warehouse with a sofa facing a television, with a rug underneath.

![Experiment 12](../../data/scenes/A_warehouse_with_a_sofa_facing-2025-02-14-23-51-33-164218/A_warehouse_with_a_sofa_facing.png)

---

## Experiment 13

**Category:** Object Relationship

**Query:** A warehouse with a table positioned between two chairs.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 14

**Category:** Object Relationship

**Query:** A warehouse with a lamp placed next to a nightstand.

![Experiment 14](../../data/scenes/A_warehouse_with_a_lamp_placed-2025-02-14-23-54-40-210614/A_warehouse_with_a_lamp_placed.png)

---

## Experiment 15

**Category:** Object Relationship

**Query:** A warehouse with a painting above the couch.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 16

**Category:** Object Relationship

**Query:** A warehouse with a dining table surrounded by four chairs.

![Experiment 16](../../data/scenes/A_warehouse_with_a_dining_tabl-2025-02-14-23-57-52-046092/A_warehouse_with_a_dining_tabl.png)

---

## Experiment 17

**Category:** Object Relationship

**Query:** A warehouse with a bookshelf aligned against the wall.

![Experiment 17](../../data/scenes/A_warehouse_with_a_bookshelf_a-2025-02-14-23-59-50-785628/A_warehouse_with_a_bookshelf_a.png)

---

## Experiment 18

**Category:** Object Relationship

**Query:** A warehouse with a bed and a nightstand beside it.

![Experiment 18](../../data/scenes/A_warehouse_with_a_bed_and_a_n-2025-02-15-00-04-16-225903/A_warehouse_with_a_bed_and_a_n.png)

---

## Experiment 19

**Category:** Object Relationship

**Query:** A warehouse with a mirror mounted on the wall above a dresser.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 20

**Category:** Object Relationship

**Query:** A warehouse with a refrigerator placed next to a counter.

![Experiment 20](../../data/scenes/A_warehouse_with_a_refrigerato-2025-02-15-00-08-22-804808/A_warehouse_with_a_refrigerato.png)

---

## Experiment 21

**Category:** Object Overlap

**Query:** A warehouse with a chair inside another chair.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 69, in get_plan
    design2material = self.select_materials(all_designs, topk=5)
  File "./ai2holodeck/generation/rooms.py", line 203, in select_materials
    candidate_materials = self.material_selector.match_material(designs, topk=topk)[
  File "./ai2holodeck/generation/rooms.py", line 441, in match_material
    string_similarity + clip_similarity
RuntimeError: The size of tensor a (0) must match the size of tensor b (236) at non-singleton dimension 1
```

---

## Experiment 22

**Category:** Object Overlap

**Query:** A warehouse with a table placed over another table.

![Experiment 22](../../data/scenes/A_warehouse_with_a_table_place-2025-02-15-00-11-28-507740/A_warehouse_with_a_table_place.png)

---

## Experiment 23

**Category:** Object Overlap

**Query:** A warehouse with a desk overlapping a shelf.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 24

**Category:** Object Overlap

**Query:** A warehouse with a cabinet intersecting a fridge.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 25

**Category:** Object Overlap

**Query:** A warehouse with two beds stacked on top of each other.

![Experiment 25](../../data/scenes/A_warehouse_with_two_beds_stac-2025-02-15-00-14-43-680749/A_warehouse_with_two_beds_stac.png)

---

## Experiment 26

**Category:** Object Overlap

**Query:** A warehouse where a rug is floating above the floor.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 27

**Category:** Object Overlap

**Query:** A warehouse where a chair is embedded halfway into a couch.

![Experiment 27](../../data/scenes/A_warehouse_where_a_chair_is_e-2025-02-15-00-17-42-072460/A_warehouse_where_a_chair_is_e.png)

---

## Experiment 28

**Category:** Object Overlap

**Query:** A warehouse where a vending machine is inside another vending machine.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 29

**Category:** Object Overlap

**Query:** A warehouse where a bookshelf overlaps with a sofa.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 30

**Category:** Object Overlap

**Query:** A warehouse where a TV is inside a wall.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 301, in generate_scene
    scene = self.generate_windows(
  File "./ai2holodeck/generation/holodeck.py", line 196, in generate_windows
    raw_window_plan, walls, windows = self.window_generator.generate_windows(
  File "./ai2holodeck/generation/windows.py", line 102, in generate_windows
    window_id = self.select_window(
  File "./ai2holodeck/generation/windows.py", line 247, in select_window
    top_window_ids = sorted_window_ids[0]
IndexError: list index out of range
```

---

## Experiment 31

**Category:** Blocking & Accessibility

**Query:** A warehouse where the entrance is blocked by a stack of crates.

![Experiment 31](../../data/scenes/A_warehouse_where_the_entrance-2025-02-15-00-21-23-633048/A_warehouse_where_the_entrance.png)

---

## Experiment 32

**Category:** Blocking & Accessibility

**Query:** A warehouse where a forklift is obstructing the main door.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 33

**Category:** Blocking & Accessibility

**Query:** A warehouse where a car is parked inside, blocking access.

![Experiment 33](../../data/scenes/A_warehouse_where_a_car_is_par-2025-02-15-00-24-11-679692/A_warehouse_where_a_car_is_par.png)

---

## Experiment 34

**Category:** Blocking & Accessibility

**Query:** A warehouse with a barricade preventing movement.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 35

**Category:** Blocking & Accessibility

**Query:** A warehouse where boxes are blocking the staircase.

![Experiment 35](../../data/scenes/A_warehouse_where_boxes_are_bl-2025-02-15-00-27-14-765904/A_warehouse_where_boxes_are_bl.png)

---

## Experiment 36

**Category:** Blocking & Accessibility

**Query:** A warehouse where a large table obstructs the only exit.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 90, in parse_raw_plan
    room_type, floor_design, wall_design, vertices = plan.split("|")
ValueError: not enough values to unpack (expected 4, got 3)
```

---

## Experiment 37

**Category:** Blocking & Accessibility

**Query:** A warehouse where a chair is placed in front of a door, preventing entry.

![Experiment 37](../../data/scenes/A_warehouse_where_a_chair_is_p-2025-02-15-00-29-58-349220/A_warehouse_where_a_chair_is_p.png)

---

## Experiment 38

**Category:** Blocking & Accessibility

**Query:** A warehouse where a large rack is positioned in a narrow corridor.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 99, in parse_raw_plan
    vertices = ast.literal_eval(vertices.strip())
  File "/home/dxv2k/anaconda3/envs/holodeck/lib/python3.10/ast.py", line 64, in literal_eval
    node_or_string = parse(node_or_string.lstrip(" \t"), mode='eval')
  File "/home/dxv2k/anaconda3/envs/holodeck/lib/python3.10/ast.py", line 50, in parse
    return compile(source, filename, mode, flags,
  File "<unknown>", line 1
    within narrow corridor [(4, 1), (4, 5), (8, 5), (8, 1)]
           ^^^^^^
SyntaxError: invalid syntax
```

---

## Experiment 39

**Category:** Blocking & Accessibility

**Query:** A warehouse where a piece of machinery blocks the loading bay.

![Experiment 39](../../data/scenes/A_warehouse_where_a_piece_of_m-2025-02-15-00-34-35-518465/A_warehouse_where_a_piece_of_m.png)

---

## Experiment 40

**Category:** Blocking & Accessibility

**Query:** A warehouse where a sofa is placed in front of the emergency exit.

![Experiment 40](../../data/scenes/A_warehouse_where_a_sofa_is_pl-2025-02-15-00-38-11-479691/A_warehouse_where_a_sofa_is_pl.png)

---

## Experiment 41

**Category:** Scene Complexity

**Query:** A warehouse with a single chair in an empty room.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 42

**Category:** Scene Complexity

**Query:** A warehouse filled with scattered furniture.

![Experiment 42](../../data/scenes/A_warehouse_filled_with_scatte-2025-02-15-00-41-55-467240/A_warehouse_filled_with_scatte.png)

---

## Experiment 43

**Category:** Scene Complexity

**Query:** A warehouse with 100 chairs arranged in a grid.

![Experiment 43](../../data/scenes/A_warehouse_with_100_chairs_ar-2025-02-15-00-44-32-839197/A_warehouse_with_100_chairs_ar.png)

---

## Experiment 44

**Category:** Scene Complexity

**Query:** A warehouse with a chaotic mix of furniture and objects.

![Experiment 44](../../data/scenes/A_warehouse_with_a_chaotic_mix-2025-02-15-00-47-46-860357/A_warehouse_with_a_chaotic_mix.png)

---

## Experiment 45

**Category:** Scene Complexity

**Query:** A warehouse with shelves systematically arranged in rows.

![Experiment 45](../../data/scenes/A_warehouse_with_shelves_syste-2025-02-15-00-50-29-856149/A_warehouse_with_shelves_syste.png)

---

## Experiment 46

**Category:** Scene Complexity

**Query:** A warehouse with objects stacked chaotically on top of each other.

![Experiment 46](../../data/scenes/A_warehouse_with_objects_stack-2025-02-15-00-52-48-169571/A_warehouse_with_objects_stack.png)

---

## Experiment 47

**Category:** Scene Complexity

**Query:** A warehouse with an open floor space but a cluttered corner.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 48

**Category:** Scene Complexity

**Query:** A warehouse with 20 tables and 50 chairs arranged for an event.

![Experiment 48](../../data/scenes/A_warehouse_with_20_tables_and-2025-02-15-00-56-24-450101/A_warehouse_with_20_tables_and.png)

---

## Experiment 49

**Category:** Scene Complexity

**Query:** A warehouse where objects are placed randomly without structure.

![Experiment 49](../../data/scenes/A_warehouse_where_objects_are_-2025-02-15-00-59-27-359860/A_warehouse_where_objects_are_.png)

---

## Experiment 50

**Category:** Scene Complexity

**Query:** A warehouse with perfectly symmetrical object placement.

![Experiment 50](../../data/scenes/A_warehouse_with_perfectly_sym-2025-02-15-01-02-13-300053/A_warehouse_with_perfectly_sym.png)

---

## Experiment 51

**Category:** Style & Theme

**Query:** A medieval-style warehouse with wooden furniture.

![Experiment 51](../../data/scenes/A_medieval-style_warehouse_wit-2025-02-15-01-08-49-019897/A_medieval-style_warehouse_wit.png)

---

## Experiment 52

**Category:** Style & Theme

**Query:** A futuristic warehouse with neon-lit shelves.

![Experiment 52](../../data/scenes/A_futuristic_warehouse_with_ne-2025-02-15-01-11-04-102962/A_futuristic_warehouse_with_ne.png)

---

## Experiment 53

**Category:** Style & Theme

**Query:** A minimalist warehouse with only essential furniture.

![Experiment 53](../../data/scenes/A_minimalist_warehouse_with_on-2025-02-15-01-16-28-720138/A_minimalist_warehouse_with_on.png)

---

## Experiment 54

**Category:** Style & Theme

**Query:** A rustic warehouse with wooden crates and old decorations.

![Experiment 54](../../data/scenes/A_rustic_warehouse_with_wooden-2025-02-15-01-20-06-228701/A_rustic_warehouse_with_wooden.png)

---

## Experiment 55

**Category:** Style & Theme

**Query:** A cyberpunk warehouse with holographic elements.

![Experiment 55](../../data/scenes/A_cyberpunk_warehouse_with_hol-2025-02-15-01-26-10-711652/A_cyberpunk_warehouse_with_hol.png)

---

## Experiment 56

**Category:** Style & Theme

**Query:** A Victorian-style warehouse with antique furniture.

![Experiment 56](../../data/scenes/A_Victorian-style_warehouse_wi-2025-02-15-01-35-12-841571/A_Victorian-style_warehouse_wi.png)

---

## Experiment 57

**Category:** Style & Theme

**Query:** A warehouse that looks like a sci-fi spaceship interior.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 1070, in step
    self.last_event = self.server.receive()
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/fifo_server.py", line 262, in receive
    metadata, files = self._recv_message(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/fifo_server.py", line 179, in _recv_message
    header = self._read_with_timeout(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/fifo_server.py", line 147, in _read_with_timeout
    raise TimeoutError(
TimeoutError: Reading from AI2-THOR backend timed out (using 100.0s) timeout.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 334, in generate_scene
    scene = self.generate_small_objects(scene, used_assets=used_assets)
  File "./ai2holodeck/generation/holodeck.py", line 226, in generate_small_objects
    controller = self.small_object_generator.start_controller(
  File "./ai2holodeck/generation/small_objects.py", line 287, in start_controller
    controller = Controller(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 618, in __init__
    event = self.reset(scene)
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 777, in reset
    self.last_event = self.step(action="CreateHouse", house=scene)
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 1066, in step
    self.run_action_hook(action)
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 997, in run_action_hook
    event = method(action, self)
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/hooks/procedural_asset_hook.py", line 109, in CreateHouse
    return create_assets_if_not_exist(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/hooks/procedural_asset_hook.py", line 58, in create_assets_if_not_exist
    evt = create_asset(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/util/runtime_assets.py", line 327, in create_asset
    evt = thor_controller.step(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 1092, in step
    raise (TimeoutError if isinstance(e, TimeoutError) else RuntimeError)(
TimeoutError: Error encountered when running action {'action': 'CreateRuntimeAsset', 'asset': {'action': 'CreateObjectPrefab', 'name': 'b765d3d9d46f4178bac931b47acbd4b3', 'receptacleCandidate': True, 'albedoTexturePath': '/home/dxv2k/.ai2thor/releases/thor-Linux64-3213d486cd09bcbafce33561997355983bdf8d1a/processed_models/b765d3d9d46f4178bac931b47acbd4b3/albedo.jpg', 'normalTexturePath': '/home/dxv2k/.ai2thor/releases/thor-Linux64-3213d486cd09bcbafce33561997355983bdf8d1a/processed_models/b765d3d9d46f4178bac931b47acbd4b3/normal.jpg', 'emissionTexturePath': '/home/dxv2k/.ai2thor/releases/thor-Linux64-3213d486cd09bcbafce33561997355983bdf8d1a/processed_models/b765d3d9d46f4178bac931b47acbd4b3/emission.jpg', 'vertices': [{'x': 0.29167421904177404, 'y': 0.006213910211179459, 'z': -0.07122233916277902}, {'x': 0.27602690215557135, 'y': 0.004885275197245787, 'z': -0.09495804059825287}, {'x': 0.2827433169030601, 'y': 0.007696929112940381, 'z': -0.09876034539995}, {'x': 0.2971883633596852, 'y': 0.012 ... p', 'secondaryProperties': []}}, 'sequenceId': 24} in scene Procedural.
```

---

## Experiment 58

**Category:** Style & Theme

**Query:** A luxury warehouse with golden accents and modern furniture.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: No vertex of a room can be inside another room.
```

---

## Experiment 59

**Category:** Style & Theme

**Query:** A haunted warehouse with old, broken furniture and dim lighting.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 1070, in step
    self.last_event = self.server.receive()
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/fifo_server.py", line 262, in receive
    metadata, files = self._recv_message(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/fifo_server.py", line 179, in _recv_message
    header = self._read_with_timeout(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/fifo_server.py", line 147, in _read_with_timeout
    raise TimeoutError(
TimeoutError: Reading from AI2-THOR backend timed out (using 100.0s) timeout.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 389, in generate_scene
    top_image = get_top_down_frame(scene, self.objaverse_asset_dir, 1024, 1024)
  File "./ai2holodeck/generation/utils.py", line 84, in get_top_down_frame
    event = controller.step(
  File "/home/dxv2k/.local/lib/python3.10/site-packages/ai2thor/controller.py", line 1092, in step
    raise (TimeoutError if isinstance(e, TimeoutError) else RuntimeError)(
TimeoutError: Error encountered when running action {'action': 'AddThirdPartyCamera', 'position': {'x': 6.5, 'y': 10.761123180389404, 'z': 4.0}, 'rotation': {'x': 90.0, 'y': 0.0, 'z': 0.0}, 'orthographic': False, 'fieldOfView': 60, 'farClippingPlane': 20.761123180389404, 'nearClippingPlane': 6.761123180389404, 'skyboxColor': 'white', 'sequenceId': 59} in scene Procedural.
```

---

## Experiment 60

**Category:** Style & Theme

**Query:** A post-apocalyptic warehouse with abandoned, worn-out objects.

![Experiment 60](../../data/scenes/A_post-apocalyptic_warehouse_w-2025-02-15-02-02-17-074395/A_post-apocalyptic_warehouse_w.png)

---

## Experiment 61

**Category:** Object Scaling

**Query:** A warehouse with an oversized sofa in the middle.

![Experiment 61](../../data/scenes/A_warehouse_with_an_oversized_-2025-02-15-02-05-47-055702/A_warehouse_with_an_oversized_.png)

---

## Experiment 62

**Category:** Object Scaling

**Query:** A warehouse with a tiny chair next to a massive table.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Room polygons must not overlap.
```

---

## Experiment 63

**Category:** Object Scaling

**Query:** A warehouse where every object is scaled to double its normal size.

![Experiment 63](../../data/scenes/A_warehouse_where_every_object-2025-02-15-02-08-54-470987/A_warehouse_where_every_object.png)

---

## Experiment 64

**Category:** Object Scaling

**Query:** A warehouse with an extremely large chandelier hanging from the ceiling.

![Experiment 64](../../data/scenes/A_warehouse_with_an_extremely_-2025-02-15-02-12-44-469491/A_warehouse_with_an_extremely_.png)

---

## Experiment 65

**Category:** Object Scaling

**Query:** A warehouse with a miniaturized version of furniture.

![Experiment 65](../../data/scenes/A_warehouse_with_a_miniaturize-2025-02-15-02-15-34-872330/A_warehouse_with_a_miniaturize.png)

---

## Experiment 66

**Category:** Object Scaling

**Query:** A warehouse with a bed that is ten times its normal size.

![Experiment 66](../../data/scenes/A_warehouse_with_a_bed_that_is-2025-02-15-02-19-23-982690/A_warehouse_with_a_bed_that_is.png)

---

## Experiment 67

**Category:** Object Scaling

**Query:** A warehouse with a normal-sized desk but a gigantic lamp.

![Experiment 67](../../data/scenes/A_warehouse_with_a_normal-size-2025-02-15-02-21-51-670188/A_warehouse_with_a_normal-size.png)

---

## Experiment 68

**Category:** Object Scaling

**Query:** A warehouse where a tiny vending machine is next to a massive refrigerator.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 143, in parse_raw_plan
    raise ValueError(msg)
ValueError: Each room polygon must share an edge with at least one other room polygon.
```

---

## Experiment 69

**Category:** Object Scaling

**Query:** A warehouse with chairs that are much smaller than usual.

![Experiment 69](../../data/scenes/A_warehouse_with_chairs_that_a-2025-02-15-02-26-21-750899/A_warehouse_with_chairs_that_a.png)

---

## Experiment 70

**Category:** Object Scaling

**Query:** A warehouse where objects are scaled randomly, creating a surreal effect.

![Experiment 70](../../data/scenes/A_warehouse_where_objects_are_-2025-02-15-02-28-53-193539/A_warehouse_where_objects_are_.png)

---

## Experiment 71

**Category:** Lighting & Environment

**Query:** A dimly lit warehouse with a single hanging lightbulb.

![Experiment 71](../../data/scenes/A_dimly_lit_warehouse_with_a_s-2025-02-15-02-31-41-061632/A_dimly_lit_warehouse_with_a_s.png)

---

## Experiment 72

**Category:** Lighting & Environment

**Query:** A warehouse illuminated by neon floor lights.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 90, in parse_raw_plan
    room_type, floor_design, wall_design, vertices = plan.split("|")
ValueError: too many values to unpack (expected 4)
```

---

## Experiment 73

**Category:** Lighting & Environment

**Query:** A warehouse where the lighting is completely dark except for one spotlight.

![Experiment 73](../../data/scenes/A_warehouse_where_the_lighting-2025-02-15-02-34-44-137779/A_warehouse_where_the_lighting.png)

---

## Experiment 74

**Category:** Lighting & Environment

**Query:** A warehouse lit only by natural sunlight coming from windows.

![Experiment 74](../../data/scenes/A_warehouse_lit_only_by_natura-2025-02-15-02-36-46-806274/A_warehouse_lit_only_by_natura.png)

---

## Experiment 75

**Category:** Lighting & Environment

**Query:** A warehouse with flickering lights giving an eerie atmosphere.

![Experiment 75](../../data/scenes/A_warehouse_with_flickering_li-2025-02-15-02-39-33-739451/A_warehouse_with_flickering_li.png)

---

## Experiment 76

**Category:** Lighting & Environment

**Query:** A warehouse with warm yellow lighting, creating a cozy feel.

_No image found._

**Error Log:**
```
Traceback (most recent call last):
  File "./ai2holodeck/exp_runner.py", line 131, in generate_all_experiments
    save_dir = generate_single_scene(args)
  File "./ai2holodeck/exp_runner.py", line 57, in generate_single_scene
    _, save_dir = args.model.generate_scene(
  File "./ai2holodeck/generation/holodeck.py", line 282, in generate_scene
    scene = self.generate_rooms(
  File "./ai2holodeck/generation/holodeck.py", line 156, in generate_rooms
    rooms = self.floor_generator.generate_rooms(scene, additional_requirements_room)
  File "./ai2holodeck/generation/rooms.py", line 58, in generate_rooms
    rooms = self.get_plan(scene["query"], scene["raw_floor_plan"], visualize)
  File "./ai2holodeck/generation/rooms.py", line 62, in get_plan
    parsed_plan = self.parse_raw_plan(raw_plan)
  File "./ai2holodeck/generation/rooms.py", line 90, in parse_raw_plan
    room_type, floor_design, wall_design, vertices = plan.split("|")
ValueError: too many values to unpack (expected 4)
```

---

## Experiment 77

**Category:** Lighting & Environment

**Query:** A warehouse with blue LED lighting, making it look futuristic.

![Experiment 77](../../data/scenes/A_warehouse_with_blue_LED_ligh-2025-02-15-02-42-56-828429/A_warehouse_with_blue_LED_ligh.png)

---

## Experiment 78

**Category:** Lighting & Environment

**Query:** A warehouse where shadows are exaggerated due to strong lighting contrast.

![Experiment 78](../../data/scenes/A_warehouse_where_shadows_are_-2025-02-15-02-45-01-220953/A_warehouse_where_shadows_are_.png)

---

## Experiment 79

**Category:** Lighting & Environment

**Query:** A warehouse with a foggy atmosphere affecting visibility.

![Experiment 79](../../data/scenes/A_warehouse_with_a_foggy_atmos-2025-02-15-02-46-56-910272/A_warehouse_with_a_foggy_atmos.png)

---

## Experiment 80

**Category:** Lighting & Environment

**Query:** A warehouse where light sources are scattered unevenly, causing random bright and dark spots.

![Experiment 80](../../data/scenes/A_warehouse_where_light_source-2025-02-15-02-49-07-349720/A_warehouse_where_light_source.png)

---
