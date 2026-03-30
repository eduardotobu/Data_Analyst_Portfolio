# Shared Data Directory

Large or frequently reused datasets that span multiple projects live here to avoid duplication.

## Structure

```
data/shared/
├── geo/        # Geographic boundaries, shapefiles, GeoJSON
├── climate/    # Weather and climate datasets
└── census/     # Census and demographic data
```

## Usage

Reference shared data from any project notebook using a relative path:

```python
import pandas as pd
from pathlib import Path

# From any project notebook:
SHARED_DATA = Path("../../data/shared")

geo_df = pd.read_csv(SHARED_DATA / "geo" / "us_states.csv")
```

## Guidelines

1. **Don't duplicate** — if a dataset is used by 2+ projects, move it here.
2. **Keep raw data immutable** — never modify files in place; save processed versions to your project's `data/processed/` folder.
3. **Document sources** — add a `SOURCES.md` in each subfolder noting where the data came from, the download date, and any license info.
4. **Use Git LFS for large files** — files over 50 MB should be tracked with [Git Large File Storage](https://git-lfs.github.com/).
