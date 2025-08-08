"""Simple CLI wrapper"""
import argparse
from .analyze import build_dataset, save_csv
from .plots import plot_stats_compare, plot_type_distribution, plot_speed_vs_attack

def cli():
    p = argparse.ArgumentParser(description="Pokémon Stats Explorer")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_fetch = sub.add_parser("fetch", help="Fetch Pokémon data and save CSV")
    p_fetch.add_argument("--limit", type=int, default=151)
    p_fetch.add_argument("--offset", type=int, default=0)
    p_fetch.add_argument("--out", default="data/pokedex.csv")

    p_cmp = sub.add_parser("plot-compare", help="Compare base stats for selected Pokémon")
    p_cmp.add_argument("--csv", default="data/pokedex.csv")
    p_cmp.add_argument("--names", nargs="+", required=True)

    p_types = sub.add_parser("plot-types", help="Type distribution bar chart")
    p_types.add_argument("--csv", default="data/pokedex.csv")

    p_sc = sub.add_parser("plot-scatter", help="Speed vs Attack scatter")
    p_sc.add_argument("--csv", default="data/pokedex.csv")

    return p.parse_args()

def main():
    args = cli()
    if args.cmd == "fetch":
        df = build_dataset(limit=args.limit, offset=args.offset)
        path = save_csv(df, args.out)
        print(f"[OK] Saved {len(df)} rows to {path}")
    elif args.cmd == "plot-compare":
        plot_stats_compare(args.csv, args.names)
    elif args.cmd == "plot-types":
        plot_type_distribution(args.csv)
    elif args.cmd == "plot-scatter":
        plot_speed_vs_attack(args.csv)

if __name__ == "__main__":
    main()
