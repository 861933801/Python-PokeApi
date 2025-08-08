"""
analyze.py — Build a DataFrame and save CSV (Student TODO version)
"""
from pathlib import Path
import pandas as pd
from .fetch import list_pokemon, get_pokemon
from .transform import extract_row

def build_dataset(limit=151, offset=0, verbose=True):
    """
    TODO:
      - Call list_pokemon(...) to get names
      - Loop names and fetch each JSON with get_pokemon(name)
      - Transform each JSON via extract_row and collect into rows
      - Build a DataFrame from rows
      - Sort by 'id' and drop duplicates
      - Print progress every ~25 items if verbose
    """
    # TODO: implement
    raise NotImplementedError("Implement build_dataset()")

def save_csv(df, path="data/pokedex.csv"):
    """
    Save CSV and ensure parent folder exists.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return str(path)
