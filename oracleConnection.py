'''
Fernando Piccini - 01/2020
Python connection example with Oracle using cx_Oracle
cx_Oracle is a Python extension module that enables access to Oracle Database.
'''
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r'C:\oracle\instantclient_19_10')

dsn_tns = cx_Oracle.makedsn(ip, porta, service_name='orcl')
conn = cx_Oracle.connect(user=r'user_name', password='password', dsn=dsn_tns)

cursor = conn.cursor()
cursor.execute('select atributo from tabela ')

for row in cursor:
    print(row[0], ': ', row[1])

cursor.close()
conn.close()