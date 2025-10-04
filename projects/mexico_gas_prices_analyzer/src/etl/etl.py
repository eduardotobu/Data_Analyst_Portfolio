import os
import glob
import logging
from pathlib import Path
from datetime import date
from typing import List

import pandas as pd
from lxml import etree

# Configuration
PLACES_PATH = Path('data/places.xml')
PRICES_PATH = Path('data/prices.xml')
HISTORICAL_PATH = Path('data/raw/gas_historical_prices.csv.gz')
OUTPUT_PATH = Path('data/processed/mexico_gas_prices.csv.gz')
RAW_DAILY_PATTERN = 'data/raw/gas_prices*.csv.gz'

# Gas type mapping
GAS_TYPE_MAPPING = {
    'Regular': 'regular',
    'Premium': 'premium',
    'Diésel': 'diesel',
    'Diésel Automotríz': 'diesel',
    'Diésel de Ultra Bajo Azufre (DUBA)': 'diesel',
    'Diésel Agrícola/Marino': 'diesel',
    'Diésel Industrial': 'diesel'
}

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def extract_places_xml(filepath: Path) -> pd.DataFrame:
    """Extract place data from XML file."""
    logger.info(f"Extracting places from {filepath}")
    
    tree = etree.parse(str(filepath))
    root = tree.getroot()
    
    data = [
        {
            "place_id": place.get('place_id'),
            "name": place.findtext('name'),
            "cre_id": place.findtext('cre_id'),
            "longitude": float(place.find('location/x').text),
            "latitude": float(place.find('location/y').text)
        }
        for place in root.findall('place')
    ]   
    return pd.DataFrame(data)


def extract_prices_xml(filepath: Path) -> pd.DataFrame:
    """Extract price data from XML file."""
    logger.info(f"Extracting prices from {filepath}")
    
    tree = etree.parse(str(filepath))
    root = tree.getroot()
    
    data = [
        {
            "place_id": place.get('place_id'),
            "gas_type": gas.get('type'),
            "price": float(gas.text)
        }
        for place in root.findall('place')
        for gas in place.findall('gas_price')
    ]
    
    return pd.DataFrame(data)

def save_daily_snapshot(df_places: pd.DataFrame, df_prices: pd.DataFrame, output_dir: str = 'data/raw') -> None:
    """Merge and save today's gas prices snapshot."""
    logger.info("Creating daily snapshot")
    
    df_snapshot = df_places.merge(df_prices, how='left', on='place_id')
    df_snapshot['date'] = date.today()
    
    # Create directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    output_file = Path(output_dir) / f'gas_prices_{date.today().strftime("%Y%m%d")}.csv.gz'
    df_snapshot.to_csv(output_file, index=False, compression='gzip')
    
    logger.info(f"Daily snapshot saved to {output_file}")

def load_and_clean_historical(filepath: Path) -> pd.DataFrame:
    """Load and clean historical gas prices data."""
    logger.info(f"Loading historical data from {filepath}")
    
    df = pd.read_csv(filepath, encoding='latin-1', compression='gzip')
    
    # Rename columns
    df = df.rename(columns={
        'NumeroPermiso': 'cre_id',
        'SubProducto': 'gas_type'
    })
    
    # Standardize gas types
    df['gas_type'] = df['gas_type'].replace(GAS_TYPE_MAPPING)
    
    # Reshape from wide to long format
    df = df.melt(
        id_vars=['cre_id', 'gas_type'],
        var_name='date',
        value_name='price'
    )
    
    # Parse dates
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    
    return df[['cre_id', 'gas_type', 'price', 'date']]


def merge_places_and_historical(
    df_places: pd.DataFrame,
    df_historical: pd.DataFrame
) -> pd.DataFrame:
    """Merge places with historical prices and report merge statistics."""
    logger.info("Merging places with historical data")
    
    df_merged = df_places.merge(
        df_historical,
        how='outer',
        on='cre_id',
        indicator=True
    )
    
    # Report merge statistics
    merge_stats = df_merged['_merge'].value_counts()
    total = len(df_merged)
    
    both = merge_stats.get('both', 0)
    left_only = merge_stats.get('left_only', 0)
    right_only = merge_stats.get('right_only', 0)
    
    logger.info(f"Merge statistics:")
    logger.info(f"  Both datasets: {both:,} ({both/total*100:.2f}%)")
    logger.info(f"  Left only: {left_only:,} ({left_only/total*100:.2f}%)")
    logger.info(f"  Right only: {right_only:,} ({right_only/total*100:.2f}%)")
    
    # Keep only matched records
    df_merged = df_merged[df_merged['_merge'] == 'both'].drop(columns=['_merge'])
    
    return df_merged


def load_daily_snapshots(pattern: str) -> List[pd.DataFrame]:
    """Load all daily snapshot files."""
    files = glob.glob(pattern)
    logger.info(f"Found {len(files)} daily snapshot files")
    
    return [pd.read_csv(f, compression='gzip') for f in files]


def combine_all_data(
    df_historical: pd.DataFrame,
    daily_snapshots: List[pd.DataFrame]
) -> pd.DataFrame:
    """Combine historical data with all daily snapshots."""
    logger.info("Combining all datasets")
    
    all_dfs = daily_snapshots + [df_historical]
    df_combined = pd.concat(all_dfs, ignore_index=True)

    df_combined['date'] = pd.to_datetime(df_combined['date'], format='ISO8601').dt.date
    
    logger.info(f"Combined dataset contains {len(df_combined):,} rows")
    
    return df_combined


def main():
    """Main ETL pipeline."""
    logger.info("=== Starting ETL Pipeline ===")
    
    # EXTRACT
    logger.info("EXTRACT phase")
    df_places = extract_places_xml(PLACES_PATH)
    df_prices = extract_prices_xml(PRICES_PATH)
    
    # Save daily snapshot
    save_daily_snapshot(df_places, df_prices)
    
    # Load historical data
    df_historical = load_and_clean_historical(HISTORICAL_PATH)
    
    # TRANSFORM
    logger.info("TRANSFORM phase")
    df_historical = merge_places_and_historical(df_places, df_historical)
    
    # Load and combine all daily snapshots
    daily_snapshots = load_daily_snapshots(RAW_DAILY_PATTERN)
    df_final = combine_all_data(df_historical, daily_snapshots)
    
    # LOAD
    logger.info("LOAD phase")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_final.to_csv(OUTPUT_PATH, index=False, compression='gzip')
    
    logger.info(f"✓ ETL Complete! Output saved to: {OUTPUT_PATH}")
    logger.info(f"✓ Final dataset: {len(df_final):,} rows")


if __name__ == "__main__":
    main()