# coding - UTF8

# ---------------------------------------------------------------------------------------------
#   This file regroup different functions used in the final function
#
#           funcDataFrameYear
#
#   available in the file functions.py
#
#   copyright @ Christophe PERE : March 14, 2017
#
# ---------------------------------------------------------------------------------------------

import numpy as np
import math as M
import random
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import datetime
from dateutil.parser import parse

def find_nearest(array,value):
    idx=(abs(array-value)).argmin()
    return idx



def validate2(date_text):
    try:
        parse(date_text)
        return date_text
    except:
        pass

def func_close_nearest(lst, value):
    return next((x for x in lst if M.fabs((x-value)/value)<=0.0001))



def funcMonth(annee=datetime.datetime.now().year, annee_fin=0, annee_debut=0, dates=[2012,2013] ): # create str for the month begin and end of the DataFrame and the difference between the year of beginning and end

    if annee_fin > 0 and annee_debut == 0 :
        month1 = '01/'+str(annee_fin)
        month2 = '12/'+str(annee_fin)
        delta_year = annee_fin - annee
    
    elif annee_fin > 0 and annee_debut > 0 :
        month1 = '01/'+str(annee_debut)
        month2 = '12/'+str(annee_fin)
        delta_year = annee_fin - annee_debut
    else :
        month1 = dates[0]
        month2 = dates[len(dates)-1]
        delta_year = datetime.datetime.now().year - annee -1
    
    return month1, month2, delta_year

def funcNames(i, annee_save, annee, marques, models, interval): # func for names creation with parameters test
    if i ==0:
        if marques[0]!="all":
            names = marques[0]
            if len(marques)!=1:
                names = '/'.join(marques)
                    

            name1 = 'For '+names+' in '+str(annee_save)+' Numb('+str(annee)+')'
            name3 = 'For '+names+' in '+str(annee_save)+' Predict '+str(annee)

        elif models[0]!="all":
            names = models[0]
                    
            if len(models)!=1:
                names = ' '.join(models)
            
            name1 = 'For '+names+' in '+str(annee_save)+' Numb('+str(annee)+')'
            name3 = 'For '+names+' in '+str(annee_save)+' Predict '+str(annee)
                
        else:
            name1 = 'For '+str(annee_save)+' Numb('+str(annee)+')'
            name3 = 'For '+str(annee_save)+' Predict '+str(annee)
    else:
        if interval!=["all"]:
        
            name1 = 'Numb('+str(annee)+')'+' values = '+str(interval[0])+', '+str(interval[1])
            name3 = 'Predict '+str(annee)
        else:
            name1 = 'Numb('+str(annee)+')'+' value = '+interv[0]
            name3 = 'Predict '+str(annee)

    return name1, name3

def funcTestValues(ca):     # function to compute the number of values, mean, and %
    try:
        
        try:                                                                                     # test if the ca is not = NaN
            bad_value = (len(ca[ca=='BAD    ']))
        except:
            bad_value=0
        try:
            medium_value = (len(ca[ca=='MEDIUM']))
        except:
            medium_value=0
        try:
            good_value = (len(ca[ca=='GOOD']))
        except:
            good_value=0
        try:
            percent_bad_value = bad_value/(sum([bad_value,medium_value,good_value]))*100
        except:
            percent_bad_value=0
        try:
            percent_medium_value = medium_value/(sum([bad_value,medium_value,good_value]))*100
        except:
            percent_medium_value = 0
        try:
            percent_good_value = good_value/(sum([bad_value,medium_value,good_value]))*100
        except:
            percent_good_value = 0

        return bad_value, medium_value, good_value, percent_bad_value, percent_medium_value, percent_good_value
    except:
        return 'Error or empty dataframe '


