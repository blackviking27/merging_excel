import numpy as np
import pandas as pd
from os import listdir
import xlrd
import os


li = []
pat = input("Enter directory of Excel file which are needed to be merged:")  # example D:\excelfolder
savepath = input('Path where the final excel file to be saved\n ex:D:\main.xlsx:')  # example D:\main.xlsx
files = listdir(pat) # List of files in the directory


for i in files:
    if i.endswith('.xlsx') or i.endswith('.xls') :  # check whether the file is excel file
        li.append(i)
fpath = pat + '\\' + str(li[0])  # path of first file along with name of file


if len(li) > 0:  # checking whether atleast single file exists
    first_df = pd.read_excel(fpath)  # Reading of first excel file into pandas dataframe
    l = f = len(first_df)  # length of dataframe used to maintain continuous index for every excel sheet

if len(li) > 1:  # Checking whether excel files exits more than 1

    for i in range(1, len(li)):
        fpath = pat+'\\'+str(li[i])  # path of each file in the directory
        temp = pd.read_excel(fpath)
        # opening each file into dataframe

        if first_df.shape[1] == temp.shape[1]:  # check the columns size of first ever dataframe and current dataframe is equal
            temp.index = np.arange(f, f+l)  # changing the current dataframe index that continues the previous dataframe
            # initially f is len of first dataframe
            
            f += l  # increase f by len of dataframe to continue the index for next excel files
            first_df = first_df.append(temp)  # append the current dataframe to first dataframe

print(first_df)
first_df.to_excel(savepath)  # saving dataframe to excel
print("File saved successfully at",savepath)