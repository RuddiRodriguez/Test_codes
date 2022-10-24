# a class that implement CHAIN OF RESPONSIBILITY pattern in python to apply a list of filters to a dataframe including rename columns.

import pandas as pd
import numpy as np
import re
import os
import sys

class Filter:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next

    def apply(self, df):
        if self.next:
            return self.next.apply(df)
        return df
    
class Rename(Filter):
    def __init__(self,old,new):
        super().__init__()
        self.old = old
        self.new = new
    def apply(self, df):
        df = df.rename(columns={self.old:self.new})
        return super().apply(df)
    
class Drop(Filter):
    def __init__(self,columns):
        super().__init__()
        self.columns = columns
    def apply(self, df):
        df = df.drop(self.columns,axis=1)
        return super().apply(df)
    
class Replace(Filter):
    def __init__(self,old,new):
        super().__init__()
        self.old = old
        self.new = new
    def apply(self, df):
        df = df.replace(self.old,self.new)
        return super().apply(df)
    
class FilterChain:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def apply(self, df):
        for filter in self.filters:
            df = filter.apply(df)
        return df
    
if __name__ == "__main__":
    filter_chain = FilterChain()
    filter_chain.add_filter(Rename('a','A'))
    filter_chain.add_filter(Drop(['b']))
    filter_chain.add_filter(Replace('C','c'))
    df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'C':[7,8,9]})
    print(filter_chain.apply(df))
    