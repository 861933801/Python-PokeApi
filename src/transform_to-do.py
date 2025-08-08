"""
transform.py — Transform raw PokeAPI JSON → tidy rows (Student TODO version)
"""

def extract_row(p):
    """
    Flatten a /pokemon payload p into a single dict row.

    Desired schema:
        id, name, height, weight,
        type1, type2,
        hp, attack, defense, sp_atk, sp_def, speed

    TODO:
      - Pull name/id/height/weight from p
      - Build a sorted list of type names from p["types"]
      - Map p["stats"] (list) into a dict keyed by stat name -> base_stat
    """
    # TODO: implement extraction
    # Hints:
    #   types = [t["type"]["name"] for t in p.get("types", [])]
    #   types.sort()
    #   stat_map = {s["stat"]["name"]: s["base_stat"] for s in p.get("stats", [])}
    raise NotImplementedError("Implement extract_row()")
