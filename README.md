# too-do_app

 assignment of too do app

## Commands on terminal

## First Day work

(base) PS C:\Users\Batch 37 PIAIC> cd generative-ai
(base) PS C:\Users\Batch 37 PIAIC\generative-ai> dir

    Directory: C:\Users\Batch 37 PIAIC\generative-ai

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         1/29/2024   1:25 PM                .mypy_cache
d-----         3/25/2024   1:44 AM                assignment
d-----         3/22/2024  10:20 PM                generative-ai
d-----         1/29/2024   3:41 PM                hello world
d-----         3/22/2024  11:56 PM                learn-generative-ai
d-----         3/23/2024  10:47 PM                modren_python
-a----         1/28/2024  11:54 PM          83715 setting environment.ipynb

(base) PS C:\Users\Batch 37 PIAIC\generative-ai> cd assignment
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment> dir

    Directory: C:\Users\Batch 37 PIAIC\generative-ai\assignment

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         3/25/2024   1:46 AM                too-do_app

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment> cd too-do_app
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> dir

    Directory: C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         3/25/2024   1:46 AM                too-do_app

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> dir

    Directory: C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         3/25/2024   1:46 AM             66 .gitattributes
-a----         3/25/2024   1:46 AM             40 README.md

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry --version

The command "—-version" does not exist.

Did you mean this?
    version
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry version

Poetry could not find a pyproject.toml file in C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app or its parents
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> cd..
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment> poetry new too-do_app

Destination C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app exists and is not empty
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment> poetry new too-do_app
Created package too_do_app in too-do_app
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment> cd too-do_app
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> dir

    Directory: C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         3/25/2024   1:55 AM                tests
d-----         3/25/2024   1:55 AM                too_do_app
-a----         3/25/2024   1:46 AM             66 .gitattributes
-a----         3/25/2024   1:55 AM            285 pyproject.toml
-a----         3/25/2024   1:46 AM             40 README.md

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run python --version
Creating virtualenv too-do-app-sXrxilcL-py3.12 in C:\Users\Batch 37 PIAIC\AppData\Local\pypoetry\Cache\virtualenvs
Python 3.12.2
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry env list
too-do-app-sXrxilcL-py3.12 (Activated)
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry add requests
Using version ^2.31.0 for requests

Updating dependencies
Resolving dependencies... (0.9s)

Package operations: 5 installs, 0 updates, 0 removals

- Installing certifi (2024.2.2)
- Installing charset-normalizer (3.3.2)
- Installing idna (3.6)
- Installing urllib3 (2.2.1)
- Installing requests (2.31.0)

Writing lock file
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry add pytest
Using version ^8.1.1 for pytest

Updating dependencies
Resolving dependencies... (0.8s)

Package operations: 5 installs, 0 updates, 0 removals

- Installing colorama (0.4.6)
- Installing iniconfig (2.0.0)
- Installing packaging (24.0)
- Installing pluggy (1.4.0)
- Installing pytest (8.1.1)

Writing lock file
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run python ./too-do_app/main.py
C:\Python312\python.exe: can't open file 'C:\\Users\\Batch 37 PIAIC\\generative-ai\\assignment\\too-do_app\\too-do_app\\main.py': [Errno 2] No such file or directory
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run python too-do_app.main.py
C:\Python312\python.exe: can't open file 'C:\\Users\\Batch 37 PIAIC\\generative-ai\\assignment\\too-do_app\\too-do_app.main.py': [Errno 2] No such file or directory
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> dir

    Directory: C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         3/25/2024   2:03 AM                tests
d-----         3/25/2024   2:00 AM                too_do_app
-a----         3/25/2024   1:46 AM             66 .gitattributes
-a----         3/25/2024   1:59 AM          20200 poetry.lock
-a----         3/25/2024   1:59 AM            326 pyproject.toml
-a----         3/25/2024   1:46 AM             40 README.md

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry version
too-do-app 0.1.0
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run python too_do_app.main.py
C:\Python312\python.exe: can't open file 'C:\\Users\\Batch 37 PIAIC\\generative-ai\\assignment\\too-do_app\\too_do_app.main.py': [Errno 2] No such file or directory
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run python ./too_do_app/main.py
Hello World
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run pytest
================================================= test session starts =================================================
platform win32 -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0
rootdir: C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app
configfile: pyproject.toml
collected 0 items / 1 error

