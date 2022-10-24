import os
from datetime import datetime, timedelta


def check_data_updates(model, sgti_file_folder):

    file_name = model["file_names"]["xls_file"]
    file_path = f"{sgti_file_folder}\\{file_name}"

    if os.path.exists(file_path):
        xls_timestamp = os.path.getmtime(file_path)
        m_time = datetime.fromtimestamp(xls_timestamp)
        today = datetime.now()

        one_day_old = today - m_time > timedelta(hours=8)
        print("one_day_old: " + str(one_day_old))
        return one_day_old
    else:
        return True
