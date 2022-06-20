import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="url_shortner"
)

mycursor = mydb.cursor()
# mycursor.execute("SELECT short_url FROM urlshort WHERE short_url='ASASA';")

# myresult = mycursor.fetchall()
# if len(myresult) == 0:
#     print("No results found in DB for short URL")
# else:
#     for x in myresult:
#         s_u = x[0]
#         print(s_u)