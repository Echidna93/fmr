import csv
import MySQLdb as mdb
import pandas as pd


#mutable data
'''
+-----------------------+---------------+------+-----+---------+----------------+
| Field                 | Type          | Null | Key | Default | Extra          |
+-----------------------+---------------+------+-----+---------+----------------+
| bird_id               | int(11)       | YES  | MUL | NULL    |                |
| num_birds             | int(11)       | YES  |     | NULL    |                |
| point_num             | int(11)       | YES  |     | NULL    |                |
| survey_date           | date          | YES  |     | NULL    |                |
| distance_time_of_call | varchar(1080) | YES  |     | NULL    |                |
| id                    | int(11)       | NO   | PRI | NULL    | auto_increment |
+-----------------------+---------------+------+-----+---------+----------------+

'''

xl = pd.ExcelFile('/home/alex/python_projects/fmr/spreadsheets/fhr_bird_survey.xlsx')
df = xl.parse('2010')
con = mdb.connect('localhost', 'root', 'edinburgh', 'fmr_birds');
cur = con.cursor()

mutbl_data = [
('coye', 1, 7),
('sosp', 1, 9),
('fisp', 1, 10),
('coye', 1, 10),
('amgo', 1, 10)
]


for i in mutbl_data:
        cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s OR common_name LIKE %s;", [i[0],i[0]])
        bird_id = cur.fetchone() 
        print('(' + str(bird_id[0]).upper()  + ', ' +  str(i[1]) + ', ' + str(i[2]) + ', ' + '\'2014-06-23\'' + ', ' + '\' adtnl 3m, > 50m\'' + '),')

'''
for i in range(7, 135):
    for j in range(7, 11):
        if not (str(df.iloc[i,j]) == 'nan' or str(df.iloc[i,j]) == 0 or str(df.iloc[i,4]) == 'nan'):
            try:
                cur.execute("SELECT bird_id FROM mn_birds WHERE species_code LIKE %s OR common_name LIKE %s;", [str(df.iloc[i,5]),str(iloc[i,4])])
            
                entries = cur.fetchone()          
                print('(' + str(entries[0])  + ', ' +  str(int(df.iloc[i,j])) + ', ' + str(int(df.iloc[6, j])) + ', ' + '\'2010-05-17\'' + ', ' + '\'5 min <= 50m\'' + '),')
            except Exception as e:
                pass
                '''
