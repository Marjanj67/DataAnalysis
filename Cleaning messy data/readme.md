<p align="center">
  <img src="https://github.com/Marjanj67/DataAnalysis/blob/b87b24f79c46ed2fb9e0264953bbeae19293df33/Cleaning%20messy%20data/film1.jpg" />
</p>
# cleaning messy data and joining with another dataset

## Importing modules and first dataset
```
import pandas as pd
import numpy as np

# ----- Netflix data
data = pd.read_csv('netflix1.csv')
df = pd.DataFrame(data)

```



## Data cleaning
Steps:
* Set index
* Drop unnecessary columns
* Remove duplicates
```
# Set index
if df['show_id'].is_unique == True:
    df.set_index('show_id',inplace=True)

# Drop unnecessary columns
ToDrop = ['date_added','duration']
df.drop(columns=ToDrop,inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# All columns are without mistake and wrong data
```
## Importing second dataset
```
#------Imdb data
data1 = pd.read_csv('imdb_top_1000.csv')
df1 = pd.DataFrame(data1)
# Find the title of columns
ColumnsNames = df1.columns.values
# We only need 'Series_Title' and 'IMDB_Rating'
ColumnsNames = np.array(ColumnsNames)
ColumnsDelete = np.delete(ColumnsNames,[1,6])
df1.drop(columns = ColumnsDelete,inplace=True)
#Changing the name of the columns
df1.rename(columns={'Series_Title':'title'},inplace=True)
```

## Joining two dataset
```
#-------joining two dataset
# We want only values in the df that have an IMDB rating in df1
JoinesData = pd.merge(df,df1,how='left', on = ['title'])
JoinesData.dropna(inplace=True)

# Now we have a nice dataframe with 172 records.
JoinesData.to_csv('JoinedData.csv')
```

## view output
