import pandas as pd


'''
This program compares 2 excel files to check for duplicates. It the creates one excel file for downloads and loads the missing rows to the master file
'''
def checker(master,new):
    df1 = pd.read_excel(master)
    df2 = pd.read_excel(new)

    print(df1.head())
    print(df2.head())

    df1.drop_duplicates(inplace=True)
    df2.drop_duplicates(inplace=True)

    df_diff = df2[~ df2["id"].isin(df1["id"])]

    writer = pd.ExcelWriter(new, engine='xlsxwriter',options={'strings_to_urls': False})
    df_diff.to_excel(writer,index=False)
    writer.close()

    updated_master = df1.append(df_diff, ignore_index=True)
    writer = pd.ExcelWriter(r'master_file.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
    updated_master.to_excel(writer,index=False)
    writer.close()

checker('master_file.xlsx','model.xls')

    # print(df_diff.head())

    # index1 = df1.index
    # index2 = df2.index
    # index3 = df_diff.index

    # number_of_rows_df1 = len(index1)
    # number_of_rows_df2 = len(index2)
    # number_of_rows_df_diff = len(index3)

    # print(f"master has {number_of_rows_df1}")
    # print(f"new has {number_of_rows_df2}")
    # print(f"diff has {number_of_rows_df_diff}")

    # writer = pd.ExcelWriter(r'master_file.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
    # df.to_excel(writer)
    # writer.close()