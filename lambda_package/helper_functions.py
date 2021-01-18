import pandas as pd
import numpy as np

'''
A 1.5*Interquartile range outlier 
detection/removal function that gets 
rid of outlying rows and returns 
that outlier cleaned dataframe
'''

def rm_outlier(df): 

    iqrs= []
    outliers_total = []
    
    for col in range(len(df.columns)):

        column = []

        for row in range(len(df)):
            if np.isnan(df.iloc[row,col]):
                pass
            else:
                column.append(df.iloc[row,col])

        if len(column)/2 == 0:
            q1 = column[0:int(len(column)/2)].median()
            q3 = column[int(len(column)/2):len(column)].median()
        else:
            q1_bounder = int(len(column)/2 - 0.5)
            q3_bounder = int(len(column)/2 + 0.5)
            q1 = column[0:q1_bounder].median()
            q3 = column[q3_bounder:len(column)].median()

        iqr = q3 - q1
        iqrs.append(iqr)
        outliers_col = (df.iloc[:col] < (q1 - 1.5 * iqr))|(df.iloc[:col] > (q3 + 1.5 * iqr))
        outliers_total.append(outliers_col)
    
    outliers_total = pd.DataFrame(outliers_total)
    df = df.iloc[~outliers_total.any(axis=1)]

    return df


def randomize(df, seed):

    for col in range(len(df.columns)):
        initial_column = list(df.iloc[:col])
        derivative_column = []
        initial_places = []
        derivative_places = []

        for i in range(len(df)):
            initial_places.append(i)
            derivative_places.append(0)
            derivative_column.append(0)

        for num in initial_places:
            # set new place in the list based on the seed
            l = (num + seed) % len(initial_places)
            derivative_places[l] = num

        for val in derivative_places:
            for k in range(len(initial_column)):
                derivative_column[val] = initial_column[k]

        df.iloc[:col] = derivative_column

    return df
            

            


        
    


    
    









