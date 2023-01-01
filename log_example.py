import pickle
from map_of_game import MapGenerateTool

map_generator = MapGenerateTool()

log = {
    "map": map_generator.generate_map(65, 20).get_map(),
    "num_of_region": 20,
    "agent_pos_init": (5, 5),
    "treasure_pos": (10, 10),
    "turn_pirate_reveal": 3,
    "turn_pirate_free": 5,
    "who_win": "agent",
    "machine_turn": [
        {
            "action_1":{
                "list_tiles_not_include_treasure": [(1, 1), (2, 2)],
                "description": "",
                "pos" : (0, 0)
                
            },
            "action_2":{
                "list_tiles_not_include_treasure": [(1, 1), (2, 2)],
                "description": "",
                "pos" : (0, 0)
                 "which_hint_checked": 1,
            "is_hint_checked_true": True
            },
            "hint":{
                "list_tiles" : [(0, 1)],
                "description" : ""
            },
            "pirate_pos": (3, 3),  # or None
            "which_hint_checked": 1,
            "is_hint_checked_true": True
        }
    ]
}

with open('log.pickle', 'wb') as handle:
    pickle.dump(log, handle, protocol=pickle.HIGHEST_PROTOCOL)
