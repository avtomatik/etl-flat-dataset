from pandas import DataFrame


def preprocess(df: DataFrame) -> DataFrame:
    df.insert(1, 'desc', df.columns[1])
    df.columns = ('period', 'desc', 'value')
    return df.set_index(df.columns[0])
