from backend.db import get_connection

def criar_usuario(nome, email):
    conn = get_connection()
    if not nome.strip():
        raise ValueError("Nome é obrigatório")
    if not email.strip():
        raise ValueError("Email é obrigatório")
    if "@" not in email:
        raise ValueError("Email Inválido")
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO usuarios (nome, email)
            VALUES (%s, %s)
            RETURNING id
            """,
            (nome, email)
        )

        usuario_id = cur.fetchone()[0]

    conn.commit()
    conn.close()

    return usuario_id

def listar_usuarios():
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, nome, email, ativo, data_criacao
            FROM usuarios
        """)

        usuarios = cur.fetchall()

    conn.close()

    return usuarios

def buscar_usuario(usuario_id):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, nome, email, ativo
            FROM usuarios
            WHERE id = %s
            """,
            (usuario_id,)
        )

        usuario = cur.fetchone()

    conn.close()

    return usuario

def atualizar_usuario(usuario_id, nome, email):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE usuarios
            SET nome = %s,
                email = %s
            WHERE id = %s
            """,
            (nome, email, usuario_id)
        )

    conn.commit()
    conn.close()

def deletar_usuario(usuario_id):
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM usuarios
            WHERE id = %s
            """,
            (usuario_id,)
        )

    conn.commit()
    conn.close()