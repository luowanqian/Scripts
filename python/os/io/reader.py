import pandas as pd
import json
from pandas.io.json import json_normalize
from abc import ABC, abstractclassmethod


class Reader(ABC):
    @abstractclassmethod
    def read(file_path: str, **kargs):
        pass


class ExcelReader(Reader):
    def read(file_path: str, **kargs):
        return pd.read_excel(file_path, **kargs)


class CSVReader(Reader):
    def read(file_path: str, **kargs):
        return pd.read_csv(file_path, **kargs)


class JSONReader(Reader):
    def read(file_path: str, **kargs):
        with open(file_path) as f:
            data = json.load(f)

        return json_normalize(data, **kargs)


def factory_method(file_type: str = 'excel'):
    file_type = file_type.lower()

    reader = None
    if file_type == 'excel':
        reader = ExcelReader()
    elif file_type == 'csv':
        reader = CSVReader()
    elif file_type == 'json':
        reader = JSONReader()

    return reader


if __name__ == "__main__":
    pass
