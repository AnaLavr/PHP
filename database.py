import sqlite3
import pyodbc
  
def query(query_text, *param):
    conn=sqlite3.connect('helppeople.db') 
    cur=conn.cursor()
    cur.execute (query_text,param)
    
    column_names=[]
    for  column in cur.description:
       column_names.append(column[0])
       print (column_names)
        
    rows=cur.fetchall()
    dicts=[]
    
    for row in rows:
       d=dict(zip(column_names,row ))
       dicts.append(d)
        
    conn.close()
    return dicts

def get_inbox_messages(ID):
    return query ('''SELECT DISTINCT * FROM MSG where to_user = ? order by date_time DESC LIMIT (SELECT count(DISTINCT subject_text) from MSG where to_user = ?)''', ID, ID)

#('''SELECT members.first_name, members.Last_name,members.profile_photo, MSG.message_text, MSG.subject_text,
     #             MSG.datetime  FROM MSG INNER JOIN members ON members.ID=MSG.from_user WHERE to_user=?''',ID)
def conversation(ID):
    return query     ('''SELECT MSG.to_user, MSG.from_user, MSG.message_text,MSG.subject_text, MSG.msg_id, MSG.date_time , members.ID FROM MSG 
                            INNER JOIN  members ON  members.ID=MSG.from_user 
                            OR members.ID=MSG.to_user 
                            WHERE ID=3
                            ORDER BY   subject_text, date_time DESC ''')
                            
    
def members(ID):
    return query('''SELECT * FROM members WHERE ID=?''', ID  )



# is ID automatic? 
def create_member(first_name,Last_name,  age, city,mode, email,password, profile_photo, phone_number ):      
    conn=sqlite3.connect('helppeople.db') 
    cur=conn.cursor()
     
    result=cur.execute('''INSERT INTO members ([first_name],[Last_name],[age],[city],[email],[password],[profile_photo],[phone_number])
                            VALUES(?,?,?,?,?,?,?,?)''',first_name,Last_name,  age, city,mode, email,password, profile_photo, phone_number )
    conn.commit()
    print(result)
    




    
    
#INSERTING DATA TO SQL 
#Connecting to sqlite
##conn = sqlite3.connect('helppeople.db')
#Creating a cursor object using the cursor() method
##cursor = conn.cursor()
# Preparing SQL queries to INSERT a record into the database.
##cursor.execute('''INSERT INTO helpers( Helper_name, age, city, category,email, password ) 
               ##VALUES ( 'Liz ', 27, 'MOW', 'helpee','liz27@gmail.com', 'coucou')''')

# Commit your changes in the database
##conn.commit()
#print("Records inserted........")

# Closing the connection
##conn.close()