import csv
import MySQLdb as mdb
import pandas as pd

xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/fhr_bird_survey.xlsx')
df = xl.parse('2018')
con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_bird_data');
cur = con.cursor()
'''
for i in range(14, 150):
    for j in range(7, 47):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,j]) == 0 or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])
            
                entries = cur.fetchone()          
                print('(' + str(int(entries[0]))  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[11, j])) + ', ' + '\'2018-06-20\'' + ', ' + '\'None\'' + '),')
            except Exception as e:
                print e

'''

for i in range(12, 136):
    for j in range(50, 90):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])
            
                entries = cur.fetchone()          
                print('(' + str(int(entries[0]))  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[11, j])) + ', ' + '\'2018-06-26\'' + ', ' + '\'None\'' + '),')
            except Exception as e:
                print e

