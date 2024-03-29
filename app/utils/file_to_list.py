from bs4 import BeautifulSoup as soup
import json


# Pega o arquivo excel(tabela html na verdade) baixado do SGTI e transforma em uma list de dictionaries
def file_to_list(file_folder: str, xls_file_name: str, update_file: bool):

    json_file = xls_file_name.replace(".xls", ".json")
    print(json_file, update_file)

    if update_file:
        f = open(f"{file_folder}\\{xls_file_name}", "r")
        raw_file = f.read()
        print("done open and read")

        file = soup(raw_file, "lxml")
        print("parsed soup")
        h, [_, *d] = [i.text for i in file.tr.find_all("th")], [
            [i.text for i in b.find_all("td")] for b in file.find_all("tr")
        ]

        result = [dict(zip(h, i)) for i in d]
        f.close()

        # CREATES A JSON FILE FOR TESTING PURPOSES - AVOID SLOW SOUP PARSING...
        mock_data = open(f"{file_folder}\\{json_file}", "w", encoding="utf-8")
        json.dump(result, mock_data, ensure_ascii=False)
        mock_data.close()

        return result

    else:
        print("getting old json file")
        f = open(f"{file_folder}\\{json_file}", "r", encoding="utf-8")
        # result = json.load(f, encoding="utf-8-sig") - python previous versions
        result = json.load(f)
        return result
