# ESTRUCTURA 
backend/
├── .gitignore
├── README.MD
├── env/
│   ├── Lib/
│   │   └── site-packages/
│   │       ├── pip-24.2.dist-info/
│   │       ├── pip/
│   │       ├── pip/_internal/
│   │       ├── pip/_vendor/
│   │       └── ...
│   ├── Scripts/
│   │   ├── activate
│   │   ├── activate.bat
│   │   └── Activate.ps1
│   └── pyvenv.cfg
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── controller.py
│   ├── extensions.py
│   ├── models/
│   │   └── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services/
│   │   └── __init__.py
│   └── utils/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── main.py
└── wsgi.py