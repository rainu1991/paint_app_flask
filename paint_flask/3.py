import psycopg2
con = psycopg2.connect(database='rainu')    
cur=con.cursor()   
cur.execute("CREATE TABLE paintrs(id serial,name TEXT,data TEXT)")
con.commit()
con.close()
