
# implementation of Factory Method to read files in any format.

import abc

class Reader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

class TextReader(Reader):
    def read(self):
        print("Reading text file")

class BinaryReader(Reader):
    def read(self):
        print("Reading binary file")

class ReaderFactory:
    def get_reader(self, filename):
        if filename.endswith('.txt'):
            return TextReader()
        elif filename.endswith('.bin'):
            return BinaryReader()
        else:
            raise ValueError('Cannot read file format')

if __name__ == '__main__':
    reader_factory = ReaderFactory()
    reader = reader_factory.get_reader('data.bin')
    reader.read()
    

    # implementation of Factory Method to read files in any format wth pandas.

import pandas as pd

class Reader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

class TextReader(Reader):
    def read(self):
        print("Reading text file")

class BinaryReader(Reader):
    def read(self):
        print("Reading binary file")

class PandasReader(Reader):
    def read(self):
        print("Reading with pandas")

class ReaderFactory:
    def get_reader(self, filename):
        if filename.endswith('.txt'):
            return TextReader()
        elif filename.endswith('.bin'):
            return BinaryReader()
        elif filename.endswith('.csv'):
            return PandasReader()
        else:
            raise ValueError('Cannot read file format')

if __name__ == '__main__':
    reader_factory = ReaderFactory()
    reader = reader_factory.get_reader('data.csv')
    reader.read()
    

  
  