
import psycopg2
import psycopg2.extras
from config import password
hostname = 'localhost'
database = 'test'
username = 'postgres'
pwd = password
port_id = 5432

# set connection and cursor to none
conn = None
try:
    with psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
    
            # drop table if it already exists
            curs.execute('DROP TABLE IF EXISTS employee')

            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                id int PRIMARY KEY,
                name varchar(50) NOT NULL,
                salary INT,
                dept_id Varchar(30)
            )
        '''
            curs.execute(create_script)

            insert_scipt = 'INSERT INTO employee(id, name, salary, dept_id) values (%s, %s, %s, %s)'
            insert_values =[(1,'Point', 27000, 'mapping dept'), (2, 'Stun', 15000, 'geology_dept'), 
                            (3, 'Kofi',14000,'gis_dept'), (4, 'Range', 25000,'mapping'), (5, 'King',13000, 'mine_dept')]
            for value in insert_values:
                curs.execute(insert_scipt,value)

        # update the record
            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            curs.execute(update_script)   

            # delete record
            delete_script = 'DELETE FROM employee WHERE  name = %s'
            delete_value = ('Stun',)
            curs.execute(delete_script,delete_value)


            # view items in table each on it's own line
            curs.execute('SELECT * FROM employee')
            for record in curs.fetchall():
                print(record[1], record[2])

except Exception as e:
    print(e)

finally:
    if conn is not None:
        conn.close()