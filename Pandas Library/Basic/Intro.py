# 1- 

import pandas
myData = {
    'cars' : ["Audi", "BMW"],
    'capacity' : [5 , 8]
}

result = pandas.DataFrame(myData)
print(result)

# 2-

import pandas 
person = {
    'Traits' : ['Name', 'Age', 'Color'],
    'Features' : ['Arsal', 19, 'Brown']
}

x = pandas.DataFrame(person)
print(x)