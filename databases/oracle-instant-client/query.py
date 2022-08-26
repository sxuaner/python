# query.py

import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="/Users/xuansong/.bin/instantclient_19_8")

print("Client version: " + str(cx_Oracle.clientversion()))


# Establish the database connection
# dsn is short for data source name
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLCDB.localdomain')
conn = cx_Oracle.connect(user=r'hr', password='hr', dsn=dsn_tns)

# Obtain a cursor
cursor = conn.cursor()

# Data for binding
managerId = 145
firstName = "Peter"

# Execute the query
# The data values in managerId and firstName are ‘bound’ to the statement placeholder ‘bind variables’: mid and : fn when the statement 
# is executed. This separates the statement text from the data, which helps avoid SQL Injection security risks. Binding is also important 
# for performance and scalability.
sql = """SELECT first_name, last_name
         FROM employees
         WHERE manager_id = :mid AND first_name = :fn"""
cursor.execute(sql, mid = managerId, fn = firstName)

# Loop over the result set
for row in cursor:
    print(row)
