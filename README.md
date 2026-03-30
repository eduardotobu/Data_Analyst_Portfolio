# Data Science & Analysis Portfolio

A collection of data science and data analysis projects demonstrating skills in exploratory data analysis, data cleaning, statistical analysis, visualization, machine learning, and SQL.

## Projects

| # | Project | Description | Tools |
|---|---------|-------------|-------|
| 1 | [Exploratory Data Analysis](projects/01-exploratory-data-analysis/) | Deep-dive EDA on a real-world dataset | Python, Pandas, Matplotlib |
| 2 | [Data Cleaning](projects/02-data-cleaning/) | Wrangling and cleaning messy data | Python, Pandas, NumPy |
| 3 | [Statistical Analysis](projects/03-statistical-analysis/) | Hypothesis testing and statistical modeling | Python, SciPy, Statsmodels |
| 4 | [Data Visualization](projects/04-data-visualization/) | Interactive and static visualizations | Python, Plotly, Seaborn |
| 5 | [Machine Learning](projects/05-machine-learning/) | Predictive modeling and classification | Python, Scikit-learn |
| 6 | [SQL Analysis](projects/06-sql-analysis/) | Database querying and analysis | SQL, SQLite, Python |
| 7 | [Dashboard](projects/07-dashboard/) | Interactive data dashboard | Python, Streamlit/Dash |

## Tools & Technologies

- **Languages:** Python, SQL
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn, SciPy, Statsmodels
- **Tools:** Jupyter Notebook, Git, VS Code, uv
- **Databases:** SQLite, PostgreSQL

## Shared Data

Large or reusable datasets (geographic boundaries, climate data, census, etc.) live in [`data/shared/`](data/shared/) to avoid duplication across projects. Each project references them via relative path:

```python
from pathlib import Path
SHARED_DATA = Path("../../data/shared")
df = pd.read_csv(SHARED_DATA / "geo" / "us_states.csv")
```

> Files over 50 MB are tracked with [Git LFS](https://git-lfs.github.com/). See `.gitattributes` for tracked patterns.

## Setup

```bash
# Install uv (if not already installed)
# Windows: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository (includes Git LFS files)
git lfs install
git clone https://github.com/YOUR_USERNAME/data-analyst-portfolio.git
cd data-analyst-portfolio

# Install dependencies (uv creates the virtual environment automatically)
uv sync
```

## Contact

- **LinkedIn:** [Your LinkedIn](https://linkedin.com/in/YOUR_USERNAME)
- **Email:** your.email@example.com
