# 1-

import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
result.loc[7, 'Age'] = 55 # Here, we assign 55 at line 7 of 'Age' column.
print(result)

# 2- checking conditions:

import pandas as pd
result = pd.read_csv(r'C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Cleaning Data\Demo File.csv')
# Here, index show the index of each row in result dataframe.
for index, row in result.iterrows():
    if row['Age'] > 40:
        result.loc[index, 'Age'] = 100

print(result.to_string())
