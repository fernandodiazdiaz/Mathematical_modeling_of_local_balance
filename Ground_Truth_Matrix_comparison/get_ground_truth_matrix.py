
import numpy as np
import pandas as pd
import re
from odf import text, teletype
from odf.opendocument import load
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)






# Load files
doc = load("../list_historical_events/list_historical_events.odt")
COW_df = pd.read_csv('../CoW_data/allies_and_enemies_1816_2014_COW.csv')

# initialize DataFrame
years = np.arange(1816,2015)
countries = np.loadtxt('data/countries.txt', dtype = str)
Ground_Truth = pd.DataFrame(0,index = years, columns = countries)


for counter, element in enumerate(doc.getElementsByType(text.P)):

    text_content = teletype.extractText(element)

    if text_content == '' or re.match(r'^-+$',text_content) is not None : #skip empty lines and separator lines ('--------')
        continue

    elif text_content.startswith('YEAR'):  # find the year of each block
        
        current_year = int(text_content.split(':')[1].strip())

        if current_year != 1816: countries_previous_year = countries_current_year  #copy countries except for the first year
        else: countries_previous_year = countries

        COW_current_year = COW_df[COW_df['year'] == current_year]
        countries_current_year = set(np.concatenate([COW_current_year['statea'].unique(),COW_current_year['stateb'].unique()]))
        

    else:  # individual events
        # extract country code and event sign
        regex = r'.*?([A-Z]+)\s*([+-]?\d+)'
        matches = re.match(regex, text_content)
        country_code = matches.group(1)
        event_sign = int(matches.group(2))


        # Add event sign to DataFrame. To include it, we ask the country to be at least in both the current year and the previous year
        if country_code in countries and country_code in countries_current_year and country_code in countries_previous_year: 
            Ground_Truth.loc[current_year, country_code] = event_sign
        elif country_code not in countries: 
            print('Warning: country code {} not found in list of countries'.format(country_code))



Ground_Truth.to_excel('data/Complete_Ground_Truth_Matrix.xlsx')
