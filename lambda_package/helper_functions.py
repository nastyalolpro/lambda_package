import pandas as pd
import numpy as np


class HelperFunctions(pd.DataFrame):

    def __init__(self, data, seed=None):
        """[summary]

        Args:
            data (pd.DataFrame): pandas DataFrame
            seed (integer): Set seed to make random 
            function reproducible. Defaults to None.

        Raises:
            ValueError: raises error if data is not pandas DataFrame
        """        
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Parameter must be of type pd.DataFrame.')
        self.data = data
        self.seed = seed

    def __str__(self):
        return f'pandas DataFrame {self.data[0]}'

    def rm_outliers(self):
        """Removes outliers based on the Interquartile range.

        Returns:
            pd.DataFrame: cleaned data frame
        """        
        iqrs = []
        outliers_total = []
        # for each column in the dataframe create a list of values
        for col in self.data.columns:
            column = self.data[col].dropna(inplace=True).tolist()
            column.sort()
            if len(column) / 2 == 0:
                q1_bounder = int(len(column) / 2)
                q3_bounder = int(len(column) / 2)
                q1 = column[0:q1_bounder].median()
                q3 = column[q3_bounder:len(column)].median()
            else:
                q1_bounder = int(len(column) / 2 - 0.5)
                q3_bounder = int(len(column) / 2 + 0.5)
                q1 = column[0:q1_bounder].median()
                q3 = column[q3_bounder:len(column)].median()
            # create a list of interquartile ranges of each column
            iqr = q3 - q1
            iqrs.append(iqr)
            outliers_col = (self.data[col] < (
                q1 - 1.5 * iqr)) | (self.data[col] > (q3 + 1.5 * iqr))
            outliers_total.append(outliers_col)
        outliers_total = pd.DataFrame(np.array(outliers_total))
        self.data = self.data.iloc[~outliers_total.any(axis=1)]

        return self.data

    def randomize(self):
        """Takes in DataFrame and random seed.
        Mixes up data based on the seed. 

        Returns:
            pd.DataFrame: [description]
        """        
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
    data = {}
    rows = []
    more_cols = input('Want to create a data frame? y/n  :')
    while more_cols == 'y':
        last_rows = rows
        rows = []
        n = 1
        column = input('Enter column name: ')
        value = float(input('Enter {} row: '.format(n)))
        rows.append(value)
        more_rows = input('More rows? y/n  ')
        while more_rows == 'y':
            n += 1
            value = float(input('Enter {} row: '.format(n)))
            rows.append(value)
            more_rows = input('More rows? y/n  :')
        data[column] = rows
        if len(data) > 1:
            if len(last_rows) != len(rows):
                raise IndexError('Length of columns do not match.')
        more_cols = input('More columns? y/n  :')
    
    df = pd.DataFrame(data=data)
    print("Shape of the data is: ", df.shape)

    remove_outliers = input("Do you want to remove outliers? y/n  :")
    if remove_outliers == 'y':
        df = HelperFunctions(df)
        df.rm_outliers()
        print("Shape of the data frame without outliers is: ", df.shape)

    mix_data = input("Do you want to mix up your data? y/n  :")
    if remove_outliers == 'y':
        seed = int(input("Enter random seed:  "))
        df = HelperFunctions(df, seed=seed)
        df.randomize()
        print("First row is now: ", df[0])
    