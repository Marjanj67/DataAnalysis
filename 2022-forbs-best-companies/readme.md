# Best companies of 2022
## Dataset
link from kaggle


## The code 
### Importing libraries
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

```
### Main function
```

colors = sns.color_palette('flare',32)
def main():
    data = pd.read_csv('Forbes_2000_top_company_CLNQ11.csv')
    df = pd.DataFrame(data)
    CleanedData = data_cleaning(df)
    plot_bar(CleanedData)


```
### Data cleaning and formating
```
def data_cleaning(df):
    # Drop 31 to 200
    df = df.iloc[0:30,:]
    df['order'] = df.loc[:,'2022 Ranking']
    df.sort_values('2022 Ranking',inplace = True, ascending = False)
    df.at[0,'order'] = 'First'
    df.at[1,'order'] = 'Second'
    df.at[2,'order'] = 'Third'
    for iter in range(3,30):
        value = str(iter+1)+'th'
        df.at[iter,'order'] = value
    CleanedData = df
    return CleanedData

```
### ploting horizontal bar chart
```
def plot_bar(CleanedData):
    fig , ax = plt.subplots(figsize =(12,10) )
    CleanedData.sort_values('2022 Ranking',inplace = True, ascending = False)
    bars = ax.barh(CleanedData['order'],CleanedData['Revenue (Billions)'],color = colors)
    ax.set_title('30 top companies revenue')
    plt.bar_label(bars,fontsize = 7,fmt = '%d')
    ax.set_xlabel('Revenue (Billion dollar)')
    fig.savefig('barh.png')
    plt.show()



```
