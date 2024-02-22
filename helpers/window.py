def window_input_output(inp, out, data):
    df = data.copy()

    # Create input columns
    for i in range(1, inp):
        df[f'x_{i}'] = df.iloc[:, 0].shift(-i)

    # Create output columns
    for j in range(0, out):
        df[f'y_{j}'] = df.iloc[:, 0].shift(-out + j)

    # Drop rows with NaN values
    df = df.dropna(axis=0)

    return df
