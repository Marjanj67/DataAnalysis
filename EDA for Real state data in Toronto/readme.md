![](real-estate-business-compressor.jpg)
Data science has had a huge effect on realstate industry. In this project i will work with toronto realstate data from 2015 to 2021. This project focuses on data analysis and provides a step-by-step explanation.
# Data analysis for realstate data in toronto from 2015 to 2021
# Table of content 
1. [Project overview](#project-overview)
2. [EDA steps](#eda-steps)
3. [Data collection](#data-collection)
4. [Data cleaning](#data-cleaning)



## Project overview
### Project Summary from Kaggle:
[page link](https://www.kaggle.com/datasets/alankmwong/toronto-home-price-index)
#### Toronto Home Price Index
This Dataset contains in CSV format the monthly housing price information as published by the Toronto Regional Real Estate Board (TRREB) and Canadian Real Estate Association (CREA) as made public via their website and is based on the MLS Home Price Index.\
[https://trreb.ca/index.php/market-news/mls-home-price-index](https://trreb.ca/index.php/market-news/mls-home-price-index)
#### Content
Location - Neighbourhood in the Greater Toronto Area/
Comp - "Comp" stands for composite and takes into account the various types of housing into a single value.\
SFDetach - "SFDetach" stands for Single Family Detached Home, or commonly referred to as houses\
SFAttach - "SFAttach" stands for Single Family Attached Home\
THouse - "THouse" stands for Townhouses\
Apart - "Apart" is the abbreviation for Apartments or Condominuims\
All prices mentioned under "Benchmark" columns are depicted in Canadian Dollars\
All YoY Changes are in context of "Percentages"

## EDA steps

Data Collection
Data Cleaning
Univariate Analysis
Bivariate Analysis

r2 score for linear regression :0.577776808271866

## Data collection
In this part, i imported the data using pandas dataframe and then converted it to a Dateframe. The output shows that everything was imported correctly.
```
    data = pd.read_csv('MLS.csv')
    df = pd.DataFrame(data)
    df.head(5)
```
output:
```
            Location  CompIndex  ...  ApartYoYChange        Date
0  Adjala-Tosorontio      143.7  ...             NaN  2015-07-01
1  Adjala-Tosorontio      140.8  ...             NaN  2015-08-01
2  Adjala-Tosorontio      142.7  ...             NaN  2015-09-01
3  Adjala-Tosorontio      138.4  ...             NaN  2015-10-01
4  Adjala-Tosorontio      145.4  ...             NaN  2015-11-01

[5 rows x 17 columns]
```
## Data cleaning
In the data cleaning process i deleted the duplicates and null records, replaced some nulls and created a column named year. I decided to drop Date column and use the year and month for easier analysis.

```
    df.drop_duplicates(inplace=True)
    cols = df.columns.values
    # drop na based on 'CompIndex'
    if df['CompIndex'].isnull().sum() >0:
        df.dropna(subset=['CompIndex'],inplace=True)

    #check if all price columns are float
    for c in cols:
        if 'Location' not in str(c) and 'Date' not in str(c) :
            df[c].fillna(df[c].mean(),inplace=True)  # fill null with zeroes
            if df[c].dtype != 'float64':
                df[c].apply(pd.to_numeric)

    # check other nulls
    nulls = df.isnull().sum()
    if nulls.max() == 0:
        print('Bravoo, there are no nulls')

    #create a year coloumn
    df['Date'].apply(pd.to_datetime)
    df['year'] = pd.DatetimeIndex(df['Date']).year
    df['month'] = pd.DatetimeIndex(df['Date']).month
    # delete unwanted variables (Date)
    df.drop(columns='Date',inplace=True)
    # now we are ready for some analysis
```
After cleaning, this is what this dataset looks like:
```
# head
df.head(10)
```
![](headaftercleaning.png)
```
# describe
df.describe()
```
![](describeaftercleaning.png)



