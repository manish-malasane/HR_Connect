from MyPackage.csv_file import HandleCSV
from pprint import pprint


def first_task():
    data = HandleCSV.read_entire_csv()
    final_dict = {}
    j = 1
    for i in data:
        if int(i["SALARY"]) > 9000:
            final_dict[j] = {
                "Name": (i["FIRST_NAME"] + " " + i["LAST_NAME"]),
                "email": i["EMAIL"],
                "Phone": i["PHONE_NUMBER"].replace(".", ""),
            }
            j += 1
    return final_dict


if __name__ == "__main__":
    (first_task())
