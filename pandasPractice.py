"""
Second Part: Create your code.

In this module you should implement a code that reads the file
nba.xlsx (taken from https://www.geeksforgeeks.org/python-pandas-dataframe/)
and import it as a pandas dataframe and process it.

There should be functions or methods that:

0) Read and import excel file into pandas dataframe (df)
1) Prints the df
2) Return a df with a single given column from the original df
3) Return a list or array (explain choise) from a given column
4) Return a sub-dataframe filtered by a column value
5) Return the merge of two dataframes (you can use the nba2.xlsx)
   with an inner join.
6) Output a given dataframe to an excel file.


Third Part: Challenge yourself
            Implement a simple API in Django with a storage
            in Postgresql that uses the methods for processing
            developed with pandas.
"""

import pandas as pd
import openpyxl

class xlsxData():
    
   def __init__(self):
      self.data = pd.DataFrame()

   def readData(self, file):
      self.data = pd.read_excel(file)

   def printData(self):
      print(self.data.to_string())

   def getColumnDf(self, column):
      return self.data[[column]]

   def getColumnArray(self, column):
      return self.data[column].values

   def getFilteredDf (self, column, value):
      return self.data[self.data[column].eq(value)]

   def intersectDf (self, data):
      return self.data.merge(data, how='inner')


def saveDf (df, file):
   df.to_excel(file) 

if __name__ == '__main__':
   nba = xlsxData() # Create the DataFrame object

   nba.readData("./nba.xlsx") # 0 Read nba.xlsx

   nba.printData() # 1 Print all the data

   nba.getColumnDf("Salary") # 2 Get one column as DataFrame

   nba.getColumnArray("Team") # 3 Get one column as numpy array to use less memory than a list

   nba.getFilteredDf( "Team", "Boston Celtics") # 4 Get sub-dataframe filtered by a column value

   nba2 = xlsxData() # Create the DataFrame object

   nba2.readData("./nba2.xlsx") # Read nba2.xlsx

   nba.intersectDf(nba2.data) # 5 Merge nba2 dataframe using inner join (intersection)
   
   saveDf(nba.data, "output.xlsx") # 6 Save as an excel file