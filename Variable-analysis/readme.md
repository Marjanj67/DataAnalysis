# Variable analysis
In this project, i explore the relationship between variables in a dataset.


## Data description
Data from kaggle\
https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021
### Context
The World Happiness Report is a landmark survey of the state of global happiness . The report continues to gain global recognition as governments, organizations and civil society increasingly use happiness indicators to inform their policy-making decisions. Leading experts across fields – economics, psychology, survey analysis, national statistics, health, public policy and more – describe how measurements of well-being can be used effectively to assess the progress of nations. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness.

### Content
The happiness scores and rankings use data from the Gallup World Poll . The columns following the happiness score estimate the extent to which each of six factors – economic production, social support, life expectancy, freedom, absence of corruption, and generosity – contribute to making life evaluations higher in each country than they are in Dystopia, a hypothetical country that has values equal to the world’s lowest national averages for each of the six factors. They have no impact on the total score reported for each country, but they do explain why some countries rank higher than others.





## The code

### importing libraries
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable
```

### The main function 
In the main function, after importing the data and creating a data frame, cleaning function is called.
Then cleaned data frame is saved in a CSV file. This data is then used in functions to find the relationship between variables.

```
def main ():
    data = pd.read_csv('world-happiness-report-2021.csv')
    df = pd.DataFrame(data)
    dfClean = clean_data(df)
    dfClean.to_csv('dfClean.csv') 
    plot_scatter(dfClean)
    correlation_matrix(dfClean)
    plot_heatmap(dfClean)

```

### Data preparing
This data has some Columns that are not useful and will be deleted in cleaning process.
After that I made sure there is no error or missing value using the described method.
```
colors = sns.color_palette('Set2',10)
def clean_data(df):
    ListVariables = df.columns.values
    Unwanted = ['Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                'Ladder score in Dystopia', 'Explained by: Log GDP per capita',
                'Explained by: Log GDP per capita',	'Explained by: Social support',	
                'Explained by: Healthy life expectancy','Explained by: Freedom to make life choices',
                'Explained by: Generosity',	'Explained by: Perceptions of corruption',	'Dystopia + residual']
    df.drop(columns = Unwanted,inplace = True)
    Describe = df.describe()  # Everything is in order
    Describe.to_csv('Describe.csv') 
    return df
```
### Mapping the data
First let's look at our data on a map to understand it better.\
I mapped the data using geopandas. 
```
def plot_map(dfClean):
    countries = gpd.read_file(
               gpd.datasets.get_path("naturalearth_lowres"))
    dfTemp = dfClean.loc[:,['Country name', 'Ladder score']]
    dfTemp = dfTemp.sort_values('Ladder score')

    # before merging name of some countries need to change
    us = dfTemp[dfTemp['Country name']=='United States'].index.values[0]
    dfTemp.at[us,'Country name'] = 'United States of America'
    dr = dfTemp[dfTemp['Country name']=='Dominican Republic'].index.values[0]
    dfTemp.at[dr,'Country name'] = 'Dominican Rep.'

    MergedData = pd.merge(countries,dfTemp, how = "outer",left_on='name',right_on='Country name')
    MergedData.loc[:,['Ladder score']] = MergedData.loc[:,['Ladder score']].fillna('2')
    MergedData['Ladder score'] = pd.to_numeric(MergedData['Ladder score'])
    fig, ax = plt.subplots(figsize=(8,6))
    divider = make_axes_locatable(ax)

    cax = divider.append_axes("right", size="5%", pad=0.1)
    MyMap = MergedData.plot(column = 'Ladder score' , cmap = 'Greens',ax = ax, legend=True, cax=cax)
    ax.set_title('Map of happiness')
    ax.text(-200,-130,'* Based on data from 2021')
    ax.text(-200,-145,'* Data for the white countries is not available')
    ax.text(-200,-160,'* Darker color means happier')
    MyMap.set_facecolor('#ADD8E6')
    fig.savefig('map.png')

```
### scatter plot
Drawing a scatter plot shows the relationship between variables. 
```
def plot_scatter(dfClean):
    fig , ax = plt.subplots(2,3)
    ax[0,0].scatter(dfClean['Ladder score'],dfClean['Logged GDP per capita'],c = colors[0])
    ax[0,0].set_title('Logged GDP per capita effect')
    # ax[0,0].set_xlabel('Ladder score')
    ax[0,0].set_ylabel('Logged GDP per capita')

    ax[0,1].scatter(dfClean['Ladder score'],dfClean['Social support'],c = colors[1])
    ax[0,1].set_title('Social support effect')
    # ax[0,1].set_xlabel('Ladder score')
    ax[0,1].set_ylabel('Social support')

    ax[0,2].scatter(dfClean['Ladder score'],dfClean['Healthy life expectancy'],c = colors[2])
    ax[0,2].set_title('Healthy life expectancy effect')
    # ax[0,2].set_xlabel('Ladder score')
    ax[0,2].set_ylabel('Healthy life expectancy')

    ax[1,0].scatter(dfClean['Ladder score'],dfClean['Freedom to make life choices'],c = colors[3])
    ax[1,0].set_title('Freedom to make life choices effect')
    ax[1,0].set_xlabel('Ladder score')
    ax[1,0].set_ylabel('Freedom to make life choices')

    ax[1,1].scatter(dfClean['Ladder score'],dfClean['Generosity'],c = colors[4])
    ax[1,1].set_title('Generosity effect')
    ax[1,1].set_xlabel('Ladder score')
    ax[1,1].set_ylabel('Generosity')

    ax[1,2].scatter(dfClean['Ladder score'],dfClean['Perceptions of corruption'],c = colors[5])
    ax[1,2].set_title('Perceptions of corruption effect')
    ax[1,2].set_xlabel('Ladder score')
    ax[1,2].set_ylabel('Perceptions of corruption')
    fig.set_size_inches(15,10)
    fig.savefig('scatter.png')
```
This scatter plot has 6 subplots and shows relationship between 6 variables and the main variables.
As shown in this plots 4 variables have positive correlation, one variables has negative correlation and for generosity no obvious pattern is seen.

### Create correlation matrix
Correlation matrix helps us understand the strength of relationship between variables.\
This matrix shows the same result as the scatter plot. In the first column we see positive correlation for first four variables (more than 0.5) and negative correlation for last variables. Correlation between ladder score and generosity is almost zero that shows no obvious correlation.
```
def correlation_matrix(dfClean):
    CorrelationMatrix = dfClean.corr(method='pearson',numeric_only = True)
    CorrelationMatrix.to_csv('CorrelationMatrix.csv')
```
### Covariance matrix and heat map
This matrix result shows relationship between variables.
```
def plot_heatmap(dfClean):
    CovMatrix = dfClean.cov(numeric_only = True)
    # CovMatrix.to_csv('CovMatrix.csv')
    fig , ax = plt.subplots()
    ax.imshow(CovMatrix)
    Variables = CovMatrix.columns.values
    ax.set_title('Heatmap for variabes',fontsize = 18 ,pad=18)
    ax.set_xticks(ticks = range(0,len(Variables)),labels = Variables,rotation = 45,ha = 'right')
    ax.set_yticks(ticks = range(0,len(Variables)),labels = Variables)
    fig.set_size_inches(12,10)
    for i in range(len(Variables)):
        for j in range(len(Variables)):
            ax.text(i-.1,j,np.around(CovMatrix.iloc[i,j],decimals = 1))
    fig.savefig('heatmap.png')
```
## The end
This little analysis was to show the relationship between variables. Covariance matrix is usually used in machine learning algorithms. there is no further analysis for now.
