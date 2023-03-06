from numba import njit
import numpy as np
import pandas as pd


def initialize_df():
    
    global countries, years, N_countries, N_years
    # imports and cleans the dataframe of alliances and conflicts
    
    df = pd.read_csv('allies_and_enemies_1816_2014_iso.csv')
    df = df[(df['alliance'] != 0) | (df['conflict']!=0)]   #filter entries with no link
    df['weight'] = df['alliance']+df['conflict']+df['alliance']*df['conflict']
    df = df.drop(columns = ['alliance','conflict'])
    
    countries = np.unique(np.concatenate((np.array(df['statea']),np.array(df['stateb']))))
    years = np.unique(df['year'])
    N_countries = len(countries)
    N_years = len(years)
    
    return df
    



def find_alliances(df):
    
    # finds a list of alliances
        
    countries = np.unique(np.concatenate((np.array(df['statea']),np.array(df['stateb']))))
    years = np.unique(df['year'])
    N_countries = len(countries)
    N_years = len(years)

    alliances = np.zeros((N_countries,N_countries,N_years), bool)

    for idx_year, year in enumerate(years):

        df_pos = df[(df['year'] == year) & (df['weight'] == 1)]

        for _, country_a, country_b, _ in df_pos.values:

            idx_a = np.where(countries == country_a)[0][0]
            idx_b = np.where(countries == country_b)[0][0]

            alliances[idx_a, idx_b, idx_year] = True
            alliances[idx_b, idx_a, idx_year] = True

    
    return alliances

        

def find_conflicts(df):
    
    # finds a list of conflicts
        

    conflicts = np.zeros((N_countries,N_countries,N_years), bool)

    for idx_year, year in enumerate(years):

        df_neg = df[(df['year'] == year) & (df['weight'] == -1)]

        for _, country_a, country_b, _ in df_neg.values:

            idx_a = np.where(countries == country_a)[0][0]
            idx_b = np.where(countries == country_b)[0][0]

            conflicts[idx_a, idx_b, idx_year] = True
            conflicts[idx_b, idx_a, idx_year] = True

     
    return conflicts
                    
                    
      
                    
@njit
def find_duration(array):
    
    # finds the duration of each link in the input array
    
    duration = []

    for idx_a in range(N_countries):
        for idx_b in range(idx_a, N_countries):
            
            counter = 0
            for idx_year in range(N_years):


                if array[idx_a,idx_b,idx_year] == True:  # add one per year the alliance is present

                    counter += 1

                else:  

                    if counter != 0:  
                        duration.append(counter)  # add the alliance length to the array

                    counter = 0  #reset counter
                    
                #if counter == 100:
                #    print(idx_a, idx_b)

            if counter != 0: duration.append(counter)  # append the current alliances
                
    return duration
                    
                    

                    
@njit
def find_neutrality(alliance, conflict):
    
    duration = []
    

    for idx_a in range(N_countries):
        for idx_b in range(idx_a, N_countries):

            counter = 0
            have_interacted = False
            for idx_year in range(N_years):
                
                # we only take into account neutrality after countries have interacted at leat once
                
                # check if the two countries have ever interacted
                if alliance[idx_a,idx_b,idx_year] == True  or  conflict[idx_a,idx_b,idx_year] == True:
                    have_interacted = True
                    
                # don't do anything if the countries have not interacted
                if have_interacted == False:
                    continue
                    
                if alliance[idx_a,idx_b,idx_year] == False  and  conflict[idx_a,idx_b,idx_year] == False:  # add one per year nothing is present

                    counter += 1

                else:  

                    if counter != 0: 
                        duration.append(counter)  # add the alliance length to the array

                    counter = 0  #reset counter

                
    return duration


    
                    
def find_alliance_duration():
           
    df = initialize_df()
    alliances = find_alliances(df)
    alliance_duration = find_duration(alliances)
    return alliance_duration               
         
                    
                    
def find_conflict_duration():
           
    df = initialize_df()
    conflicts = find_conflicts(df)
    conflict_duration = find_duration(conflicts)
    return conflict_duration                     

                    
                    
def find_neutrality_duration():
           
    df = initialize_df()
    alliances = find_alliances(df)
    conflicts = find_alliances(df)
    neutrality_duration = find_neutrality(alliances, conflicts)
    return neutrality_duration
                    