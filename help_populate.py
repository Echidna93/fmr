import csv
import MySQLdb as mdb
import pandas as pd

xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/fhr_bird_survey.xlsx')
df = xl.parse('2018')

con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_birds');
cur = con.cursor()
for i in range(14, 103):
    for j in range(7, 18):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,5]) == 'nan'):
            cur.execute("SELECT common_name FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,6])])
            entries = cur.fetchone()          
           #print(entries)
            print('(' + str(entries)  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[14, j])) + ', ' +'\'2014-06-23\''+  + ')')

