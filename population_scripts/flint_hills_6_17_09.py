import csv
import MySQLdb as mdb
import pandas as pd

xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/fhr_bird_survey.xlsx')
df = xl.parse('6-17-09')

con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_bird_data');
cur = con.cursor()
for i in range(1, 97):
    for j in range(7, 19):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])
            
                entries = cur.fetchone()          
                print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[2, j])) + ', ' + '\'2009-06-11\'' + ', ' + '\'5 min, within 50m\'' + '),')
            except Exception as e:
                pass


'''
for i in range(3, 103):
    for j in range(20, 32):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])

                entries = cur.fetchone()
                print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[2, j])) + ', ' + '\'2009-06-11\'' + ', ' + '\'5 min, > 50m\'' + ')' + ',')
            except Exception as e:
                pass

for i in range(3, 103):
    for j in range(34, 46):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])
            
                entries = cur.fetchone()          
                print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[2, j])) + ', ' + '\'2009-06-11\'' + ', ' + '\'addtnal, within 50m\'' + '),')
            except Exception as e:
                pass

for i in range(3, 103):
    for j in range(48, 60):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])

                entries = cur.fetchone()
                print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[2, j])) + ', ' + '\'2009-06-11\'' + ', ' + '\'addtnl 3 min, >50m\'' + '),')
            except Exception as e:
                pass
'''
