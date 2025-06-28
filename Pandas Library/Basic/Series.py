# 1-

import pandas as pd
x = [4,5,6]
result = pd.Series(x)
print(result)

# 2- for list.

import pandas as pd
myList = [5, 9, 8]
output = pd.Series(myList, index= ['x', 'y', 'z'])
print(output)

# 3- for dict.

import pandas as pd
myDict = {
    "Name" : "Ahmed", 
    "Age" : 19,
    "Color" : "Brown"
}
# Note: Here, we add to_string to remove dtype in the output.
final = pd.Series(myDict)
print(final.to_string(index= False))