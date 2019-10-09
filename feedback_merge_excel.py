# If you are using any third party modules, it is good practice to specify the ones that are being used and
# also the commands to install those modules would be helpful for someone using your code.
# numpy/pandas/xlrd in this case
import numpy as np
import pandas as pd
from os import listdir # duplicate transitive import 'listdir', can use os.listdir if 'os' module is being imported
import xlrd
import os # os module is imported, but never used ==> Un-used import statement, can be removed


li = []
# If we give user the choice to enter the directory, it is highly likely that user might enter something which is not valid
# For example, the directory which does not exist (or) typo in directory name/path
# In such cases, the program ends abruptly, which should be avoided
# It is recommended to specify a directory explicitly and ask user to place all the files inside that directory inorder to use
# this script.
# Also, the output file should also be specified so that user can look at that file after the job is done
pat = './'#input("Enter directory of Excel file which are needed to be merged:")  # example D:\excelfolder
savepath = pat + '/final.xlsx' #input('Path where the final excel file to be saved\n ex:D:\main.xlsx:')  # example D:\main.xlsx
print(pat, savepath)
files = listdir(pat) # List of files in the directory
print(files)

# Should support .csv files as well
for i in files:
    if i.endswith('.xlsx') or i.endswith('.xls'):  # check whether the file is excel file
        li.append(i)
# What if there is no excel file in the given directory ?
# The below line would throw an error, fix this
fpath = pat + '\\' + str(li[0])  # path of first file along with name of file


if len(li) > 0:  # checking whether atleast single file exists
    first_df = pd.read_excel(fpath)  # Reading of first excel file into pandas dataframe
    l = f = len(first_df)  # length of dataframe used to maintain continuous index for every excel sheet

if len(li) > 1:  # Checking whether excel files exits more than 1

    for i in range(1, len(li)):
        fpath = pat+'\\'+str(li[i])  # path of each file in the directory
        temp = pd.read_excel(fpath)
        # opening each file into dataframe

        # f and l are not defined in this scope
        # first_df is not defined in this scope
        if first_df.shape[1] == temp.shape[1]:  # check the columns size of first ever dataframe and current dataframe is equal
            temp.index = np.arange(f, f+l)  # changing the current dataframe index that continues the previous dataframe
            # initially f is len of first dataframe
            
            f += l  # increase f by len of dataframe to continue the index for next excel files
            first_df = first_df.append(temp)  # append the current dataframe to first dataframe

# What if there are no excel files present in the given directory ?
# The variable 'first_df' is undefined and the program would throw an error, fix this
print(first_df)
first_df.to_excel(savepath)  # saving dataframe to excel
print("File saved successfully at",savepath)

# Overall comments:
# Variable names can be better
# The code itself should be understandable by having a look at it, the aim should be 
# 'Writing the code which needs no documentation'