def funcTestGap(a_save,  c_save, ca): # function to generate a final Series with char instead of values
    try:                                                                                     # test if the ca is not = NaN
        mean_percent_good    = a_save[ca=='GOOD'].mean().round(2)
    except:
        mean_percent_good    = 0
    try:
        mean_price_good      = int(c_save[ca=='GOOD'].mean().round(0))
    except:
        mean_price_good      = 0
    try:                                                                                     # test if the ca is not = NaN
        mean_percent_medium  = a_save[ca=='MEDIUM'].mean().round(2)
    except:
        mean_percent_medium  = 0
    try:
        mean_price_medium    = int(c_save[ca=='MEDIUM'].mean().round(0))
    except:
        mean_price_medium    = 0
    try:                                                                                     # test if the ca is not = NaN
        mean_percent_bad     = a_save[ca=='BAD    '].mean().round(2)
    except:
        mean_percent_bad     = 0
    try:
        mean_price_bad       = int(c_save[ca=='BAD    '].mean().round(0))
    except:
        mean_price_bad       = 0

    return '%.2f'%mean_percent_good, '%.0d'%mean_price_good, '%.2f'%mean_percent_medium, '%.0d'%mean_price_medium, '%.2f'%mean_percent_bad, '%.0d'%mean_price_bad


def get_first_non_null_vec(df):                                                               # Find the first value non null in the dataframe and return a vector with the first value
    a = df.values
    n_rows, n_cols = a.shape
    col_index = np.isnan(a).argmin(axis=1)
    flat_index = n_cols * np.arange(n_rows) + col_index
    return a.ravel()[flat_index]



