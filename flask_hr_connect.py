from flask import Flask, render_template

from task_one import first_task
from task_two import second_task


app = Flask(__name__)


@app.route("/hr/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/hr/one")
def task_one():
    return render_template("one.html", emp_data=first_task())


@app.route("/hr/two")
def task_two():
    return render_template("two.html", final_dict=second_task())
