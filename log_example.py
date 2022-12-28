import pickle
from map_of_game import MapGenerateTool

map_generator = MapGenerateTool()

log = {
    "map": map_generator.generate_map(16, 7).get_map(),
    "num_of_region": 7,
    "agent_pos_init": (5, 5),
    "treasure_pos": (10, 10),
    "turn_pirate_reveal": 3,
    "turn_pirate_free": 5,
    "who_win": "agent",
    "machine_turn": [
        {
            "agent_pos": (0, 0),
            "list_tiles_not_include_treasure": [(1, 1), (2, 2)],
            "list_tiles_include_treasure": [(2, 2), (0, 9)],
            "pirate_pos": (3, 3)  # or None
        }
    ],
    "human_turn": [
        {
            "hint": "",
            "action_1": "",
            "action_2": "",
            "which_hint_checked": 1,
            "is_hint_checked_true": True
        }
    ]
}

with open('log.pickle', 'wb') as handle:
    pickle.dump(log, handle, protocol=pickle.HIGHEST_PROTOCOL)
