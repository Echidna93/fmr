import csv
import MySQLdb as mdb
import pandas as pd


kval=[
        {0 : "5 mn <= 50m"},
        {1 : "5 mn > 50 m"},
        {2 : "Addtl 3 mn <= 50m"},
        {3 : "Addtl 3 mn > 50m"}
]


xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/fhr_bird_survey.xlsx')
df = xl.parse('2016')

con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_birds');
cur = con.cursor()
c = 0

for i in range(12, 129):
    for j in range(7, 49):
    #for j in range(54, 98):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,4]) == 'nan'):
            #print(df.iloc[i,5])
            cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])
            #print(cur.fetchone())
            entries = cur.fetchone()
            #print(df.iloc[i,5])
            print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' +  str(int(df.iloc[11,j])) + ', ' +'\'2017-06-12\'' + ', ' +  "'"+ str(kval[c][c]) + "'" + '),')
        if c == 3:
            c = 0 
        else:
            c += 1
