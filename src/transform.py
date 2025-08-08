"""Transform raw PokeAPI JSON → tidy rows"""
def extract_row(p):
    name = p.get("name")
    pid  = p.get("id")
    height = p.get("height")
    weight = p.get("weight")

    types = [t["type"]["name"] for t in p.get("types", [])]
    types.sort()
    type1 = types[0] if len(types) > 0 else None
    type2 = types[1] if len(types) > 1 else None

    stat_map = {s["stat"]["name"]: s["base_stat"] for s in p.get("stats", [])}
    return {
        "id": pid,
        "name": name,
        "height": height,
        "weight": weight,
        "type1": type1,
        "type2": type2,
        "hp":      stat_map.get("hp"),
        "attack":  stat_map.get("attack"),
        "defense": stat_map.get("defense"),
        "sp_atk":  stat_map.get("special-attack"),
        "sp_def":  stat_map.get("special-defense"),
        "speed":   stat_map.get("speed"),
    }
