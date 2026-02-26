import pandas as pd

def configure_pandas_display():
    """Sets consistent pandas display options for the project."""
    # Show all columns (don't hide them with '...')
    pd.set_option('display.max_columns', 100)
    
    # Show a reasonable number of rows
    pd.set_option('display.max_rows', 100)
    
    # Don't truncate long strings in columns (great for text data or URLs)
    pd.set_option('display.max_colwidth', None)
    
    # Format floats to 2 decimal places to avoid scientific notation
    pd.set_option('display.float_format', lambda x: f'{x:,.2f}')
    
    print("Pandas display options configured!")