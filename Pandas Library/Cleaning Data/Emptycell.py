# 1- dropna() method.

import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
newResult = result.dropna()
print(newResult.dropna())

# 2- inplace 

import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
newResult = result.dropna(inplace= True)
print(newResult)
# Note: Due to inplace the output will be None.

# 3- fillna() method is use to insert 12 in place to None values in csv files.
import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
newResult = result.fillna(14, inplace= True)
print(newResult)

# 4- Here, result['Age'] indicates the Age column.

import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
newResult = result['Age'].fillna(140)
print(newResult.to_string())

# 5- mean() method.

import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
x = result["Age"].mean()
result['Age'].fillna(120, inplace= True)
print(result.to_string())

# 6- median() method.

import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
x = result['Age'].median()
result['Age'].fillna(340, inplace=True)
print(result.to_string())