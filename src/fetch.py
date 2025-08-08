"""PokeAPI helpers"""
import requests, time

BASE = "https://pokeapi.co/api/v2"

def get_json(url, retries=3, timeout=10):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=timeout)
            if r.status_code == 200:
                return r.json()
            else:
                print(f"[WARN] {url} -> HTTP {r.status_code}")
        except requests.RequestException as e:
            print(f"[ERR] {e}")
        time.sleep(0.5 + i)
    return None

def list_pokemon(limit=151, offset=0):
    url = f"{BASE}/pokemon?limit={limit}&offset={offset}"
    data = get_json(url)
    if not data:
        return []
    return [p["name"] for p in data.get("results", [])]

def get_pokemon(name_or_id):
    return get_json(f"{BASE}/pokemon/{name_or_id}")
