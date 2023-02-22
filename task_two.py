from datetime import datetime
from pprint import pprint
from MyPackage.csv_file import HandleCSV


def actual():
    content = HandleCSV.read_entire_csv()
    final_dict = {}
    for i in content:

        if 30 < int(i["DEPARTMENT_ID"]) < 110 and int(i["SALARY"]) > 4200:
            bar = i["HIRE_DATE"]

            date = datetime.strptime(bar, "%d-%b-%y")
            get_date = date.strftime("%Y-%m-%d")
            final_dict.setdefault(get_date, []).append(i["FIRST_NAME"] + " " + i["LAST_NAME"])
    return final_dict


if __name__ == "__main__":
    pprint(actual())