'''
def funcDataFrameYear(df, annee=datetime.datetime.now().year, annee_fin=0, annee_debut=0, marques="all", model="all"):

    df_all_vr = df[df['Type']=='vr']                        # selection des vr
    df_vr = df_all_vr[df_all_vr['NB']>=5]                   # selection des vehicules quand leur nombre depasse 4
    
    df_vr_annee = df_vr[df_vr['Date MEC']==annee]           # recupere les vehicules par annee (date MEC)
    month1, month2, delta_year = funcMonth(annee,annee_fin, annee_debut)
    df_diff_price_annee = df_vr_annee.ix[:,month1:month2].sub(df_vr_annee['02/2017'],0)          # calcul la
    y = df_vr_annee['02/2017']
    df_percent_annee = df_vr_annee.ix[:,month1:month2].apply(lambda x: (x-y)*100/y,0).apply(lambda x: pd.to_numeric(x))                                       # percent computation
    df_diff_price_annee[df_diff_price_annee<0] = -df_diff_price_annee   # absolute number
    
    df_percent_annee[df_percent_annee<0] = -df_percent_annee            # absolute number
    annee_save = annee                                                  # save the year of reference
    if(delta_year>=0):                                                  # test on the year
        i = 0
        e = {}                                                          # empty dict
        columns1 = []                                                   # header final dataframe
        columns2 = []

        #print(delta_year)
        if(annee_debut != 0):                                           # test on the parameter to determine the year of the begin =/= Date MEC
            annee = annee_debut
        while i <= delta_year:                                          # loop on the year's number for the computation
            month1 = '01/'+str(annee)                                   # month beginning
            month2 = '12/'+str(annee)                                   # month ending
            a = df_percent_annee.ix[:,month1:month2].mean(axis=1).round(2)  # computation of the mean per row with 2 decimals
            b = df_percent_annee.ix[:,month1:month2].std(axis=1).round(2)   # computation of the standard deviation per row with 2 decimals
            c = df_diff_price_annee.ix[:,month1:month2].mean(axis=1).round() # computation of the mean per row with 0 decimals
            d = df_diff_price_annee.ix[:,month1:month2].std(axis=1).round() # computation of the standard deviation per row with 0 decimals
            if i ==0 :
                name1 = 'For '+str(annee_save)+' mean % '+str(annee)        # make name of the first column
            else :
                name1 = 'mean % '+str(annee)        # make name of the first column
            
            name2 = 'std % '+str(annee)                                 # name of the second
            e[name1] = pd.Series(np.array(a), index=df_vr_annee['Ref ID']) # Series on pandas -> mean computation with the index
            e[name2] = pd.Series(np.array(b), index=df_vr_annee['Ref ID'])
            name3 = 'mean price '+str(annee)
            name4 = 'std price '+str(annee)
            e[name3] = pd.Series(np.array(c), index=df_vr_annee['Ref ID'])
            e[name4] = pd.Series(np.array(d), index=df_vr_annee['Ref ID'])
            annee+=1                                                    # increment year
            i+=1                                                        # increment loop
            columns1.append(name1)
            columns1.append(name2)
            columns1.append(name3)
            columns1.append(name4)
        
            #columns2.append(name3)
                            
        df2 = pd.DataFrame(columns = columns1 , data = e)                                           # pass from dict to DataFrame
        df2.name = 'DataFrame for vehicules with Date MEC = {}'.format(annee_save)
        #print('DataFrame for vehicules with Date MEC = {}'.format(annee_save))
        return df2[df2[columns1[int(len(columns1)/2)]]>0]                                        # return only if row has one number

    else:
        return "The year is in the futur, go ahead with a doloreane"


def funcDataFrameYear2(df,  annee=None, annee_fin=0, annee_debut=0, marques=["all"], models=["all"], interv=["all"], predict=None ):
    # ---- Get the dates in the header of the dataframe ------------------------------------------------------
    head_df = list(df)                                      # get the header
    dates = [validate2(i) for i in head_df]                 # return the date if it's validate or None
    dates = [i for i in dates if i!=None]                   # return a list of the dates
    dates = sorted(dates, key=lambda x:x[3:7])              # sort the list by year
    
    # ---- Get 'vr' data and when the sample is >= 5 cars ----------------------------------------------------
    df_all_vr = df[df['Type']=='vr']                        # selection des vr
    df_vr = df_all_vr[df_all_vr['NB']>=0]                   # selection des vehicules quand leur nombre depasse x
    
    #df_vr = df_all_vr
    
    # ---- Computation of the slice's month and the difference between years ----------------------------------
    
    month1, month2, delta_year = funcMonth(annee,annee_fin, annee_debut, dates)
    
    # ---- Index columns with the first value of the VR  ------------------------------------------------------
    
    #first_valid_loc = df_vr.ix[:,month1:month2].apply(lambda row: row.first_valid_index(),axis=1)
    #first_valid_null = first_valid_loc.index[first_valid_loc.isnull()]
    #first_valid_nonnull = first_valid_loc.drop(first_valid_null)
    
    new_col = get_first_non_null_vec(df_vr.ix[:,month1:month2])
    new_col = pd.Series(new_col, index=df_vr.index)
    df_vr['First Value'] = new_col
    
    # ---- Conditions implies by parameters -------------------------------------------------------------------
    
    df_year_unique = sorted(df_vr['Date MEC'].unique(), key=lambda x:x)
    
    
    
    
    if interv[0]=="all":
        pass
    else:
        #df_vr = df_vr[(df_vr[dates[len(dates)-1]]>=interv[0]) & (df_vr[dates[len(dates)-1]]<=interv[1])]
        df_vr = df_vr[(df_vr['First Value']>=interv[0]) & (df_vr['First Value']<=interv[1])]
    if annee!=None:
        df_vr_annee = df_vr[df_vr['Date MEC']==annee]           # recupere les vehicules par annee (date MEC)
    else:
        df_vr_annee = df_vr
    if type(marques)!=list:
        marques = [marques]
    if marques[0]!="all":
        df_vr_annee2 = []
        for i in marques:
            df_vr_annee2.append(df_vr_annee[df_vr_annee['Marque']==i])
        df_vr_annee = df_vr_annee2.copy()
        df_vr_annee= pd.concat(df_vr_annee, axis=0)
    if type(models)!=list:
        models = [models]
    if models[0]!="all":
        df_vr_annee2 = []
        if len(models)==1:
            df_vr_annee = df_vr_annee[df_vr_annee['Modele']==models[0]]
        else:
            for i in models:
                df_vr_annee2.append(df_vr_annee[df_vr_annee['Modele']==i])
            df_vr_annee = df_vr_annee2.copy()
            df_vr_annee= pd.concat(df_vr_annee, axis=0)

#    print(df_vr_annee.ix[:,'01/2016':'12/2016'].mean(axis=1).count())
    # ---- Diff between the mean vr on the year and a reference (last value) ----------------------------------

    df_diff_price_annee = df_vr_annee.ix[:,month1:month2].sub(df_vr_annee[dates[len(dates)-1]],0)

    # ---- Computation of the % between the mean vr on the year and a reference (last value) ------------------

    y = df_vr_annee[dates[len(dates)-1]]
    df_percent_annee = df_vr_annee.ix[:,month1:month2].apply(lambda x: (x-y)*100/y,0).apply(lambda x: pd.to_numeric(x))

    # ---- Positive values ------------------------------------------------------------------------------------

    df_diff_price_annee[df_diff_price_annee<0] = -df_diff_price_annee   # absolute number
    df_percent_annee[df_percent_annee<0] = -df_percent_annee            # absolute number

    annee_save = annee                                                  # save the year of reference

    # ---- DataFrame computation ------------------------------------------------------------------------------
    if(delta_year>=0):                                                  # test on the year
        
        i = 0
        e = {}                                                          # empty dict
        f = {}
        columns1 = []
        columns2 = []
        #print(delta_year)
        if(annee_debut != 0):                                           # test on the parameter to determine the year of the begin =/= Date MEC
            annee = annee_debut
        while i <= delta_year:                                          # loop on the year's number for the computation
            #print(i, delta_year)
            month1 = '01/'+str(annee)                                   # month beginning
            month2 = '12/'+str(annee)                                   # month ending
            #print(df_vr_annee.ix[:,month1:month2].mean(axis=1).count())
            
            a = df_percent_annee.ix[:,month1:month2].mean(axis=1).round(2)  # computation of the mean per row with 2 decimals
            b = df_percent_annee.ix[:,month1:month2].std(axis=1).round(2)   # computation of the standard deviation per row with 2 decimals
            c = df_diff_price_annee.ix[:,month1:month2].mean(axis=1).round() # computation of the mean per row with 0 decimals
            d = df_diff_price_annee.ix[:,month1:month2].std(axis=1).round() # computation of the standard deviation per row with 0 decimals
            print(df_vr_annee.ix[:,month1:month2].mean(axis=1).count(), df_vr_annee['02/2017'].count(), a.count())
            # ---- Change values to str conditions ----------------------------------------------------------
            a_save = a.copy()
            a_str = a.copy()
            a_str[(a>5) & (a<=10)]='MEDIUM'
            a_str[(a<=5)]='GOOD'
            a_str[(a>10)]='BAD    '
            a = a_str.copy()
            
            c_save = c.copy()
            c_str = c.copy()
            c_str[(c>500) & (c<=1000)]='MEDIUM'
            c_str[(c<=500)]='GOOD'
            c_str[(c>1000)]='BAD    '
            c = c_str.copy()

            ca = a.copy()

            k=0
            for j in ca:                                                                             # test between char length to choose the minimum
                if(len(str(a.iat[k]))<len(str(c.iat[k]))):
                    ca.iat[k]=a.iat[k]
                
                else:
                    ca.iat[k]=c.iat[k]
                    k+=1

            # ---- Computation of the med

            mean_percent_good, mean_price_good, mean_percent_medium, mean_price_medium, mean_percent_bad, mean_price_bad = funcTestGap(a_save, c_save, ca)

            # ---- Test if the chain is non null ----

            bad_value, medium_value, good_value, percent_bad_value, percent_medium_value, percent_good_value = funcTestValues(ca)

            name1, name3 = funcNames(i,annee_save, annee,marques,models, interv)
            
            f[name1] = pd.Series(np.array([good_value, medium_value, bad_value]), index=['Good', 'Near', 'Bad'])
            name2 = 'Percent('+str(annee)+')'
            f[name2] = pd.Series(np.array(['%.2f'%percent_good_value, '%.2f'%percent_medium_value, '%.2f'%percent_bad_value]), index=['Good', 'Near', 'Bad'])
            name4 = 'Mean %('+str(annee)+')'
            f[name4] = pd.Series(np.array([mean_percent_good, mean_percent_medium, mean_percent_bad]), index=['Good', 'Near', 'Bad'])
            name5 = 'Mean €('+str(annee)+')'
            f[name5] = pd.Series(np.array([mean_price_good, mean_price_medium, mean_price_bad]), index=['Good', 'Near', 'Bad'])


            e[name3] = pd.Series(np.array(ca), index=df_vr_annee['Ref ID'])
            columns1.append(name1)
            columns1.append(name2)
            columns1.append(name4)
            columns1.append(name5)
            columns2.append(name3)
            #print(annee)
            annee+=1                                                    # increment year
            i+=1                                                        # increment loop
        #print(annee)

        df2 = pd.DataFrame(columns=columns2 , data = e)                                           # pass from dict to DataFrame
        df2.name = 'DataFrame for vehicules with Date MEC = {}'.format(annee_save)
        df3 = pd.DataFrame(columns=columns1, data = f)
        #print('DataFrame for vehicules with Date MEC = {}'.format(annee_save))
        return df2, df3                                        # return only if row has one number
    
    else:
        return "The year is in the futur, go ahead with a doloreane"

'''


