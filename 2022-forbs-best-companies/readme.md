# Best companies of 2022
## Dataset
link from kaggle
https://www.kaggle.com/datasets/rakkesharv/forbes-2000-global-companies

### Forbes 2000 Global Companies
#### About Dataset
This is a webscrapped dataset containing Top 2000 Companies which are ranked by by using four metrics which are their sales, profits, assets, and market value. It has the 11 columns of data and they are:

2022 Ranking : Organization's Current Year Ranking

Organization Name : Name of the Organization

Industry : The industry type the Organization mainly deals with.

Country : Country of Origin

Year Founded : Year in which the Organization Founded

CEO : CEO of the Organization

Revenue (Billions) : Revenue made in the current year

Profits (Billions) : Profits made in the current year

Assets (Billions) : Assets made in the current year

Market Value (Billions) : Market Value as in current year

Total Employees : Total Number of working employees

## The code 
### Importing libraries
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

```
### Main function
Cleaning data and plotting
```

colors = sns.color_palette('flare',32)
def main():
    data = pd.read_csv('Forbes_2000_top_company_CLNQ11.csv')
    df = pd.DataFrame(data)
    CleanedData = data_cleaning(df)
    plot_bar(CleanedData)


```
### Data cleaning and formating
The dataset contains top 2000 companies and we only want the firdt 30.
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
In this chart I plot top 30 companies with their revenue to show that revenue alone is not a factor for being a top company.
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
<p align="center">
  <img src="https://github.com/Marjanj67/DataAnalysis/blob/3e672a1d60a0767b166609072d97d0466b29c8a7/2022-forbs-best-companies/barhfinal.png" />
</p>

