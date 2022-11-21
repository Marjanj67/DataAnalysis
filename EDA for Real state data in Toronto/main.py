import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

color1 = sns.color_palette('rocket_r',71)
color2 = sns.color_palette('rocket',10)
color3 = sns.color_palette('bright',10)

def DataClean(df):
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
    # delete unwanted variables (Date)
    df.drop(columns='Date',inplace=True)
    # now we are ready for some analysis
    return df


def main():
    global df
    # data = pd.read_csv('MLS.csv')
    # df = pd.DataFrame(data)
    #-------- cleaning the data
    # DataClean(df)
    # pd.DataFrame.to_csv(df,'cleanedData.csv')

    # load cleaned data
    data = pd.read_csv('cleanedData.csv')
    df = pd.DataFrame(data)

    # --------------------Univariate Analysis-------------------
    # thre are no useful Univariate Analysis for this data

    # --------------------Bivariate Analysis---------------------
    # # ------------ barh start --------
    # plotyear = '2021'
    # plotyear = pd.to_numeric(plotyear)
    # df_temp = df.where(df['year']==plotyear).dropna()
    # df_temp = df_temp.groupby(by = 'Location',as_index=False).mean()
    # df_temp.sort_values('CompBenchmark', inplace=True,ascending=True)

    # fig , ax = plt.subplots(1)
    # bars = ax.barh(df_temp['Location'],df_temp['CompBenchmark'] ,color = color1)
    # ax.set_title('avarage price for each neighbourhood in ' + str(plotyear ),fontsize = 50)
    # plt.yticks(fontsize = 35)
    # plt.bar_label(bars,fontsize = 35,fmt = '%d')
    # fig.set_size_inches(50,70)
    # fig.savefig('fig1.png')
    # # ------------ barh end --------
    neg = 'Ajax'
    df_temp = df.where(df['Location']==neg).dropna()
    df_temp = df_temp.groupby(by = 'year',as_index=False).mean()
    df_temp.sort_values('year', inplace=True,ascending=False)

    # without regresion ---------------
    # fig , ax = plt.subplots(1)
    # ax.plot(df_temp['year'],df_temp['CompBenchmark'] ,color = color2[5])
    # ax.set_title('price change in ' + neg + ' over the years')
    # fig.savefig('line1.png')
    
    # with regresion -------------------
    NormalDict = {}
    ind = 0
    for y in df_temp['year'].unique():
        NormalDict[y] = ind
        ind += 1


    X = df_temp['year'].map(NormalDict).values.reshape(-1, 1)
    y = df_temp['CompBenchmark'].values.reshape(-1, 1)
    reg = LinearRegression()
    reg.fit(X,y)
    new_x = np.array([7])
    new_x = new_x.reshape(-1,1)
    new_y =reg.predict(new_x)


    fig , ax = plt.subplots(1)
    df_temp = pd.concat(df_temp,pd.DataFrame(new_x,new_y))
    ax.plot(df_temp['year'],df_temp['CompBenchmark'] ,color = color2[2])
    ax.set_title('price change in ' + neg + ' over the years')
    # ax.plot(new_x,new_Y,c=color3[0])
    fig.savefig('line1.png')

    plt.show()
    # print(df.head())





main()
