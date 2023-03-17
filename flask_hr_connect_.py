from flask import Flask
from MyPackage.csv_file import HandleCSV
from datetime import datetime

app = Flask(__name__)


@app.route("/task_one")
def first_task():
    data = HandleCSV.read_entire_csv()
    final_dict = {}
    j = 1
    for i in data:
        if int(i["SALARY"]) > 9000:
            final_dict[j] = {
                "Name": (i["FIRST_NAME"] + " " + i["LAST_NAME"]),
                "Email": i["EMAIL"],
                "Phone": i["PHONE_NUMBER"].replace(".", ""),
            }
            j += 1
    return final_dict


@app.route("/task_two")
def second_task():
    content = HandleCSV.read_entire_csv()
    final_dict = {}
    for i in content:
        if 30 < int(i["DEPARTMENT_ID"]) < 110 and int(i["SALARY"]) > 4200:
            bar = i["HIRE_DATE"]

            date = datetime.strptime(bar, "%d-%b-%y")
            get_date = date.strftime("%Y-%m-%d")
            final_dict.setdefault(get_date, []).append(
                i["FIRST_NAME"] + " " + i["LAST_NAME"]
            )
    return final_dict
