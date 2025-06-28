# 1-

import pandas as pd
Person = {
    'Traits' : ['Color', 'Age', 'Height'],
    'Features' : ['Brown', 14, 5.5]
} 

res = pd.DataFrame(Person)
print(res)

# 2- locating rows.

import pandas as pd
Total = {
    'profits' : [1500, 1400, 1000],
    'losses' : [400, 250, 650]
}

final = pd.DataFrame(Total)
print(final.loc[1].to_string(index= False))

# 3- locating rows & column.


import pandas as pd
Total = {
    'profits' : [1500, 1400, 1000],
    'losses' : [400, 250, 650]
}

final = pd.DataFrame(Total)
print(final.loc[[1, 2]])

# 4- renaming indexs & locating them.


import pandas as pd
Total = {
    'profits' : [1500, 1400, 1000],
    'losses' : [400, 250, 650]
}

final = pd.DataFrame(Total, index= ['Day1', 'Day2', 'Day3'])
print(final.loc['Day2'])