import psycopg2

def create_server_connection():

    PGHOST='ep-shy-queen-a2izrsqc.eu-central-1.aws.neon.tech'
    PGDATABASE='datafundamentals'
    PGUSER='datafundamentals_owner'
    PGPASSWORD='OApta9xdrRn8'

    conn = None
    try:
        conn = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=5432)
        print("Database conn successful")
    except Error as err:
        print(f"Error: '{err}'")

    return conn

connection = create_server_connection()
connection.close()

'''# CREAR TABLA
conn = create_server_connection()

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datafund_students table
try:
    cur.execute("""CREATE TABLE datafund_students(
                student_id SERIAL PRIMARY KEY,
                student_name VARCHAR (50) UNIQUE NOT NULL,
                student_email VARCHAR (100) NOT NULL,
                student_age INT NOT NULL);
                """)
    # Make the changes to the database persistent
    conn.commit()
except Error as err:
        print(f"Error: '{err}'")
        conn.rollback()

# Close cursor and communication with the database
cur.close()

#Mas ordenes...con nuevos cursores
conn.close()'''

'''# INSERT
conn = create_server_connection()

cur = conn.cursor()

cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Pedro','p@p.es',34)")
cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Anna','a@a.es',43)")
cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Luisa','l@l.es',54)")
cur.execute("INSERT INTO datafund_students(student_name, student_email, student_age) VALUES('Juan','j@j.es',21)")

conn.commit()
cur.close()
conn.close()'''

'''# SELECT
conn = create_server_connection()

cur = conn.cursor()
cur.execute('SELECT * FROM datafund_students;')
rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()

for row in rows:
    print(row)'''

# UPDATE
conn = create_server_connection()

cur = conn.cursor()
cur.execute("UPDATE datafund_students SET student_age = 23 WHERE student_name = 'Juan';")
conn.commit()
cur.close()
conn.close()

# DELETE
conn = create_server_connection()

cur = conn.cursor()
cur.execute("""DELETE from datafund_students WHERE student_name = 'Luisa'""");
conn.commit()
cur.close()
conn.close()

# JOIN
conn = create_server_connection()

cur = conn.cursor()
cur.execute("""SELECT DISTINCT p.customerNumber, p.checkNumber, p.paymentDate, p.amount FROM payments p 
LEFT JOIN sales s ON s.customerNumber=p.customerNumber WHERE s.customerNumber IS NOT NULL ORDER BY p.customerNumber""")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()