import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=172.17.170.121,1433;"
    "DATABASE=registro_horas;"
    "UID=app_python_registro;"
    "PWD=PruebaDePython23;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT @@SERVERNAME, DB_NAME()")
print(cursor.fetchone())
