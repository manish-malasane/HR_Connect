## Visit this URL :-> https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784

```                               
                                      *** TASK 1 ***

Write a program to get details of employees who's salary is > 9000. The output should be in 
following format :->
                            {
                                "Name": "<first_name last_name>",
                                "email": "<email>",
                                "phone number": "<phone number without DOT>"
                            }
```

```
                                     *** TASK 2 ***
                                    
Write a program to get "HIRE DATE" of employee who's department is within range 30 to 110 AND who's salary is > 4200.
The output should be in following format :-> 
                                         {
                                           "<HIRE DATE in YYYY-MM-DD format>": [
                                           "<first_name last_name>", ...,
                                            "<first_name last_name>"],
                                         }
```

# Project Structure
- HR_Connect (Project Root)
    - task_one.py (entry point for task_one)
    - task_two.py (entry point for task_two)
    - MyPackage (Custom Package)
        - __init__.py
        - csv_file.py (csv file related operations)
    - README.md (Documentation of project)
    - venv (to keep dependencies of project)
