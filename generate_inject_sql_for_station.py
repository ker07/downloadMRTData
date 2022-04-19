import pandas as pd

FILEPATH = "TaipeiMRTStationList.csv"
STATION_ADDED = []


def read_and_slice_station_csv(filepath):
    df = pd.read_csv(filepath)
    df_slice = df[["stationNameEng", "stationName", "startDate"]]

    return df_slice


def generate_station_sql_inject(column_inject, row):
    datas = ""
    data = row[1]
    datas += f"'{data['stationNameEng']}', " \
             f"'{data['stationName']}', " \
             f"'{data['startDate']}'"

    return f"INSERT INTO station ({column_inject}) VALUES ({datas});\n"


with open("SQL/InsertStationData.sql", 'w') as file:
    iter_row = read_and_slice_station_csv(FILEPATH).iterrows()
    columns = "stationNameEng, stationName, startDate"
    station_added = []
    for i in iter_row:
        if i[1]['stationName'] not in station_added:
            file.write(generate_station_sql_inject(columns, i))
            station_added.append(i[1]['stationName'])
