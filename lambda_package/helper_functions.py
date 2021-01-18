import pandas as pd
import numpy as np


class HelperFunctions():
    
    def __init__(self, data, seed=None):
        if not type(data) == pd.DataFrame:
            raise ValueError('Parameter must be of type pd.DataFrame.')
        self.data = data
        self.seed = seed

    def __str__(self):
        return f'pandas DataFrame {self.data[0]}'

    def rm_outliers(self): 
        iqrs= []
        outliers_total = []
        # for each column in the dataframe create a list of values
        for col in self.data.columns:
            column = self.data.iloc[col].tolist()
            column.dropna(inplace=True)
            column.sort()
            if len(column)/2 == 0:
                q1_bounder = int(len(column)/2)
                q3_bounder = int(len(column)/2)
                q1 = column[0:q1_bounder].median()
                q3 = column[q3_bounder:len(column)].median()
            else:
                q1_bounder = int(len(column)/2 - 0.5)
                q3_bounder = int(len(column)/2 + 0.5)
                q1 = column[0:q1_bounder].median()
                q3 = column[q3_bounder:len(column)].median()
            # create a list of interquartile ranges of each column
            iqr = q3 - q1
            iqrs.append(iqr)
            outliers_col = (self.data[col] < (q1 - 1.5 * iqr))|(self.data[col] > (q3 + 1.5 * iqr))
            outliers_total.append(outliers_col)
        outliers_total = pd.DataFrame(np.array(outliers_total))
        self.data = self.data.iloc[~outliers_total.any(axis=1)]

        return self.data

    def randomize(self):
        for col in self.data.columns:
            initial_column = self.data[col].tolist()
            derivative_column = []
            initial_places = []
            derivative_places = []
            for i in range(len(self.data)):
                initial_places.append(i)
                derivative_places.append(0)
                derivative_column.append(0)
            # give new place to each number based on the seed
            for num in initial_places:
                l = (num + self.seed) % len(initial_places)
                derivative_places[l] = num
            for val in derivative_places:
                for k in range(len(initial_column)):
                    derivative_column[val] = initial_column[k]
            self.data[col] = derivative_column

        return self.data

if __name__ == "__main__":
    print("Enter a number")
            

            


        
    


    
    









