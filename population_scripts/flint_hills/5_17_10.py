import csv
import MySQLdb as mdb
import pandas as pd

xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/fhr_bird_survey.xlsx')
df = xl.parse('2011')
con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_bird_data');
cur = con.cursor()

for i in range(6, 107):
    for j in range(84, 101):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,j]) == 0 or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])
            
                entries = cur.fetchone()          
                print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[6, j])) + ', ' + '\'2011-06-28\'' + ', ' + '\'5 min, <= 50m\'' + '),')
            except Exception as e:
                pass

