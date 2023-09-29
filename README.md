### Netsci_meets_history ###

This repository contains the python codes for the article "Local balance of signed networks: Definition and application to reveal historical events in international relations", written by Fernando Diaz-Diaz, Paolo Bartesaghi and Ernesto Estrada. Each section roughly corresponds to one directory of this repository.

Description of each directory:

0) list_historical_events contains a list with the events considered to create the ground Truth matrix. The list includes year, country, sign (+1 for non-violent and -1 for violent) and brief description of the event.

1)comparison_with_centrality_measures compares the local balance index with four other measures, both in two small networks and in the Gahuku-Gama dataset.

2) Ground_Truth_Matrix_comparison contains the code to create the ground truth matrix of historical events, the local balance event matrix, and a script to find the correaltions between the two.

3) 3) GPR_comparison contains the code that compares the local balance time sereis with the GeoPolitical Risk timeseries.

4) maps contains the code to plot a world map together with the IR network of a particular year. One can also choose to plot only a subgraph of the IR network.

5) balance_timeseries_analysis contains the codes used to create histograms of the interevent time and size distributions, using the data contained in the excel files IET and magnitude_sizes, respectively. It also calculates the distribution of the duration of positive and negative edges, and neutral relations. The file  extract_durations.py is an auxiliary file with functions needed to find the dration of alliances, conflicts and neutral events. It is used by the time_series_distributions notebook.

6) county_codes_and_coordinates.csv contains the ISO_3, latitude and longitude of every country, among other things. It is used to translates full names to iso-3 names when needed, and to correctly position the nodes of the IR network over the world map.


IMPORTANT: Data Set Not Included
This repository does not include the data set used in the project. We do not possess the rights to distribute the data set, because it is the property of Prof. Zeev Maoz. If you require access to the data set, please contact Prof. Maoz directly at zmaoz@ucdavis.edu to request permission. We apologize for the inconvenience.

For any other question, please contact fernandodiaz@ifisc.uib-csic.es
