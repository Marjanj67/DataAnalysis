import pandas as pd
import numpy as np


# ----- netflix data
data = pd.read_csv('netflix1.csv')
df = pd.DataFrame(data)


# steps
# set index
# drop unnecessary columns
# remove duplicates
# join tables


# set index
if df['show_id'].is_unique == True:
    df.set_index('show_id',inplace=True)

# drop unnecessary columns
toDrop = ['date_added','duration']
df.drop(columns=toDrop,inplace=True)

# remove duplicates
df.drop_duplicates(inplace=True)

# all columns are without mistake and wrong data

#------Imdb data
data1 = pd.read_csv('imdb_top_1000.csv')
df1 = pd.DataFrame(data1)
# find the title of columns
cols = df1.columns.values
# we only need 'Series_Title' and 'IMDB_Rating'
cols = np.array(cols)
delCol = np.delete(cols,[1,6])
df1.drop(columns = delCol,inplace=True)
#changing the name of the columns
df1.rename(columns={'Series_Title':'title'},inplace=True)



#-------joining two dataset (left outer join)
# we want only values in the df that have an IMDB rating in df1
jo = pd.merge(df,df1,how='left', on = ['title'])
jo.dropna(inplace=True)

# now we have a nice dataframe with 172 records.


