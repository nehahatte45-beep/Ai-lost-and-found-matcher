import sqlite3


def create_table():

    con = sqlite3.connect("lost_found.db")

    con.execute("""
        CREATE TABLE IF NOT EXISTS items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            name TEXT,
            description TEXT,
            location TEXT,
            date TEXT,
            contact TEXT
        )
    """)

    con.commit()
    con.close()


def add_item(
    item_type,
    name,
    description,
    location,
    date,
    contact
):

    con = sqlite3.connect("lost_found.db")

    con.execute("""
        INSERT INTO items(
            type,
            name,
            description,
            location,
            date,
            contact
        )
        VALUES(?,?,?,?,?,?)
    """, (
        item_type,
        name,
        description,
        location,
        date,
        contact
    ))

    con.commit()
    con.close()


def get_items(item_type):

    con = sqlite3.connect("lost_found.db")

    data = con.execute(
        "SELECT * FROM items WHERE type=?",
        (item_type,)
    ).fetchall()

    con.close()

    return data