import pandas as pd

data = {
  "calories": ['arroz', 380, 390],
  "duration": [50, 40, 45],
  "calories2": [420, 380, 390],
  "duration2": [50, 40, 45]
}


#load data into a DataFrame object:
df = pd.DataFrame(data)
df.info()
print(df) 

df.to_excel("output.xlsx") 

