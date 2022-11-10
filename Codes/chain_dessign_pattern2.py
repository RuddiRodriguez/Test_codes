# a class that implement CHAIN OF RESPONSIBILITY pattern in python to apply a list of filters to a dataframe including rename columns, drop columns, drop rows, fill missing values, and convert data types."


import pandas as pd
import numpy as np
import os
import sys
import datetime
import time
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
    
class RenameColumns(Filter):
        
        def __init__(self, dict_of_columns):
            self.dict_of_columns = dict_of_columns
            super().__init__()
            
        def apply(self, df):
            df = df.rename(columns=self.dict_of_columns)
            return super().apply(df)
        
class DropColumns(Filter):
            
            def __init__(self, columns):
                self.columns = columns
                super().__init__()
                
            def apply(self, df):
                df = df.drop(columns=self.columns)
                return super().apply(df)
            
class DropRows(Filter):
                    
                    def __init__(self, rows):
                        self.rows = rows
                        super().__init__()
                        
                    def apply(self, df):
                        df = df.drop(index=self.rows)
                        return super().apply(df)
                    
                    
class FillMissingValues(Filter):
                            
                            def __init__(self, dict_of_columns):
                                self.dict_of_columns = dict_of_columns
                                super().__init__()
                                
                            def apply(self, df):
                                df = df.fillna(self.dict_of_columns)
                                return super().apply(df)
                            
class ConvertDataTypes(Filter):
    
        
        def __init__(self, dict_of_columns):
            self.dict_of_columns = dict_of_columns
            super().__init__()
            
        def apply(self, df):
            df = df.astype(self.dict_of_columns)
            return super().apply(df)
        
        
class ChainOfResponsibility:
        
        def __init__(self, *filters):
            self.filters = filters
            self._setup_chain()
            
        def _setup_chain(self):
            for i in range(len(self.filters) - 1):
                self.filters[i].set_next(self.filters[i + 1])
                
        def apply(self, df):
            return self.filters[0].apply(df)
        
        
if __name__ == '__main__':
    
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    print(df)
    
    dict_of_columns = {'a': 'A', 'b': 'B', 'c': 'C'}
    columns = ['A', 'B']
    rows = [0, 1]
    dict_of_columns_fill = {'A': 0, 'B': 0, 'C': 0}
    dict_of_columns_convert = {'A': 'int64', 'B': 'int64', 'C': 'int64'}
    
    rename_columns = RenameColumns(dict_of_columns)
    drop_columns = DropColumns(columns)
    drop_rows = DropRows(rows)
    fill_missing_values = FillMissingValues(dict_of_columns_fill)
    convert_data_types = ConvertDataTypes(dict_of_columns_convert)
    
    chain = ChainOfResponsibility(rename_columns, drop_columns, drop_rows, fill_missing_values, convert_data_types)
    
    df = chain.apply(df)
    
    