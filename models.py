import mysql.connector



conexao = mysql.connector.connect(
    host ='localhost',
    user='root',
    password='Wes170702',
    database='cadastro_cliente',
)

cursor = conexao.cursor()



cursor.close()
conexao.close()