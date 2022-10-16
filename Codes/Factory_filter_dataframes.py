# Factory method classes to filter a dataframe by a given type and value.

import pandas as pd

class Filter:
    def filter(self, df):
        raise NotImplementedError

class FilterByType(Filter):
    def __init__(self, type):
        self.type = type

    def filter(self, df):
        return df[df['type'] == self.type]

class FilterByValue(Filter):

    def __init__(self, value):
        self.value = value

    def filter(self, df):
        return df[df['value'] == self.value]

class FilterByTypeAndValue(Filter):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def filter(self, df):
        return df[(df['type'] == self.type) & (df['value'] == self.value)]

class FilterFactory:

    def __init__(self, df):
        self.df = df
# client 
    def serialize(self, type=None, value=None):
        serializer = self.get_filter(type,value)
        return serializer.filter(self.df)    
# creator
    def get_filter(self, type=None,value=None):
        if type and value:
            return FilterByTypeAndValue(type, value)
        elif type:
            return FilterByType(type)
        elif value:
            return FilterByValue(value)
        else:
            return Filter()

if __name__ == '__main__':
    df = pd.DataFrame({'type': ['A', 'A', 'B', 'B', 'C', 'C'],
                       'value': [1, 2, 3, 4, 5, 6]})
    factory = FilterFactory(df)
    print(factory.get_filter().filter(df))
    #print(factory.serialize(type='A'))
    #print(factory.get_filter(value=3).filter(df))
    print(factory.get_filter(type='B', value=4).filter(df))


# checking waht value was passed to argument in a function.

def foo(*args):
    print(args)
    

   