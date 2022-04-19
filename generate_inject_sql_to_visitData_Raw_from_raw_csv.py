import datetime
import pandas as pd
import sql_access


def get_unique_pairs_of_entry_and_exit(path):
    csv_chunk_reader = pd.read_csv(path,
                                   chunksize=40000)

    df = csv_chunk_reader.get_chunk()
    return len(df.groupby(['進站', '出站']))


def generate_dictionary_for_creating(path):
    chunk_reader = pd.read_csv(path,
                               chunksize=get_unique_pairs_of_entry_and_exit(path))

    date_location_visit_dict = {}

    for chunk in chunk_reader:
        for row in chunk.itertuples(index=False):
            key_for_dict = (row[0], row[2], row[3])

            if key_for_dict not in date_location_visit_dict.keys():
                date_location_visit_dict[key_for_dict] = [(row[1], row[4])]
            else:
                date_location_visit_dict[key_for_dict].append((row[1], row[4]))

    return date_location_visit_dict


def generate_insert_string_for_visits_data_raw(date_station_in_station_out, hour_visit_tuple):
    columns = "date, dayOfWeek, station_in, station_out"
    datas = ""

    datas += f"'{date_station_in_station_out[0]}'::DATE, " \
             f"{datetime.datetime.strptime(date_station_in_station_out[0], '%Y-%m-%d').strftime('%w')}, " \
             f"'{date_station_in_station_out[1]}', " \
             f"'{date_station_in_station_out[2]}'"

    daily_sum_hour = 0
    for hour in hour_visit_tuple:
        columns += f", visit_hour_{hour[0]}"
        datas += f", {hour[1]}"
        daily_sum_hour += hour[1]
    datas += f", {daily_sum_hour}"

    return f"INSERT INTO visitsData_raw ({columns}, visitAllDay) VALUES ({datas});\n"


def loop_through_dictionary_and_write_sql_file(filepath, dictionary):
    with open(f"{filepath[:-10]}output/{filepath[-10:].strip('.csv')}ToVisitData.sql", 'w') as file:
        for date_stationIn_stationOut, hour_visit_tuple in dictionary.items():
            string_to_write = generate_insert_string_for_visits_data_raw(date_stationIn_stationOut, hour_visit_tuple)
            file.write(string_to_write)
    print(f"{filepath[-10:].strip('.csv')}ToVisitData.sql created!")


def mrt_csv_path_to_sql_file(path):
    dictionary = generate_dictionary_for_creating(path)
    loop_through_dictionary_and_write_sql_file(path, dictionary)


if __name__ == "__main__":
    source_list = sql_access.get_column_list_from_table("sourceurl", "month")

    for month in source_list:
        filepath = f"raw/{month}.csv"
        mrt_csv_path_to_sql_file(filepath)
