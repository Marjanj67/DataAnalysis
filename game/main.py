import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn  as sns


color1 = sns.color_palette('Set2',10)[0]
color2 = sns.color_palette('Set2',10)[1]
# reading data source
data = pd.read_csv('hotel_bookings.csv')
df = pd.DataFrame(data)


CahrtType = ''
def main():
    if CahrtType == 'Bar':
        # ----- bar chart -----------marketSegment ---------------------
        marketSegment = df.groupby(['market_segment'],as_index=False).count()
        fig , ax = plt.subplots(1,1)
        bars = ax.bar(marketSegment['market_segment'],marketSegment['hotel'] ,color = color1)
        plt.xticks(rotation = 45)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_title('Market segment')
        ax.set_xlabel('type of reservation')
        ax.set_ylabel('count')
        ax.tick_params(length = 0)
        ax.bar_label(bars)
    elif CahrtType == 'Box':
    # ----------boxplot--------------------- distribution channel
        sns.boxplot(df['distribution_channel'],df['adr'],palette="Set3",showmeans = True, meanprops={"marker":"o",
                    "markerfacecolor":"white", 
                    "markeredgecolor":"black",
                    "markersize":"10"})
        plt.xlabel('distribution channel')
        plt.ylabel('price per night')
        plt.title('price affected by distribution channel')
        sns.despine(right=True,top=True)
        # ----boxplot----------------------- distribution channel ----------- cleaned
        df.replace(df['adr'].max(),df['adr'].mean(),inplace=True)
        sns.boxplot(df['distribution_channel'],df['adr'],palette="Set3",showmeans = True, meanprops={"marker":"o",
                    "markerfacecolor":"white", 
                    "markeredgecolor":"black",
                    "markersize":"10"})
        plt.xlabel('distribution channel')
        plt.ylabel('price per night')
        plt.title('price affected by distribution channel')
        sns.despine(right=True,top=True)
    elif CahrtType == 'Scatter':
        #----- scatter chart
        pd.options.mode.chained_assignment = None
        df.replace(df['adr'].max(),df['adr'].mean(),inplace=True)
        rooms = df['reserved_room_type']
        roomsU = rooms.drop_duplicates()
        colors = {}
        i = 1
        for r in roomsU:
            colorTemp = sns.color_palette('Set3',11)[i]
            colorTemp = mpl.colors.to_hex(colorTemp)
            colors[r] = colorTemp
            i += 1


        df.replace({'reserved_room_type':colors},inplace=True)

        # fig , ax = plt.subplots(1,1)
        scatter = plt.scatter(df['lead_time'],df['adr'],c = df['reserved_room_type'])
        plt.spines['top'].set_visible(False)
        plt.spines['right'].set_visible(False)
        plt.set_title('effect of the lead  time on price per room')
        plt.set_xlabel('lead time')
        plt.set_ylabel('price')
        plt.tick_params(length = 0)

        plt.legend(handles=scatter.legend_elements(), labels=colors.keys())
    elif CahrtType == 'Pie':
    # --------------------pie chart --------------type of meal-------------
        ml = df.groupby(by = 'meal',as_index=False).count()
        ml = ml.loc[:,['meal','hotel']]
        plt.pie(ml['hotel'],labels=ml['meal'],autopct='%0.f%%',shadow=True,explode=[0,0,0,0.5,0],startangle=-130)
        plt.title('type of meal')
        plt.text(0.7,-1.2,
                "Type of meal booked. :\nUndefined/SC :no meal package\nBB : Bed & Breakfast\nHB : Half board ,breakfast and one other meal\nFB : Full board",verticalalignment='bottom', horizontalalignment='left',
                color='green', fontsize=8)
    elif CahrtType == 'Area':
    # ----------------------- area chart
        df.replace(df['adr'].max(),df['adr'].mean(),inplace=True)

        df['monthYear'] = df['arrival_date_year'].astype(str) +'-'+df['arrival_date_month']
        years = df.groupby(by = df['monthYear'] ,as_index=False).sum()
        av = df.groupby(by = df['monthYear'],as_index=0).sum()
        avr = av['adr'].mean()
        plt.fill_between(years['monthYear'],years['adr'],y2 = avr,color = color1)


        plt.xticks(rotation = 45)
        plt.grid(axis='x')
        plt.text(25.5,470000,'average line',color = color1,fontsize = 15)
    plt.show()



if __name__ == "__main__":
  main();
