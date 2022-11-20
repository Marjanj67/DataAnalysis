import pandas as pd
import matplotlib.pyplot as plt



def main():
    data = pd.read_csv('MLS.csv')
    df = pd.DataFrame(data)
    #-------- cleaning the data
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


    # delete unwanted variables
    
    # now we are ready for some analysis


    print(df.head())





main()
