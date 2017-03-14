# beginning_pandas
algorithm to use data frame/Series and modified it 

The project implies three python files and a csv files. This last file is the dataframe using during the study. 

The goals of this scripts are to generate dataframe with a probability of accuracy of the prediction of the value of a car. 

Different cars are in the csv file, we have generate an price estimation during a timeline depending of the date MEC (it's the immatriculation of the car dating of the first January of the year. 

The different parameters permit to get data of the big data frame using the pandas library. They permit to reduce the number of data and make statistique on the estimation price. 

At the end, the final DF show the results : 

                                                     Good   Near    Bad
For PEUGEOT/CITROEN/DS AUTOMOBILES in 2016 Numb...     17     26      5
Percent(2016) values = 0, 12000                     35.42  54.17  10.42
Mean %(2016)                                         3.93   7.14  11.78
Mean €(2016)                                          425    824   1536


What's it ? In this case I have isolate three brands (PSA group) and study the registered vehicules of the year 2016 whose price is between 0 and 12000€. The function compute the data and class it in three branchs Good (the price is near 5% or near 500€ of the final estimation (comparaison between the mean year and a final value), Near (10% or 1000€) and Bad (others). 

The function return the number of each prediction and the percent representation, and the mean of the percent and difference price. 

The parameters are : 

df          : it's the reference dataframe 
annee       : year of registered 
annee_fin   : upper edge of the study 
annee_debut : lower edge of the study 
marques     : brand 
models      : model of car
interv      : price intervals
predict     : Values for the values or None for Good/Near/Bad

The function can be used without parameters (initialisation parameters in the loop), the only one mandatory is the reference dataframe : df 

marques/models  can be string (one brand/one model) or list of string (several brands/several models)
interv          can be a list of two values or more 



Enjoy and comment ! 
