import numpy as np
import pandas as pd
import networkx as nx
import scipy.linalg as la
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)



def initialize_df():
    
    # import and clean the dataframe with alliances and conflicts
    
    df = pd.read_csv('../CoW_data/allies_and_enemies_1816_2014_COW.csv')

    df = df[(df['alliance'] != 0) | (df['conflict']!=0)]   #filter entries with no link
    
    df['weight'] = df['alliance']+df['conflict']+df['alliance']*df['conflict']   # merge alliances and conflicts in a single column
    df = df.drop(columns = ['alliance','conflict'])
    
    return df





def create_network(df, year, giant_component = True):
    
    # returns a Graph object corresponding to the international relations network of the given year
    # edges have a weighted attribute which can be 1 or -1
    
    df2 = df[df['year']==year]   # select one particular year    
    G = nx.from_pandas_edgelist(df2, source ='statea', target = 'stateb', edge_attr='weight')
    
    # take only the giant component
    if giant_component:
        GC = max(nx.connected_components(G), key=len)
        G = G.subgraph(GC)

    return G




def local_balance(G, country):   
    
    ### find local balance index for a given node and a given network
    
    idx = np.where(np.array(G.nodes()) == country)[0][0]    
    
    # calculate signed communicability
    A = nx.adjacency_matrix(G).todense()
    A0 = np.abs(A)
    
    Comm = la.expm(A)
    Comm0 = la.expm(A0)
    
    # calculate balance
    Ki = np.diag(Comm)/np.diag(Comm0)       # node balance
    
    return Ki[idx]




def local_balance_timeseries(country, year_range = [1816,2014]):
    
    # finds the local balance for several years and creates a balance time series for a specific country
    
    years_v = np.arange(year_range[0],year_range[1]+1)
    Kloc = np.ones(len(years_v))

    if country in ['VAN', 'KIR', 'TUV', 'NAU', 'MSI', 'FSM', 'ZAN']:  # isolated countries. Balance is equal to one
        return years_v, Kloc

    else:
        df = initialize_df()
        for i, year in enumerate(years_v):

            G = create_network(df, year)

            if country not in G.nodes():
                Kloc[i] = None

            else:
                Kloc[i] = local_balance(G, country)

        return years_v, Kloc





def get_Kloc_timeseries():
    
    # computes the local balance time series for each country and saves it in a csv file

    # import data
    df = initialize_df()

    # get list of countries and years
    years = df['year'].unique()
    countries = np.loadtxt('data/countries.txt', dtype = str)   # we want to use always the same order of countries

    # compute balance time series for each country
    K_loc = pd.DataFrame(index = years, columns = countries)
    for country in countries:
        print(country)
        _, K_loc[country] = local_balance_timeseries(country)

    # save the df to avoid computing this again
    K_loc.to_csv('data/K_loc_timeseries.csv')





if __name__ == '__main__':

    get_Kloc_timeseries()