import psycopg2
import random
dbconfig = {'host': 'localhost',
            'user': 'postgres',
            'port': '5432',
            'password': 'postgres',
            'database': 'bank', }

conn = psycopg2.connect(**dbconfig)

cur = conn.cursor()
i = 13
month=1
day=1
while i <= 2000000:
    id=i
    month = random.randint(1, 7)
    day = str(random.randint(1, 28))
    # if len(day)== 1:
    #     day="0"+day
    save = "UPDATE transactions SET transaction_time='2021-"+str(month)+"-"+day+"' WHERE transaction_id="+str(id)

    cur.execute(save)
    conn.commit()
    i += 1
cur.close()
conn.close()
