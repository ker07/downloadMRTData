import pandas as pd

FILEPATH = "TaipeiMRTStationList.csv"
STATION_ADDED = []


def read_and_slice_station_csv(filepath):
    df = pd.read_csv(filepath)
    df_slice = df[["stationCode", "metroLineCode", "stationName"]]

    return df_slice


def generate_station_sql_inject(column_inject, row):
    datas = ""
    data = row[1]
    datas += f"'{data['stationCode']}', " \
             f"'{data['metroLineCode']}', " \
             f"'{data['stationName']}'"

    return f"INSERT INTO stationCode ({column_inject}) VALUES ({datas});\n"


with open("SQL/InsertStationCodeData.sql", 'w') as file:
    iter_row = read_and_slice_station_csv(FILEPATH).iterrows()
    columns = "stationCode, metroLineCode, stationName"
    for i in iter_row:
        file.write(generate_station_sql_inject(columns, i))