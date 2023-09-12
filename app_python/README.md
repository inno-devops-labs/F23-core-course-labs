<p align="center">

  <h3 align="center">Lab 1</h3>

  <p align="center">
    Web application displaying time in Moscow
    <br>
  </p>
</p>


## Table of contents

- [Table of contents](#table-of-contents)
- [Description](#description)
- [Quick start](#quick-start)
- [Testing](#testing)


## Description

This is a simple web application on flask. It displays current date and time in Moscow. 


## Quick start

Clone the repository

```
git clone https://github.com/JustSomeDude2001/core-course-labs
```

Navigate to the project directory

```
cd ./core-course-labs/app_python
```

Install the requirements

```
pip install -r requirements.txt
```

Run the app

```
python3 app.py
```

Afterwards, the date and time can be seen on `127.0.0.1:5000`


## Testing

After installing the application, go to the directory and run tests package using `pytest`

```
python3 -m pytest
```

Note that if your ping is higher than 2 minutes (which is highly unlikely) tests will always fail.


