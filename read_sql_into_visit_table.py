import sql_access

source_list = sql_access.get_column_list_from_table("sourceurl", "month")

for month in source_list:
    conn, cur = sql_access.create_psql_connection(sql_access.DBNAME, sql_access.USER)
    filepath = f"raw/output/{month}ToVisitData.sql"

    with open(filepath, 'r') as file:
        print(f"Start Executing Injection of {month}")
        for line in file:
            cur.execute(f"{line}")
            conn.commit()
        print(f"Injection of {month} complete!")

    sql_access.close_psql_connection(curser=cur, connection=conn)