======================================================= ERRORS ========================================================
______________________________________ ERROR collecting tests/test_myproject.py _______________________________________
ImportError while importing test module 'C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app\tests\test_myproject.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Python312\Lib\importlib\__init__.py:90: in import_module
    return_bootstrap._gcd_import(name[level:], package, level)
tests\test_myproject.py:1: in ## <module>
    from project_001 import main
E   ModuleNotFoundError: No module named 'project_001'
=============================================== short test summary info ===============================================
ERROR tests/test_myproject.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
================================================== 1 error in 0.39s ===================================================
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run pytest
================================================= test session starts =================================================
platform win32 -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0
rootdir: C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app
configfile: pyproject.toml
collected 2 items

tests\test_myproject.py ..                                                                                       [100%]

================================================== 2 passed in 0.05s ==================================================
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app>

## Second Day work

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry version
too-do-app 0.1.0
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run python --version
Python 3.12.2
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry add fastapi "uvicorn[standard]"
Using version ^0.110.0 for fastapi
Using version ^0.29.0 for uvicorn

Updating dependencies
Resolving dependencies... (16.1s)

Package operations: 16 installs, 0 updates, 0 removals

- Installing sniffio (1.3.1)
- Installing typing-extensions (4.10.0)
- Installing annotated-types (0.6.0)
- Installing anyio (4.3.0)
- Installing pydantic-core (2.16.3)
- Installing click (8.1.7)
- Installing h11 (0.14.0)
- Installing pydantic (2.6.4)
- Installing python-dotenv (1.0.1)
- Installing pyyaml (6.0.1)
- Installing starlette (0.36.3)
- Installing watchfiles (0.21.0)
- Installing websockets (12.0)
- Installing fastapi (0.110.0)
- Installing uvicorn (0.29.0)

Writing lock file
(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry add sqlmodel
Using version ^0.0.16 for sqlmodel

Updating dependencies
Resolving dependencies... (3.1s)

Package operations: 3 installs, 0 updates, 0 removals

- Installing greenlet (3.0.3)
- Installing sqlalchemy (2.0.29)
- Installing sqlmodel (0.0.16)

Writing lock file

PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> pip install todo
Collecting todo
  Downloading todo-0.1.tar.gz (2.1 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: todo
  Building wheel for todo (pyproject.toml) ... done
  Created wheel for todo: filename=todo-0.1-py3-none-any.whl size=2671 sha256=6df0f74d362724c027d5ed0dd9e753c53f0ce0ce824573a9012a870e7812e0d5
  Stored in directory: c:\users\batch 37 piaic\appdata\local\pip\cache\wheels\0f\6e\a4\849e1c5a38e32ace6f07eba948b4dd261887768ff05b452db2
Successfully built todo
Installing collected packages: todo
Successfully installed todo-0.1

## Third Day work

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> ls

    Directory: C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app

Mode                 LastWriteTime         Length Name
d-----         3/27/2024   9:31 PM                .mypy_cache
d-----         3/25/2024   2:06 AM                .pytest_cache
d-----         3/25/2024   2:08 AM                tests
d-----         3/25/2024   2:17 AM                too_do_app
-a----         3/25/2024   1:46 AM             66 .gitattributes
-a----         3/26/2024  12:58 AM         103606 poetry.lock
-a----         3/26/2024   1:08 AM            426 pyproject.toml
-a----         3/26/2024   1:26 AM           9753 README.md

(base) PS C:\Users\Batch 37 PIAIC\generative-ai\assignment\too-do_app> poetry run uvicorn too_do_app.main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\Batch 37 PIAIC\\generative-ai\\assignment\\too-do_app']
INFO:     Uvicorn running on <http://127.0.0.1:8000> (Press CTRL+C to quit)
INFO:     Started reloader process [12672] using WatchFiles
INFO:     Started server process [17728]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:63115 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:63124 - "GET /city HTTP/1.1" 200 OK
INFO:     127.0.0.1:63181 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:63181 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:63214 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:63224 - "GET /city HTTP/1.1" 200 OK
