# myscript.py

import cx_Oracle

# Use following command to initialize lib dir.
cx_Oracle.init_oracle_client(lib_dir="/Users/xuansong/.bin/instantclient_19_8")

# http://www.dominicgiles.com/blog/files/a4698a719e20e8b3b9542ed43d51e0a2-178.html
# dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name')  
# conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns) 
# Read how to find SERVER_NAME with sql
# select value from v$parameter where name like '%service_name%';
# https: // www.stechies.com/difference-between-oracle-sids-and-oracle-service-names/

print("Client version: " + str(cx_Oracle.clientversion()))

dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLCDB.localdomain')
conn = cx_Oracle.connect(user=r'hr', password='hr', dsn=dsn_tns)

print("Connection version:"+ conn.version)

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
# connection = cx_Oracle.connect("hr", "hr", "localhost/ORCLCDB")

# cursor()??
cursor = conn.cursor()
cursor.execute("""
        SELECT first_name, last_name
        FROM employees
        WHERE department_id = :did AND employee_id > :eid""",
        did = 50,
        eid = 190)

for fname, lname in cursor:
    print("Values:", fname, lname)