def funcDataFrameComput(df_vr,  date, annee_fin, annee_debut, marques,  models,  interv, predict , dates, frames, frames2 ):                # function test parameters and computation of the difference in price, the % of the accuracy and the different dataframes
        if interv[0]=="all":                                    # test the interval values
            pass                                                # if nothing passed --> go ahead
        else:
            
            df_vr = df_vr[(df_vr['First Value']>=interv[0]) & (df_vr['First Value']<=interv[1])] # selection of the row corresponding to the interval determined by the first value of each row
        if date!=None:
            df_vr_annee = df_vr[df_vr['Date MEC']==date]        # get cars by years ('Date MEC')
            month1, month2, delta_year = funcMonth(date,annee_fin, annee_debut, dates)  # copmpute the month1, month2 and the delta year for the corresponding date
        else:
            df_vr_annee = df_vr                                 # use the all dataset
        if type(marques)!=list:                                 # test on the parameter marques
            marques = [marques]                                 # if one marques, passed from char to list
        if marques[0]!="all":                                   # test on the name
            df_vr_annee2 = []                                   # create empty list
            for i in marques:                                   # loop on the marques' name
                df_vr_annee2.append(df_vr_annee[df_vr_annee['Marque']==i])  # set a dataframe with all the row corresponding to the marques
            df_vr_annee = df_vr_annee2.copy()                   # make a copy
            df_vr_annee= pd.concat(df_vr_annee, axis=0)         # concatane all the dataframes
        if type(models)!=list:                                  # test on the models
            models = [models]
        if models[0]!="all":
            df_vr_annee2 = []
            if len(models)==1:
                df_vr_annee = df_vr_annee[df_vr_annee['Modele']==models[0]]
            else:
                for i in models:
                    df_vr_annee2.append(df_vr_annee[df_vr_annee['Modele']==i])
                df_vr_annee = df_vr_annee2.copy()
                df_vr_annee= pd.concat(df_vr_annee, axis=0)
    
    
        # ---- Diff between the mean vr on the year and a reference (last value) ----------------------------------
        
        df_diff_price_annee = df_vr_annee.ix[:,month1:month2].sub(df_vr_annee[dates[len(dates)-1]],0)
        
        # ---- Computation of the % between the mean vr on the year and a reference (last value) ------------------
        
        y = df_vr_annee[dates[len(dates)-1]]
        df_percent_annee = df_vr_annee.ix[:,month1:month2].apply(lambda x: (x-y)*100/y,0).apply(lambda x: pd.to_numeric(x))
        
        # ---- Positive values ------------------------------------------------------------------------------------
        
        df_diff_price_annee[df_diff_price_annee<0] = -df_diff_price_annee   # absolute number
        df_percent_annee[df_percent_annee<0] = -df_percent_annee            # absolute number
        
        annee_save = date                                                  # save the year of reference
        annee = date
        # ---- DataFrame computation ------------------------------------------------------------------------------
        if(delta_year>=0):                                                  # test on the year
            #print(annee)
            i = 0
            e = {}                                                          # empty dict
            f = {}
            columns1 = []
            columns2 = []
            #print(delta_year)
            if(annee_debut != 0):                                           # test on the parameter to determine the year of the begin =/= Date MEC
                annee = annee_debut
            while i <= delta_year:                                          # loop on the year's number for the computation
                #print(i, delta_year)
                month1 = '01/'+str(annee)                                   # month beginning
                month2 = '12/'+str(annee)                                   # month ending
                #print(df_vr_annee.ix[:,month1:month2].mean(axis=1).count())
                #print(month1, month2)
                a = df_percent_annee.ix[:,month1:month2].mean(axis=1).round(2)  # computation of the mean per row with 2 decimals
                b = df_percent_annee.ix[:,month1:month2].std(axis=1).round(2)   # computation of the standard deviation per row with 2 decimals
                c = df_diff_price_annee.ix[:,month1:month2].mean(axis=1).round() # computation of the mean per row with 0 decimals
                d = df_diff_price_annee.ix[:,month1:month2].std(axis=1).round() # computation of the standard deviation per row with 0 decimals
                #print(df_vr_annee.ix[:,month1:month2].mean(axis=1).count(), df_vr_annee['02/2017'].count(), a.count())
                
                # ---- Change values to str conditions --------------------------------------------------
                a_save = a.copy()
                c_save = c.copy()
                
                e, f, columns1, columns2 = funcTestPredict(a, b, c, d, i, annee_save, annee, marques, models, predict , e, f, columns1, columns2, df_vr_annee, interv) # compute the results and the name of the columns for the final dataframe
                
                annee+=1                                                    # increment year
                i+=1                                                        # increment loop

            
            df2 = pd.DataFrame(columns=columns2 , data = e)                 # pass from dict to DataFrame
            df2.name = 'DataFrame for vehicules with Date MEC = {}'.format(annee_save)
            df3 = pd.DataFrame(columns=columns1, data = f)
            df2 = df2.T                                                     # transpose the dataframe
            df3 = df3.T
            if predict=='Values':
                
                df2 = df2.T
                df3 = df3.T
            frames.append(df2)
            frames2.append(df3)



        return frames, frames2

