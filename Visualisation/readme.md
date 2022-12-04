# visualisation practice with python
```
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import seaborn  as sns



ColorSelect = sns.color_palette('Set3',10)

def plot_market_segment(df):
    MarketSegment = df.groupby(['market_segment'],as_index=False).count()
    fig , ax = plt.subplots(1,1)
    Bars = ax.bar(MarketSegment['market_segment'],MarketSegment['hotel'] ,color = ColorSelect[0])
    plt.xticks(rotation = 45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title('Market segments' , fontsize = 20)
    ax.set_xlabel('Type of reservation', fontsize = 14)
    ax.set_ylabel('Count', fontsize = 14)
    ax.tick_params(length = 0)
    ax.bar_label(Bars)
    fig.set_size_inches(14,12)
    fig.savefig('bar.png')
    ax.cla()


def plot_distribution_channel(df):
    plt.figure(figsize=(14,12))
    sns.boxplot(df['distribution_channel'],df['adr'],palette="Set3",showmeans = True, meanprops={"marker":"o",
                    "markerfacecolor":"white", 
                    "markeredgecolor":"black",
                    "markersize":"10"})
    plt.xlabel('Distribution channel', fontsize = 14)
    plt.ylabel('Price per night', fontsize = 14)
    plt.title('Price affected by distribution channel' , fontsize = 20)
    sns.despine(right=True,top=True)
    plt.savefig('boxplot.png')
    plt.cla()

def plot_time_price(df):
    pd.options.mode.chained_assignment = None
    Rooms = df['reserved_room_type']
    RoomsUnique = Rooms.drop_duplicates()
    ColorsMap = {}
    i = 1
    for r in RoomsUnique:
        ColorTemp = sns.color_palette('Set3',11)[i]
        ColorTemp = mpl.colors.to_hex(ColorTemp)
        ColorsMap[r] = ColorTemp
        i += 1


    df.replace({'reserved_room_type':ColorsMap},inplace=True)
    plt.figure(figsize=(14,12))
    Iter = 0
    for ColorTemp in ColorsMap.values():
        Room = list(ColorsMap.keys())[Iter]
        dfTemp = df[(df['reserved_room_type']== ColorTemp)]
        plt.scatter(dfTemp['lead_time'],dfTemp['adr'],c = ColorTemp,label=Room)
        Iter += 1
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.title('Effect of the lead  time on price per room', fontsize = 20)
    plt.xlabel('Lead time', fontsize = 14)
    plt.ylabel('Price', fontsize = 14)
    plt.tick_params(length = 0)

    plt.legend()
    plt.savefig('scatter.png')
    plt.cla()

def plot_meal(df):
    MealsData = df.groupby(by = 'meal',as_index=False).count()
    MealsData = MealsData.loc[:,['meal','hotel']]
    plt.figure(figsize=(14,12))
    plt.pie(MealsData['hotel'],labels= MealsData['meal'],autopct='%0.f%%',shadow=True,explode=[0,0,0,0.5,0],startangle=-130,colors=ColorSelect, textprops={'fontsize': 14})
    plt.title('Type of meal', fontsize=20)
    plt.text(0.7,-1.2,
            "Type of meal booked. :\nUndefined/SC :no meal package\nBB : Bed & Breakfast\nHB : Half board \nFB : Full board",verticalalignment='bottom', horizontalalignment='left',
            color='#000000', fontsize=15)
    
    plt.savefig('pie.png')
    plt.cla()

def plot_month_profit(df):
    df['monthYear'] = df['arrival_date_year'].astype(str) +'-'+df['arrival_date_month']
    YearsData = df.groupby(by = df['monthYear'] ,as_index=False).sum()
    MeansMonth = df.groupby(by = df['monthYear'],as_index=0).sum()
    MeanTotal = MeansMonth['adr'].mean()
    plt.figure(figsize=(14,12))
    plt.fill_between(YearsData['monthYear'],YearsData['adr'],y2 = MeanTotal,color = ColorSelect[0])
    plt.xticks(rotation = 90)
    plt.title('Profit by months',fontsize = 20,pad=30)
    plt.grid(axis='x')
    plt.text(25.5,470000,'Average line',color = ColorSelect[3],fontsize = 17)
    plt.savefig('area.png')
    plt.cla()


def cleaning_data(df):
    df.replace(df['adr'].max(),df['adr'].mean(),inplace=True)
    return df


def main():
    global df
    data = pd.read_csv('hotel_bookings.csv')
    df = pd.DataFrame(data)
    cleaning_data(df)
    plot_market_segment(df)         # Bar chart
    plot_distribution_channel(df)   # Boxplot
    plot_time_price(df)             # Scatter chart
    plot_meal(df)                   # Pie chart
    plot_month_profit(df)           # Area chart
 
 



if __name__ == "__main__":
  main();
  
  ```
