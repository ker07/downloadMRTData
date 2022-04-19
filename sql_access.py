import psycopg2

DBNAME = "taipeimrtdata"
USER = "mikelee"


def create_psql_connection(dbname, user):
    conn = psycopg2.connect(dbname=dbname, user=user)
    cur = conn.cursor()

    return conn, cur


def close_psql_connection(curser, connection):
    curser.close()
    connection.close()


def get_column_list_from_table(table, column):
    conn, cur = create_psql_connection(DBNAME, USER)

    cur.execute(f"SELECT {column} FROM {table};")
    source_list = [element[0] for element in cur]

    close_psql_connection(cur, conn)

    return source_list
