# coding - UTF8

# --------------------------------------------------------------------------------------------#
#                                                                                             #
#                                                                                             #
#   The function : funcDataFrameYear take different paramters, df : dataframe ; annee = year  #
#   of immatriculation ; annee_fin = last year for the study ; annee_debut : first year of    #
#   the study ; marques : name(s) of the enterprise(s) ; models = model(s) of the car(s) ;    #
#   interv is the price interval for the study, if more two values are provided the soft      #
#   generate itself the the different reference intervals with the values ; predict is a      #
#   alias if you want to work with the values or the prediction representation                #
#                                                                                             #
#                                                                                             #
#   copyright @ Christophe PERE : March 14, 2017                                              #
#                                                                                             #
# --------------------------------------------------------------------------------------------#

import numpy as np
import math as M
import random
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import datetime
from dateutil.parser import parse
from functions_make import *
import itertools

def funcDataFrameYear(df,  annee=datetime.datetime.now().year, annee_fin=0, annee_debut=0, marques=["all"], models=["all"], interv=["all"], predict=None ):
    
    # ---- Get the dates in the header of the dataframe ------------------------------------------------------
    head_df = list(df)                                      # get the header
    dates = [validate2(i) for i in head_df]                 # return the date if it's validate or None
    dates = [i for i in dates if i!=None]                   # return a list of the dates
    dates = sorted(dates, key=lambda x:x[3:7])              # sort the list by year
    
    # ---- Get 'vr' data and when the sample is >= 5 cars ----------------------------------------------------
    df_all_vr = df[df['Type']=='vr']                        # selection des vr
    df_vr = df_all_vr[df_all_vr['NB']>=1]                   # selection des vehicules quand leur nombre depasse x
    
    
    # ---- Computation of the slice's month and the difference between years ----------------------------------
    df_year_unique = sorted(df_vr['Date MEC'].unique(), key=lambda x:x)     # get the different years in Date MEC and return the unique values
    
    # ---- Index columns with the first value of the VR  ------------------------------------------------------
    
    #first_valid_loc = df_vr.ix[:,month1:month2].apply(lambda row: row.first_valid_index(),axis=1)
    #first_valid_null = first_valid_loc.index[first_valid_loc.isnull()]
    #first_valid_nonnull = first_valid_loc.drop(first_valid_null)
    if 2017 in df_year_unique:                              # test if 2017 is in the list
        df_year_unique.remove(2017)                         # remove the year 2017
    
    month1, month2, delta_year = funcMonth(df_year_unique[0],df_year_unique[len(df_year_unique)-1], df_year_unique[0], dates) # computation of the months slices and the year variation
    new_col = get_first_non_null_vec(df_vr.ix[:,month1:month2]) # get the first value of each row between the columns month1 and month2
    new_col = pd.Series(new_col, index=df_vr.index)             # pass from list to Series (pandas) with the same index of the dataframe
    df_vr['First Value'] = new_col                              # add a column at the end of the dataframe with the fist value of each row


    if annee!=datetime.datetime.now().year:                     # test on the first parameter annee, if a value is passed in parameter
        df_year_unique = [annee]                                # transforme the value in list

    frames = []                                                 # creation of empty lists to receive the all final dataframe
    frames2 = []
    
    
    for date in df_year_unique :                                # loop on the year, if a value is enter, the script work on this year, is no value is enter, the script uses the unique values available in 'Date MEC'
        
        if len(interv)>2:                                       # if the interval contain more than 2 values
            n = 2                                               # value number per interval
            intervTuples = [interv[i:i+n] for i in range(0, len(interv)-1, 1)]      # parse the list in interval two by two
            for interval in intervTuples :                      # loop on the number of interval
                frames, frames2 = funcDataFrameComput(df_vr,  date, annee_fin, annee_debut, marques, models, interval, predict, dates, frames, frames2 )                           # function of computation

        else:
            frames, frames2 = funcDataFrameComput(df_vr,  date, annee_fin, annee_debut, marques, models, interv, predict, dates, frames, frames2 )                                       # make all the dataframes


    result = pd.concat(frames)                                  # concatenate all the dataframes in one
    result2= pd.concat(frames2)
    return result, result2                                        # return only if row has one number
    
