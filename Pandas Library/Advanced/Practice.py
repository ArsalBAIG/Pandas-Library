import sys
import pandas as pd
import matplotlib.pyplot as plt
result = pd.read_csv(r"C:\Users\ok\OneDrive\Documents\PANDAS LIBRARY\Advanced\Demo File.csv")
result.plot(kind='pie', x='Name', y='Age')
plt.show()
plt.savefig(sys.stdout.buffer) # This ensures that data is stored in Buffer instead of file.
sys.stdout.flush()# This ensures the data is removed when send completely.