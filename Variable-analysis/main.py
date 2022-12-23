import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


colors = sns.color_palette('Set2',10)
def clean_data(df):
    ListVariables = df.columns.values
    Unwanted = ['Standard error of ladder score', 'upperwhisker', 'lowerwhisker',
                'Ladder score in Dystopia', 'Explained by: Log GDP per capita',
                'Explained by: Log GDP per capita',	'Explained by: Social support',	
                'Explained by: Healthy life expectancy','Explained by: Freedom to make life choices',
                'Explained by: Generosity',	'Explained by: Perceptions of corruption',	'Dystopia + residual']
    df.drop(columns = Unwanted,inplace = True)
    print(df.head(5))
    Describe = df.describe()  # Everything is in order
    Describe.to_csv('Describe.csv') 
    return df

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
    # plt.show()

def correlation_matrix(dfClean):
    CorrelationMatrix = dfClean.corr(method='pearson')
    CorrelationMatrix.to_csv('CorrelationMatrix.csv')

def plot_heatmap(dfClean):
    CovMatrix = dfClean.cov()
    # CovMatrix.to_csv('CovMatrix.csv')
    fig , ax = plt.subplots()
    ax.imshow(CovMatrix)
    Variables = CovMatrix.columns.values
    ax.set_xticks(ticks = range(0,len(Variables)),labels = Variables,rotation = 45)
    ax.set_yticks(ticks = range(0,len(Variables)),labels = Variables)
    fig.set_size_inches(10,10)
    fig.savefig('heatmap.png')
    # plt.show()
    
def main ():
    data = pd.read_csv('world-happiness-report-2021.csv')
    df = pd.DataFrame(data)
    dfClean = clean_data(df)
    # dfClean.to_csv('dfClean.csv') 
    # plot_scatter(dfClean)
    correlation_matrix(dfClean)
    plot_heatmap(dfClean)



main ()
