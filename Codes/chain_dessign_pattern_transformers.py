import pandas as pd


class Transformer:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next

    def apply(self, df):
        if self.next:
            return self.next.apply(df)
        return df


class Rename(Transformer):
    def __init__(self, col_dict):
        self.col_dict = col_dict

    def apply(self, df):
        df.rename(columns=self.col_dict, inplace=True)
        return df  # df.rename(columns=self.col_dict,inplace=True)


class CleanColumnName(Transformer):
    def apply(self, df):
        df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
        return df


class ToDateTime(Transformer):
    def __init__(self, col):
        super().__init__()
        self.col = col

    def apply(self, df):
        df[self.col] = pd.to_datetime(df[self.col])
        return df


class FilterData(Transformer):
    def __init__(self, col, value):
        self.col = col
        self.value = value

    def apply(self, df):
        df.drop(df[df[self.col] == self.value].index, inplace=True)
        return df


class DropDuplicates(Transformer):
    def __init__(self, col):
        self.col = col

    def apply(self, df):
        df.drop_duplicates(subset=self.col, inplace=True)
        return df


class TransformerChain:
    def __init__(self):
        self.transformers = []

    def add_transformer(self, transformer):
        self.transformers.append(transformer)

    def apply(self, df):
        for transformer in self.transformers:
            df = transformer.apply(df)
        return df


if __name__ == '__main__':
    df = pd.DataFrame({'a a': [2, 2, 3], 'b-h': [4, 5, 6], 'c': [7, 8, 9]})
    print(df)

    dict_of_columns = {'c': 'D'}
    transformer_chain = TransformerChain()
    transformer_chain.add_transformer(Rename(dict_of_columns))
    transformer_chain.add_transformer(CleanColumnName())
    # transformer_chain.add_transformer(ToDateTime('a_a'))
    transformer_chain.add_transformer(FilterData('D', 10))
    transformer_chain.add_transformer(DropDuplicates('a_a'))
    transformer_chain.apply(df)
    print(df)
