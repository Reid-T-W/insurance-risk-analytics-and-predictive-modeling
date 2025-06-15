def count_empty_or_null(df):
    return df.apply(lambda col: col.isnull().sum() + col.astype(str).str.strip().eq('').sum())

def percent_null_and_empty_string(df):
    total_rows = len(df)
    return df.apply(lambda col: ((col.isnull().sum() + col.astype(str).str.strip().eq('').sum()) / total_rows) * 100)