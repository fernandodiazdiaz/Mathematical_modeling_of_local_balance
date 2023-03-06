### Netsci_meets_history ###

This repository contains the python codes for the article "Network science meets history: Local balance in global international relations", written by Fernando Diaz-Diaz, Paolo Bartesaghi and Ernesto Estrada.

Description of each notebook:

1) descriptive_statistics some important variables of the temporal network of international relations (like the number of nodes, connected components, etc.)

2) balance_timeseries plots the local balance of individual countries as a function of time.

3) synthetic_signed_cliques creates synthetic graphs of the form K_n(K_l^-) and calculates the local balance index of their nodes.

4) find_negative_cliques was the program used to detect the K_n(K_l^-) present in the data set. 

5) plot_maps plots a world map together with the IR network of a particular year. One can also choose to plot only a subgraph of the IR network.

6) time_series_distributions creates histograms of the interevent time and size distributions, ausing the data contained in the excel files IET and magnitude_sizes, respectively. It also alculates the distribution of the duration of positive and negative edges, and neutral relations.

7) extract_durations.py is an auxiliary file with functions needed to find the dration of alliances, conflicts and neutral events. It is used by the time_series_distributions notebook.

8) county_codes_and_coordinates.csv contains the ISO_3, latitude and longitude of every country, among other things. It is used to translates full names to iso-3 names when needed, and to correctly position the nodes of the IR network over the world map.

9) comments_time_series_distributions.txt specifies details about the process from which we created the excel files used in time_series_distributions.

IMPORTANT: Data Set Not Included
This repository does not include the data set used in the project. We do not possess the rights to distribute the data set, because it is the property of Prof. Zeev Maoz. If you require access to the data set, please contact Prof. Maoz directly at zmaoz@ucdavis.edu to request permission. We apologize for the inconvenience.

For any other question, please contact fernandodiaz@ifisc.uib-csic.es
