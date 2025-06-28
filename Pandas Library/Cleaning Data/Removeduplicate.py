 # 1-

import pandas as pd
data = {
"brand": ["Yum Yum", "Yum Yum", "Indomie", "Indomie", "Indomie"],
"style": ["cup", "cup", "cup", "pack", "pack"],
"rating": [4, 4, 3.5, 15, 5]
}

data_frame = pd.DataFrame(data)
remove_duplicate = data_frame.duplicated()
print(remove_duplicate)

# 2-

 # 1-

import pandas as pd
data = {
"brand": ["Yum Yum", "Yum Yum", "Indomie", "Indomie", "Indomie"],
"style": ["cup", "cup", "cup", "pack", "pack"],
"rating": [4, 4, 3.5, 15, 5]
}

data_frame = pd.DataFrame(data)
remove_duplicate = data_frame.drop_duplicates()
print(remove_duplicate)