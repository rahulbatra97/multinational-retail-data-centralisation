#pip install psycopg2
import psycopg2

# Database connection details
host = "database-1.coddpaqo7juo.eu-north-1.rds.amazonaws.com"
port = "5432"
database = "postgres"
user = "postgres"
password = "#Thepearhouse1"

# Establish the connection
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
cursor = conn.cursor()


#showing the contents of table "employee"

select_query = "SELECT * FROM employee"
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()