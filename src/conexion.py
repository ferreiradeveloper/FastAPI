import cx_Oracle

try:
    connection = cx_Oracle.connect(
        user = 'system',
        password = 'pefeto68',
        dsn='localhost:1521/xe',
        encoding = 'UTF-8'
    )
    print(connection.version)
    cursor=connection.cursor()
    cursor.execute("insert into tabla_test values (5,'Ambrocio','Pancracio')")
    cursor.execute("select * from tabla_test")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("coneccion finalizada")


