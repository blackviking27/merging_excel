import numpy as np #install using cmd: pip install numpy
#we used numpy to generate arrays to maintain contious 

import pandas as pd #install using cmd: pip install pandas
#we used pandas to read the excel files into dataframes and to make operations on it

import os #inbuild module and used to get current working directory and to know list of files in directory specified


li = [] #Empty list

pat = os.getcwd() #current working directory is the search directory for the excel files
print('please place all your excel files in the directory',pat)
print("Looking for Excel files in the",pat)
savepath = pat +'\\'+'final.xlsx' 

files = os.listdir(pat) # List of files in the directory

for i in files:
    if i.endswith('.xlsx') or i.endswith('.xls') or i.endswith('.csv'):  # check whether the file is excel file
        li.append(i)

if len(li) > 0:  # checking whether atleast single excel file exists
    fpath = pat + '\\' + str(li[0])  # path of first file along with name of file
    first_df = pd.read_excel(fpath)  # Reading of first excel file into pandas dataframe

if len(li) > 1:  # Checking whether excel files exits more than 1
    for i in range(1, len(li)):
        fpath = pat+'\\'+str(li[i])  # path of each file in the directory
        temp = pd.read_excel(fpath)      # opening each file into dataframe    
        if first_df.shape[1] == temp.shape[1]:   # check the columns size of first ever dataframe and current dataframe is equal
            first_df = first_df.append(temp,ignore_index=True)  # append the current dataframe to first dataframe
        else:
            print('file name :',li[i],' Has diffrent shape in columns')

if len(li)>0:
    print(first_df)
    first_df.to_excel(savepath)  # saving dataframe to excel
    print("File saved successfully at",savepath)
else:
    print("No excel files found please copy the excel file into",pat,"\n","then re RUN the code")
