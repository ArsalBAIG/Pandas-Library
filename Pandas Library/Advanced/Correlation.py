import pandas as pd
data = {
"Duration": [50, 40, 45],
"Pulse": [109, 117, 110],
"Calories": [409.1, 479.5, 340.8]
}

data_frame = pd.DataFrame(data)
print(data_frame.corr())