# 1-

import pandas as pd
data = {
    'Country' : ['UK', 'USA', 'CAD', 'AMR', 'DUB'],
    'Temp' : ['30.0', '23.9', '55.4', '12.9', '4.4']
}

result = pd.DataFrame(data)
result['Temp'] = result['Temp'].astype(float)
newTemp = result['Temp'].mean()
print(newTemp)

# 2-

import pandas as pd
mixed = pd.DataFrame({'date': ['2022-12-01', '01/02/2022', '2022-03-23', '03/02/2022', '3 4 2023', '2023.9.30']})
mixed['date'] = pd.to_datetime(mixed['date'], format= 'mixed', dayfirst=True)
print(mixed)