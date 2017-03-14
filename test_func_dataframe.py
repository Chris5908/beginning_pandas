# coding - UTF8

# --------------------------------------------------------------------------------------------#
#                                                                                             #
#                                                                                             #
#   Test the functions with a basic dataframe                                                 #
#                                                                                             #
#                                                                                             #
#   copyright @ Christophe PERE : March 14, 2017                                              #
#                                                                                             #
# --------------------------------------------------------------------------------------------#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import math as M
import functions_make
import functions

df = pd.read_csv('/Users/christophepere/Desktop/data_test/vr2.csv', sep=';',encoding='ISO-8859-1')

marques_PSA = ['PEUGEOT', 'CITROEN', 'DS AUTOMOBILES']

interv = [0,12000]
interv2 = [14500, 17000]                       #[12001,16000]
interv3 = [17001, 20000]                       #[16001,20000]
interv4 = [20001,1e6]                          #[20001,26000]

interv_all=[0, 12000, 14500, 17000, 20000, 1e6]

f2_predict, df3 = functions.funcDataFrameYear3(df, 2016, 2016, 2016 ,marques=marques_PSA, interv=interv) #predict='Values'

print('\n\n')
print(df3)
print('\n\n')
#

#df3.to_csv('Results_PSA_NB>=20.csv','\t')
