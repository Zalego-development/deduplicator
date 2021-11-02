import os
import pandas as pd

'''
This program helps merge all excel files in a directory into a single excel file.
It uses the pandas package
'''

# files = os.listdir('files')  
# df = pd.DataFrame()
# for file in files:
#     if file.lower().endswith(('.xlsx','.xls')):
#         df = df.append(pd.read_excel(file), ignore_index=True) 
# df.head() 
# df.to_excel('master_file.xlsx')

def combine_files(directory):
    df = pd.DataFrame()
    for file in os.listdir(directory):
        if file.lower().endswith(('.xlsx','.xls')):
            path = os.path.join(directory, file)
            df = df.append(pd.read_excel(path), ignore_index=True) 
    df.head() 
    # df.to_excel('master_file.xlsx')
    writer = pd.ExcelWriter(r'master_file.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
    df.to_excel(writer,index=False)
    writer.close()

combine_files('files')