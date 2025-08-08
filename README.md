# Pokémon Stats Explorer (API → CSV → Plots)

A classroom-ready starter project that teaches:
- Calling a public API (PokeAPI)
- Cleaning and saving data to CSV with pandas
- Visualizing with matplotlib
- Organizing a multi-file Python project
- (Optional) CLI, caching, and stretch tasks

## Quick Start

1) Create & activate a virtual environment (recommended)
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Fetch data (first 151 Pokémon) and save CSV
```bash
python -m src.main fetch --limit 151
```

4) Make a comparison plot of base stats
```bash
python -m src.main plot-compare --names pikachu charizard blastoise
```

5) See type distribution
```bash
python -m src.main plot-types
```

6) Scatter plot (Speed vs Attack)
```bash
python -m src.main plot-scatter
```

> All generated data is saved in `data/`. Plots open in a window by default.
