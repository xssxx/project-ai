import pandas as pd

def window_input_output(inp: int, out: int, data: pd.DataFrame) -> pd.DataFrame:
    df = data.copy()

    # Create input columns
    i = 1
    while i < inp:
        df[f'x_{i}'] = df.iloc[:, 0].shift(i)
        i += 1

    # Create output columns
    j = 0
    while j < out:
        df[f'y_{j}'] = df.iloc[:, 0].shift(out+j)
        j += 1

    # Drop rows with NaN values
    df = df.dropna(axis=0)

    return df
