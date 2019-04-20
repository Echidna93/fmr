import csv
import MySQLdb as mdb
import pandas as pd

xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/fhr_bird_survey.xlsx')
df = xl.parse('2010')
con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_bird_data');
cur = con.cursor()

mutbl_data = [('YTVI', 1, 3)
]





for i in mutbl_data:
        cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [i[0]])
        bird_id = cur.fetchone() 
        print('(' + str(bird_id[0])  + ', ' +  str(i[1]) + ', ' + str(i[2]) + ', ' + '\'2010-06-30\'' + ', ' + '\'adtnl 3 min, > 50m\'' + '),')



'''
for i in range(7, 105):
    for j in range(3, 19):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,j]) == 0 or str(df.iloc[i,5]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s;", [str(df.iloc[i,5])])
            
                entries = cur.fetchone()          
                print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[6, j])) + ', ' + '\'2010-05-17\'' + ', ' + '\'5 min, within 50m\'' + '),')
            except Exception as e:
                pass
'''
