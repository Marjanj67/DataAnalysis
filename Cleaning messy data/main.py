import pandas as pd


data = pd.read_csv('netflix1.csv')
df = pd.DataFrame(data)

columns = df.columns.values


# steps
# set index
# remove duplicates
# remove mistakes

# set index
if df['show_id'].is_unique == True:
    df.set_index('show_id',inplace=True)

# remove duplicates
df.drop_duplicates(inplace=True)

# remove mistakes

# # col1--------------
# # all show_id start with s and follows by a number so any value that doesn't is a mistake
# correct = df['show_id'].str.startswith('s')
# correct = pd.DataFrame(correct)
# des1 = correct.describe()  # the result shows that everything is in order in this column

# # col2-----------
# des2 = df['type'].describe()  
# values = pd.unique(df['type'])
# # result : array(['Movie', 'TV Show'], dtype=object) --> there is no mistake

# col2-----------
des3 = df['title'].describe() #this code shows that there are duplicates and missformated data
# df['title'] = 
df['title'].astype('string')


# this codes gives error which means there are mistakes in this column


print(des3)