def funcTestLetter(a, c):       # pass from values to term (char) test it to find the best solution and return a Series with it
    a_str = a.copy()
    a_str[(a>5) & (a<=10)]='MEDIUM'
    a_str[(a<=5)]='GOOD'
    a_str[(a>10)]='BAD    '
    a = a_str.copy()
                    
    c_save = c.copy()
    c_str = c.copy()
    c_str[(c>500) & (c<=1000)]='MEDIUM'
    c_str[(c<=500)]='GOOD'
    c_str[(c>1000)]='BAD    '
    c = c_str.copy()
                    
    ca = a.copy()
                    
    k=0
    for j in ca:                                                                             # test between char length to choose the minimum
        if(len(str(a.iat[k]))<len(str(c.iat[k]))):
            ca.iat[k]=a.iat[k]
                
        else:
            ca.iat[k]=c.iat[k]
        k+=1

    return ca


def funcNamesSeries(name1, name3, good_value, medium_value, bad_value, mean_percent_good, mean_percent_medium, mean_percent_bad, percent_good_value, percent_medium_value, percent_bad_value, mean_price_good, mean_price_medium, mean_price_bad, annee, f, columns1, interval, i):  # Generate the final dict containing good, bad, and medium values and their % and diff price


    f[name1] = pd.Series(np.array([good_value, medium_value, bad_value]), index=['Good', 'Near', 'Bad'])
    if interval!=["all"] and i==0:
        name2 = 'Percent('+str(annee)+')'+' values = '+str(interval[0])+', '+str(interval[1])
    else:
        name2 = 'Percent('+str(annee)+')'#+' value = '+interval[0]
    
    f[name2] = pd.Series(np.array(['%.2f'%percent_good_value, '%.2f'%percent_medium_value, '%.2f'%percent_bad_value]), index=['Good', 'Near', 'Bad'])
    name4 = 'Mean %('+str(annee)+')'
    f[name4] = pd.Series(np.array([mean_percent_good, mean_percent_medium, mean_percent_bad]), index=['Good', 'Near', 'Bad'])
    name5 = 'Mean €('+str(annee)+')'
    f[name5] = pd.Series(np.array([mean_price_good, mean_price_medium, mean_price_bad]), index=['Good', 'Near', 'Bad'])
    
    columns1.append(name1)
    columns1.append(name2)
    columns1.append(name4)
    columns1.append(name5)


    return f, columns1

