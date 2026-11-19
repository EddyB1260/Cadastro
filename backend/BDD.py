from dotenv import load_dotenv
import os
import psycopg

load_dotenv()

conn = psycopg.connect(
    dbname="postgres",  # banco padrão que já existe
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)

conn.autocommit = True

with conn.cursor() as cur:
    cur.execute("CREATE DATABASE cadastro_usuarios")

print("Banco criado com sucesso!")

conn.close()