from abc import ABC, abstractmethod
from pandas import read_csv, read_excel


class Strategy:

    def read_file(self, path: str, file_type: str) -> object:
        pass


# ConcreteStrategy
class CsvStrategy(Strategy):
    def read_file(self, path: str, file_type: str) -> object:
        return read_csv(path)


# ConcreteStrategy
class ExcelStrategy(Strategy):
    def read_file(self, path):
        return read_excel(path)


# Context

class File:
    def __init__(self):
        self.strategy = object

    def execute(self, path: str, file_type: str) -> object:
        if not isinstance(self.strategy, Strategy):
            return None
        return self.strategy.read_file(path)

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    reader = File()
    path = '/Users/ruddirodriguez/Documents/ML/test_dvc/Data/Vendor_Data.csv'
    df = reader.execute('%s' % path)
    # result1 is 0

    reader.set_strategy(CsvStrategy())
    result2 = reader.execute('%s' % path)
    # result2 is 8

    reader.set_strategy(ExcelStrategy())
    result3 = reader.execute(5, 3)
    # result3 is 2

    print(result1)
    print(result2)
    print(result3)
