# 1-

import pandas as pd
read_file = pd.read_csv(r"C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Demo File.csv")
print(read_file.head())

# 2-

import pandas as pd
read_files = pd.read_csv(r"C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Demo File.csv")
print(read_files.tail())

# 3-

import pandas as pd
read_files = pd.read_csv(r"C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Demo File.csv")
print(read_files.info())
