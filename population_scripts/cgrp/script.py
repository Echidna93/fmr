import csv
import MySQLdb as mdb
import pandas as pd


kval=[
        {0 : "5 mn <= 50m"},
        {1 : "5 mn > 50 m"},
        {2 : "Addtl 3 mn <= 50m"},
        {3 : "Addtl 3 mn > 50m"}
]


xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/cgrp_bird_survey_data.xlsx')
df = xl.parse('Data')

con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_birds');
cur = con.cursor()
c = 0

for i in range(4, 39):
    for j in range(6, 41):
    #for j in range(54, 98):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,3]) == 'nan'):
            #print(df.iloc[i,5])
            cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,6])])
            #print(cur.fetchone())
            entries = cur.fetchone()
            #print(df.iloc[i,5])
            print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' +  str(int(df.iloc[3,j])) + ', ' +'\'2018-06-25\'' + ', ' +  "'"+ str(kval[c][c]) + "'" + '),')
        if c == 3:
            c = 0 
        else:
            c += 1