def funcTestPredict(a, b, c, d, i, annee_save, annee, marques, models, predict, e, f, columns1, columns2, df_vr_annee, interv):     # choose between to cases, if we want a table with good/medium/bad and the values

    if predict!='Values':                               # Test if the parameter predict is equal to 'Values'
    
        ca = funcTestLetter(a, c )
    # ---- Computation of the med -------------------------------------------------------------------
        
        mean_percent_good, mean_price_good, mean_percent_medium, mean_price_medium, mean_percent_bad, mean_price_bad = funcTestGap(a, c, ca)
            
    # ---- Test if the chain is non null ------------------------------------------------------------
            
        bad_value, medium_value, good_value, percent_bad_value, percent_medium_value, percent_good_value = funcTestValues(ca)
                
                
    # ---- Make the final dict + names -------------------------------------------------------------
        name1, name3 = funcNames(i,annee_save, annee,marques,models, interv)
                    
        f, columns = funcNamesSeries(name1, name3, good_value, medium_value, bad_value, mean_percent_good, mean_percent_medium, mean_percent_bad, percent_good_value, percent_medium_value, percent_bad_value, mean_price_good, mean_price_medium, mean_price_bad, annee, f, columns1, interv, i)
        #columns1.append(columns)
        e[name3] = pd.Series(np.array(ca), index=df_vr_annee['Ref ID'])
        columns2.append(name3)
            
    else:
        if i ==0 :
            name1 = 'For '+str(annee_save)+' mean % '+str(annee)        # make name of the first column
        else :
            name1 = 'mean % '+str(annee)        # make name of the first column
                    
            name2 = 'std % '+str(annee)                                 # name of the second
            f[name1] = pd.Series(np.array(a), index=df_vr_annee['Ref ID']) # Series on pandas -> mean computation with the index
            f[name2] = pd.Series(np.array(b), index=df_vr_annee['Ref ID'])
            name3 = 'mean price '+str(annee)
            name4 = 'std price '+str(annee)
            f[name3] = pd.Series(np.array(c), index=df_vr_annee['Ref ID'])
            f[name4] = pd.Series(np.array(d), index=df_vr_annee['Ref ID'])
            columns1.append(name1)
            columns1.append(name2)
            columns1.append(name3)
            columns1.append(name4)
    #columns = columns1
    return e, f, columns1, columns2

