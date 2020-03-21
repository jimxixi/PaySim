
import sqlite3
import time
import uuid

db = sqlite3.connect(r"C:\Users\admin\Desktop\jdf\PaySim\PaySim.db")
cursor = db.cursor()

cursor.execute("select * from transaction_table")
result = cursor.fetchall()

for line in result:
    print(line)

cursor.execute("select accountBalance from account_table")
result = cursor.fetchone()
for line in result:
    print(line)
cursor.close()
db.close()

def makeTimeStamp() -> str:
    return str(int(1000 * time.time()))

def makeUUID() -> str:
    return uuid.uuid4()

print(makeTimeStamp())
print(makeUUID())
print(makeUUID())
print(makeUUID())
print(makeUUID())
