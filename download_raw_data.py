import shutil
import requests
import sql_access

SOURCE_URL = "https://data.taipei/api/dataset/63f31c7e-7fc3-418b-bd82-b95158755b4d/resource/555d84c1-5a25-4644-85e2-bd1284a7482e/download"


def download_file(name, url):
    local_filename = f"raw/{name}.csv"
    print(f"Downloading {local_filename}...")
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    print(f"{local_filename} complete")
    return local_filename


def download_reference():
    print("Starting downloading reference...")
    reference_response = requests.get(SOURCE_URL,
                                      stream=True)
    print(reference_response)
    return reference_response


def loop_through_reference_and_download_csv(reference_response):
    elements = reference_response.text.split()[1:]

    for i in range(len(elements)):
        file_name = elements[i].split(",")[0]
        file_url = elements[i].split(",")[1]
        file_name_int = int(file_name)

        if file_name_int in sql_access.get_column_list_from_table("sourceurl", "month"):
            print(f"{file_name}.csv is already in database.")
        else:
            download_file(file_name, file_url)


if __name__ == '__main__':
    response = download_reference()
    loop_through_reference_and_download_csv(response)
