# implementation of Factory Method to save files in any format.

import abc

class FileSaver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, data):
        pass

class TextFileSaver(FileSaver):
    def save(self, data):
        print('Saving text file')

class BinaryFileSaver(FileSaver):
    def save(self, data):
        print('Saving binary file')

class FileSaverFactory:

    @staticmethod
    def get_saver(type):
        if type == 'text':
            return TextFileSaver()
        elif type == 'binary':
            return BinaryFileSaver()
        else:
            raise ValueError(type)

if __name__ == '__main__':


    text_saver = FileSaverFactory.get_saver('text')
    text_saver.save('some data')

    binary_saver = FileSaverFactory.get_saver('binary')
    binary_saver.save(b'\x00\x01')

    # this will raise ValueError
    FileSaverFactory.get_saver('unknown')



    # class  to save a file with a button in streamlit.

    import streamlit as st
    import pandas as pd


    def save_file(df, file_name, file_type):
        if file_type == 'csv':
            df.to_csv(file_name, index=False)
        elif file_type == 'xlsx':
            df.to_excel(file_name, index=False)
        elif file_type == 'json':
            df.to_json(file_name, orient='records', lines=True)
        else:
            raise ValueError(file_type)

    def save_file_button(df, file_name, file_type):
        if st.button('Save File'):
            save_file(df, file_name, file_type)
            st.success('File saved!')

    if __name__ == '__main__':
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        save_file_button(df, 'test.csv', 'csv')
        save_file_button(df, 'test.xlsx', 'xlsx')
        save_file_button(df, 'test.json', 'json')

        # this will raise ValueError
        save_file_button(df, 'test.txt', 'txt')



 # filter a dataframe with by date with a slider in streamlit.

    import streamlit as st
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)

    st.write('### Filter by date')

    min_date = st.slider('Min date', value=df.index.min())
    max_date = st.slider('Max date', value=df.index.max())

    st.write('### Number of points:', len(df[(df.index >= min_date) & (df.index <= max_date)]))

    st.map(df[(df.index >= min_date) & (df.index <= max_date)])

    # filter a dataframe with by date with a slider in streamlit.



    # implementation of Factory Method to convert column dataframe to datetime.

    import abc
    import pandas as pd

    class ColumnConverter(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def convert(self, column):
            pass


    class DatetimeColumnConverter(ColumnConverter):
        def convert(self, column):
            return pd.to_datetime(column).dt.date

    class StringColumnConverter(ColumnConverter):
        def convert(self, column):
            return column.astype(str)

    class ColumnConverterFactory:
            
            @staticmethod
            def get_converter(type):
                if type == 'datetime':
                    return DatetimeColumnConverter()
                elif type == 'string':
                    return StringColumnConverter()
                else:
                    raise ValueError(type)

    if __name__ == '__main__':

        df = pd.DataFrame({'col1': ['2020-01-01', '2020-01-02', '2020-01-03']})
        df['col1'] = ColumnConverterFactory.get_converter('datetime').convert(df['col1'])
        print(df.dtypes)

        df = pd.DataFrame({'col1': [1, 2, 3]})
        df['col1'] = ColumnConverterFactory.get_converter('string').convert(df['col1'])
        print(df.dtypes)

        # this will raise ValueError
        ColumnConverterFactory.get_converter('unknown')


        

# implementation of scikit learn like pipeline with factory method.

import abc
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer

class PipelineFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self):
        pass
    
        
class StandardScalerPipeline(PipelineFactory):
    def create(self):
        return Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('std_scaler', StandardScaler()),
        ])

class MinMaxScalerPipeline(PipelineFactory):
        
        def create(self):
            return Pipeline([
                ('imputer', SimpleImputer(strategy='median')),
                ('min_max_scaler', MinMaxScaler()),
            ])

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def fit(self, X, y=None):
        for step in self.steps:
            step.fit(X, y)

    def transform(self, X):
        for step in self.steps:
            X = step.transform(X)
        return X

    def fit_transform(self, X, y=None):
        for step in self.steps:
            X = step.fit_transform(X, y)
        return X

class PipelineBuilder:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)
        return self

    def build(self):
        return Pipeline(self.steps)

if __name__ == '__main__':



    pipeline = PipelineBuilder()\
        .add_step(StandardScalerPipeline().create())\
        .add_step(MinMaxScalerPipeline().create())\
        .build()

    print(pipeline)

    # implementation of scikit learn like pipeline with factory method.



    # implementation of scikit learn like pipeline with factory method.

    import abc
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.impute import SimpleImputer

    class PipelineFactory(metaclass=abc.ABCMeta