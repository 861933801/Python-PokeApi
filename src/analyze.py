"""Build a DataFrame and save CSV"""
import pandas as pd
from .fetch import list_pokemon, get_pokemon
from .transform import extract_row

def build_dataset(limit=151, offset=0, verbose=True):
    names = list_pokemon(limit=limit, offset=offset)
    rows = []
    for i, name in enumerate(names, 1):
        p = get_pokemon(name)
        if p:
            rows.append(extract_row(p))
            if verbose and i % 25 == 0:
                print(f"[INFO] Fetched {i}/{len(names)}")
    df = pd.DataFrame(rows)
    df = df.sort_values("id").drop_duplicates(subset=["id"])
    return df

def save_csv(df, path="data/pokedex.csv"):
    df.to_csv(path, index=False)
    return path
