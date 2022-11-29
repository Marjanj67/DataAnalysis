import pandas as pd
import numpy as np


# ----- Netflix data
data = pd.read_csv('netflix1.csv')
df = pd.DataFrame(data)


# Steps
# Set index
# Drop unnecessary columns
# Remove duplicates
# Join

# Set index
if df['show_id'].is_unique == True:
    df.set_index('show_id',inplace=True)

# Drop unnecessary columns
ToDrop = ['date_added','duration']
df.drop(columns=ToDrop,inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# All columns are without mistake and wrong data

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



#-------joining two dataset
# We want only values in the df that have an IMDB rating in df1
JoinesData = pd.merge(df,df1,how='left', on = ['title'])
JoinesData.dropna(inplace=True)

# Now we have a nice dataframe with 172 records.
JoinesData.to_csv('JoinedData.csv')

