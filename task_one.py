from MyPackage.csv_file import HandleCSV
from pprint import pprint


def first_task():
    data = HandleCSV.read_entire_csv()
    final_dict = {}
    for i in data:
        if int(i["SALARY"]) > 9000:
            number = str(i["PHONE_NUMBER"]).split(".")
            number = "".join(number)
            final_dict["Name"] = i["FIRST_NAME"] + " " + i["LAST_NAME"]
            final_dict["email"] = i["EMAIL"]
            final_dict["phone number"] = number
            pprint(final_dict)


if __name__ == "__main__":
    (first_task())
