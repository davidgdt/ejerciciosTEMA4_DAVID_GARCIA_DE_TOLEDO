import random

class Mission:
    def __init__(self, mission_type, planet, general):
        self.mission_type = mission_type
        self.planet = planet
        self.general = general
        self.priority = self.set_priority()
        self.resources = self.assign_resources()

    def set_priority(self):
        high_priority_generals = ["Palpatine", "Darth Vader"]
        return "high" if self.general in high_priority_generals else "low"

    def assign_resources(self):
        if self.priority == "high":
            return "Manual assignment"

        vehicles = {
            "exploration": ("Scout Troopers", 15, "speeder bike", 2),
            "containment": ("Stormtroopers", 30, "random vehicles", 3),
            "attack": ("Stormtroopers", 50, "random vehicles", 7)
        }
        return vehicles[self.mission_type]

    def __str__(self):
        return f"Mission: {self.mission_type}, Planet: {self.planet}, General: {self.general}, Priority: {self.priority}, Resources: {self.resources}"

def create_mission(mission_type, planet, general):
    return Mission(mission_type, planet, general)

def display_missions(missions):
    for mission in missions:
        print(mission)

def add_mission(missions, mission_type, planet, general):
    missions.append(create_mission(mission_type, planet, general))

def total_resources_assigned(missions):
    resources = {"Scout Troopers": 0, "Stormtroopers": 0, "speeder bike": 0}
    for mission in missions:
        if mission.priority == "low":
            resources[mission.resources[0]] += mission.resources[1]
            if mission.resources[2] == "random vehicles":
                resources["speeder bike"] += mission.resources[3]
    return resources

# Ejemplo de uso:
missions = [
    create_mission("exploration", "Tatooine", "General Rieekan"),
    create_mission("containment", "Hoth", "Darth Vader"),
    create_mission("attack", "Endor", "Palpatine")
]

display_missions(missions)

add_mission(missions, "exploration", "Jakku", "General Hux")
add_mission(missions, "containment", "Naboo", "General Veers")

print("\nMissions after adding new requests:")
display_missions(missions)

print("\nTotal resources assigned:")
print(total_resources_assigned(missions))
