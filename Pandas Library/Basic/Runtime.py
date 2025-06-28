
import pandas as pd
Total = {
    'profits' : [1500, 1400, 1000],
    'losses' : [400, 250, 650]
}

final = pd.DataFrame(Total, index= ['Day1', 'Day2', 'Day3'])
print(final.loc['Day2'])