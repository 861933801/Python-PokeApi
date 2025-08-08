"""
fetch.py — PokeAPI helpers (Student TODO version)
"""
import time
import requests

BASE = "https://pokeapi.co/api/v2"

def get_json(url, retries=3, timeout=10):
    """
    Return parsed JSON from a URL with simple retry/backoff.
    TODOs:
      - Implement the request with requests.get
      - Handle non-200 status codes
      - Handle exceptions (RequestException)
      - Add a simple backoff (sleep)
    """
    # TODO: implement
    # Hints:
    #   try:
    #       r = requests.get(url, timeout=timeout)
    #       if r.status_code == 200: return r.json()
    #       else: print a warning
    #   except requests.RequestException as e:
    #       print an error
    #   time.sleep(...) between retries
    raise NotImplementedError("Implement get_json()")

def list_pokemon(limit=151, offset=0):
    """
    Return a list of Pokémon names using the /pokemon endpoint.
    Example: GET {BASE}/pokemon?limit=151&offset=0
    TODO:
      - Call get_json on the correct URL
      - Extract the 'name' values from data['results']
    """
    # TODO: implement
    raise NotImplementedError("Implement list_pokemon()")

def get_pokemon(name_or_id):
    """
    Return the JSON for a single Pokémon (by lowercase name or id).
    TODO:
      - Call get_json on f"{BASE}/pokemon/{name_or_id}"
    """
    # TODO: implement
    raise NotImplementedError("Implement get_pokemon()")

# --------- Stretch (optional) ----------
# def list_pokemon_by_generation(gen_id: int) -> list[str]:
#     """
#     Use /generation/{id} to get species, then resolve to Pokémon.
#     TODO (stretch): implement generation-based listing.
#     """
#     raise NotImplementedError
#
# def get_json_cached(url: str, cache_path: str) -> dict:
#     """
#     TODO (stretch): if cache_path exists, read and return JSON from disk.
#     Otherwise fetch, then save JSON to cache_path.
#     """
#     raise NotImplementedError
