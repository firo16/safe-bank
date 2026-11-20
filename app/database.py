import sqlite3


NAZWA_BAZY= 'uzytkownicy.db'

def create_tabel_users():
    with sqlite3.connect(NAZWA_BAZY) as polaczenie:
        kursor = polaczenie.cursor()

        kursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            is_active INTEGER NOT NULL DEFAULT 1
            )
        """)



def create_user(
        username:str,
        email:str,
        password_hash:str
):
    with sqlite3.connect(NAZWA_BAZY) as polaczenie:
        polaczenie.row_factory = sqlite3.Row
        kursor = polaczenie.cursor()

        kursor.execute("""
        INSERT INTO users
        (username, email, password_hash)
        VALUES(?, ?, ?)
        """,(username,email,password_hash)
        )
        user_id = kursor.lastrowid
        kursor.execute(
            """
            SELECT
            id,
            username,
            email,
            created_at,
            is_active
            FROM users
            WHERE id = ?
            """,(user_id,)
        )

        rekord = kursor.fetchone()
        user = dict(rekord)
        user["is_active"] = bool(user["is_active"])
    return user


def get_user_by_username(username:str):
    with sqlite3.connect(NAZWA_BAZY) as polaczenie:
        polaczenie.row_factory = sqlite3.Row
        kursor = polaczenie.cursor()

        kursor.execute("""
        SELECT id,
        username,
        email,
        password_hash
        FROM users
        WHERE username = ?
        """,(username,)
        )

    user = kursor.fetchone()
    if user is None:
        return None

    return dict(user)




create_tabel_users()