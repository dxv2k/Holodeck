import os
from openai import OpenAI
from pprint import pprint


class SceneDescriptionGenerator:
    """
    A class to generate structured scene descriptions for fire evacuation scenarios
    using OpenAI's GPT models.
    """

    def __init__(self, model="gpt-4o", api_key=None):
        self.model = model
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))

        self.env_params = {
            "floors": 0,
            "length": 0,
            "width": 0,
            "height": 0,
            "material_type": "",
            "temperature": "",
            "fire_location": "",
        }

        # Reference example for validation and output structure
        self.reference_output = {
            "scene_description": """
The three-story commercial building stretches 50 meters in length and 30 meters in width, with each floor reaching 4 meters in height. The main entrance, featuring glass double doors, is centered on the front facade. A spacious reception area greets visitors, with a curved desk positioned 3 meters from the entrance, oriented to face both incoming traffic and the central corridor.

The central corridor, 3 meters wide, runs the building's length, with offices and meeting rooms flanking both sides. On the left side, workstations are arranged in clusters of four, maintaining 2-meter spacing between groups. The right side features enclosed offices with glass walls, each measuring 5x4 meters.

The fire originates in the central kitchen on the first floor, approximately 20 meters from the main entrance. Thick smoke billows upward through the central stairwell, creating a gradient of visibility that deteriorates from front to back. The smoke's density is heaviest near the kitchen and progressively thins towards the building's front.

Emergency systems are strategically placed:
- Fire alarms: Every 15 meters along corridors
- Sprinklers: Grid pattern on ceiling, 3-meter spacing
- Exit signs: Above all doorways, with enhanced visibility at corridor intersections

Occupant clusters are currently positioned:
- Group A: Near the left stairwell, second floor
- Group B: Reception area, first floor
- Group C: Right wing offices, third floor

The external assembly point is located 30 meters from the main entrance, marked by yellow lines and illuminated signage."""
        }

    def set_parameters(self, **kwargs):
        """Set environmental parameters for the scene."""
        valid_params = self.env_params.keys()
        for key, value in kwargs.items():
            if key in valid_params:
                self.env_params[key] = value
            else:
                raise ValueError(f"Invalid parameter: {key}")

    def generate_prompt(self):
        """Generate the LLM prompt based on the set parameters."""
        return f"""
You are tasked with constructing a virtual fire evacuation scene. 
Generate a concise scene description (around 50 words total). 
Keep descriptions simple, clear and brief.

Example 1:
<scene>
  <building>
    <floors>2</floors>
    <dimensions>
      <length>40</length>
      <width>20</width>
      <height>3</height>
    </dimensions>
    <materials>brick</materials>
    <temperature>22°C</temperature>
  </building>
  <emergency>
    <fire>
      <location>lobby</location>
      <smoke>Smoke near fire source</smoke>
    </fire>
    <systems>
      <alarms>Near exits</alarms>
      <sprinklers>Ceiling mounted</sprinklers>
      <signs>Above doors</signs>
    </systems>
  </emergency>
  <layout>
    <mainEntrance>Front entrance with wooden doors</mainEntrance>
    <corridor>Central corridor</corridor>
    <rooms>Meeting rooms on both sides</rooms>
    <furniture>
      <reception>Front desk</reception>
      <workstations>Desk clusters</workstations>
      <offices>Glass-walled rooms</offices>
    </furniture>
  </layout>
  <occupants>
    <groupA>First floor</groupA>
    <groupB>Ground floor</groupB>
  </occupants>
  <exterior>
    <assemblyPoint>Back of building</assemblyPoint>
    <markings>Safety signs</markings>
  </exterior>
</scene>

Example 2:
<scene>
  <building>
    <floors>4</floors>
    <dimensions>
      <length>60</length>
      <width>40</width>
      <height>4</height>
    </dimensions>
    <materials>steel and glass</materials>
    <temperature>25°C</temperature>
  </building>
  <emergency>
    <fire>
      <location>server room</location>
      <smoke>Smoke near fire source</smoke>
    </fire>
    <systems>
      <alarms>Near exits</alarms>
      <sprinklers>Ceiling mounted</sprinklers>
      <signs>Above doors</signs>
    </systems>
  </emergency>
  <layout>
    <mainEntrance>Side entrance with automatic doors</mainEntrance>
    <corridor>Wide corridor</corridor>
    <rooms>Labs on both sides</rooms>
    <furniture>
      <reception>Information desk</reception>
      <workstations>Lab benches</workstations>
      <offices>Private offices</offices>
    </furniture>
  </layout>
  <occupants>
    <groupA>Third floor</groupA>
    <groupB>Second floor</groupB>
  </occupants>
  <exterior>
    <assemblyPoint>Side of building</assemblyPoint>
    <markings>Emergency signs</markings>
  </exterior>
</scene>

<scene>
  <building>
    <floors>{self.env_params['floors']}</floors>
    <dimensions>
      <length>{self.env_params['length']}</length>
      <width>{self.env_params['width']}</width>
      <height>{self.env_params['height']}</height>
    </dimensions>
    <materials>{self.env_params['material_type']}</materials>
    <temperature>{self.env_params['temperature']}</temperature>
  </building>

  <emergency>
    <fire>
      <location>{self.env_params['fire_location']}</location>
      <smoke>Smoke near fire source</smoke>
    </fire>
    <systems>
      <alarms>Near exits</alarms>
      <sprinklers>Ceiling mounted</sprinklers>
      <signs>Above doors</signs>
    </systems>
  </emergency>

  <layout>
    <mainEntrance>Front entrance with glass doors</mainEntrance>
    <corridor>Central corridor</corridor>
    <rooms>Offices on both sides</rooms>
    <furniture>
      <reception>Front desk</reception>
      <workstations>Desk clusters</workstations>
      <offices>Glass-walled rooms</offices>
    </furniture>
  </layout>

  <occupants>
    <groupA>Second floor</groupA>
    <groupB>First floor</groupB>
    <groupC>Third floor</groupC>
  </occupants>

  <exterior>
    <assemblyPoint>Front of building</assemblyPoint>
    <markings>Safety signs</markings>
  </exterior>
</scene>

Remember to response a short narrative (in string, not XML) to condense all of the above requirements.
"""

    def generate_scene(self):
        """Generate the scene description using OpenAI's API."""
        if not all(self.env_params.values()):
            raise ValueError(
                "All environmental parameters must be set before generating a scene"
            )

        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in architectural description and emergency scenario planning.",
                    },
                    {"role": "user", "content": self.generate_prompt()},
                ],
                model=self.model,
                temperature=0.7,
                max_tokens=1000,
            )

            scene_description = response.choices[0].message.content
            return {"scene_description": scene_description}

        except Exception as e:
            print(f"Error generating scene: {str(e)}")
            return None

    def validate_scene(self, scene):
        """Validate that the scene description meets all required criteria."""
        if not scene:
            return False

        required_elements = [
            "main entrance",
            "corridor",
            "fire",
            "smoke",
            "emergency systems",
            "occupant",
        ]

        description = scene.get("scene_description", "").lower()
        return all(element in description for element in required_elements)


# Example usage:
if __name__ == "__main__":
    # Create generator instance
    generator = SceneDescriptionGenerator(model="gpt-4o")

    # Set parameters
    generator.set_parameters(
        floors=3,
        length=50,
        width=30,
        height=4,
        material_type="concrete and steel",
        temperature="23°C",
        fire_location="central kitchen on the first floor",
    )

    # Generate scene using OpenAI
    scene = generator.generate_scene()
    pprint(scene)

    # Validate and print the scene
    if scene and generator.validate_scene(scene):
        print("Generated Scene Description:")
        print("-" * 50)
        print(scene["scene_description"])
    else:
        print("Generated scene description failed validation!")
