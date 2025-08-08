"""
plots.py — Visualization utilities (Student TODO version)
"""
import pandas as pd
import matplotlib.pyplot as plt

STATS = ["hp","attack","defense","sp_atk","sp_def","speed"]

def plot_stats_compare(csv_path, names):
    """
    TODO:
      - Read CSV into df
      - Filter rows where name is in provided names (lowercase)
      - Set index to 'name', select STATS columns, and transpose
      - Plot a bar chart with titles/labels/legend
    """
    # TODO: implement
    raise NotImplementedError("Implement plot_stats_compare()")

def plot_type_distribution(csv_path):
    """
    TODO:
      - Read CSV
      - Melt type1/type2 into a single 'type' column and drop NaNs
      - Value counts -> bar chart with labels/title
    """
    # TODO: implement
    raise NotImplementedError("Implement plot_type_distribution()")

def plot_speed_vs_attack(csv_path):
    """
    TODO:
      - Read CSV
      - Scatter plot: x='speed', y='attack', alpha ~ 0.7
      - Add a title; call tight_layout
    """
    # TODO: implement
    raise NotImplementedError("Implement plot_speed_vs_attack()")

# --------- Stretch (optional) ----------
# def plot_speed_vs_attack_by_type(csv_path):
#     """
#     TODO (stretch): group by type1, plot each group with its own marker/label on same axes.
#     """
#     raise NotImplementedError
#
# def plot_radar_for_one(csv_path, name):
#     """
#     TODO (stretch): radar chart for a single Pokémon across STATS
#     """
#     raise NotImplementedError
