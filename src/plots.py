"""Visualization utilities"""
import pandas as pd
import matplotlib.pyplot as plt

STATS = ["hp","attack","defense","sp_atk","sp_def","speed"]

def plot_stats_compare(csv_path, names):
    df = pd.read_csv(csv_path)
    wanted = [n.lower() for n in names]
    sub = df[df["name"].isin(wanted)]
    if sub.empty:
        print("[WARN] No matching names found in CSV.")
        return
    sub = sub.set_index("name")[STATS]
    sub.T.plot(kind="bar")
    plt.title("Base Stats Comparison")
    plt.xlabel("Stat")
    plt.ylabel("Value")
    plt.legend(title="Pokémon")
    plt.tight_layout()
    plt.show()

def plot_type_distribution(csv_path):
    df = pd.read_csv(csv_path)
    types = pd.melt(df, value_vars=["type1","type2"], value_name="type")["type"].dropna()
    counts = types.value_counts().sort_values(ascending=False)
    counts.plot(kind="bar")
    plt.title("Type Distribution")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_speed_vs_attack(csv_path):
    df = pd.read_csv(csv_path)
    if df.empty:
        print("[WARN] CSV is empty.")
        return
    df.plot(kind="scatter", x="speed", y="attack", alpha=0.7)
    plt.title("Speed vs Attack")
    plt.tight_layout()
    plt.show()
