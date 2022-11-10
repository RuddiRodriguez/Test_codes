# a class that implement CHAIN OF RESPONSIBILITY pattern in python to apply a list of filters to a dataframe with unknown column name"

import pandas as pd
import numpy as np
import os
import sys
import time
import datetime
import logging

class Filter:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next

    def apply(self, df):
        if self.next:
            return self.next.apply(df)
        return df
    
class Capitalize(Filter):
    def apply(self, df):
        return df.apply(lambda x: x.str.capitalize())
    
class Lowercase(Filter):
    def apply(self, df):
        return df.apply(lambda x: x.str.lower())
    
class Uppercase(Filter):
    def apply(self, df):
        return df.apply(lambda x: x.str.upper())
    
class Space(Filter):
    def apply(self, df):
        return df.apply(lambda x: x.str.replace(" ", ""))
    
    
class Reverse(Filter):
    def apply(self, df):
        return df.apply(lambda x: x[::-1])
    
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
    filter_chain.add_filter(Lowercase())
    filter_chain.add_filter(Space())
    filter_chain.add_filter(Reverse())
    filter_chain.add_filter(Capitalize())
    filter_chain.add_filter(Uppercase())
    
    df = pd.DataFrame({'col1': ['Hello world!']})
    print(filter_chain.apply(df))
                
                     
