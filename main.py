import pandas as pd
import fsspec
from fsspec.implementations.local import LocalFileSystem
fs = LocalFileSystem()
df = pd.read_csv('iris.csv')

with fs.open('iris_fsspec.csv', 'w') as f:
    df.to_csv(f)

df.to_csv('iris_classic_pandas.csv')
