import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_data(PopulationNumber):
    # create dataset
    Id = np.arange(PopulationNumber)
    EyeColors = ['black','brown','blue','green']
    Eye = np.random.choice(EyeColors,PopulationNumber)
    Age = np.random.randint(80,size = PopulationNumber)
    Happy = np.random.choice(['yes','no'],PopulationNumber)
    data = {'Id':Id,'Eye color':Eye,'Age':Age,'Happy':Happy}
    population = pd.DataFrame(data)
    return population

def simple_random_sampling(population,PopulationNumber,SampleNumber):
    #------probability methods
    ## ----- simple random sampling
    Id = np.arange(PopulationNumber)
    
    IdSample = np.random.choice(Id,SampleNumber,replace=False)   # Select random ids
    Sample = population.iloc[IdSample]
    return Sample


def stratified_sampling(population,PopulationNumber,SampleNumber):
    Factor = 'Eye'
    ClusterNumber = len(population['Eye color'].unique())
    Ids = []
    for iter in range(ClusterNumber):
        EyeColor = population['Eye color'].unique()[iter]
        Group = population[population['Eye color']==EyeColor]
        Id = np.arange(len(Group))
        IdSample = np.random.choice(Id,int(SampleNumber/ClusterNumber),replace=False)
        Ids = Ids + IdSample.tolist()
    Sample = population.iloc[Ids]
    return Sample
    
def cluster_sampling(population,PopulationNumber):
    Factor = 'Eye'
    ClusterNumber = len(population['Eye color'].unique())
    SampleCluster = np.random.randint(ClusterNumber,size = 1)
    for iter in range(ClusterNumber):
        if iter == SampleCluster:
            EyeColor = population['Eye color'].unique()[iter]
            Sample = population[population['Eye color']==EyeColor]
    return Sample

def systematic_random_sampling(population,PopulationNumber,SampleNumber,Interval):
    Upper = PopulationNumber-(SampleNumber*Interval)
    First = np.random.randint(0,Upper,size = 1)
    IdSample = []
    for iter in range(SampleNumber):
        IdSample.append(First[0])
        First += Interval
    Sample = population.iloc[IdSample]
    return Sample




def plotting(population,Sample,Type):
    # ploting
    fig , ax = plt.subplots(1,2)
    fig.suptitle(Type + ' sampling')
    ax[0].hist(population['Age'])
    ax[0].set_title('Population')
    ax[1].hist(Sample['Age'])
    ax[1].set_title('Sample')
    plt.show()

def main():
    PopulationNumber = 500
    SampleNumber = int(PopulationNumber/5)
    population = create_data(PopulationNumber)
    Type = 'cluster'
    if Type == 'simple':
        Sample = simple_random_sampling(population,PopulationNumber,SampleNumber)
    elif Type == 'systematic':
        Interval = int(PopulationNumber/120)
        Sample = systematic_random_sampling(population,PopulationNumber,SampleNumber,Interval)
    elif Type == 'startified':
        Sample = stratified_sampling(population,PopulationNumber,SampleNumber)
    elif Type == 'cluster':
        Sample = cluster_sampling(population,PopulationNumber)
    plotting(population,Sample,Type)

main()