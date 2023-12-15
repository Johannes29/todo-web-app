# To Do Web App
A simple web app for keeping track of tasks

## Development setup
Make a virtual environment for Python
```bat
python -m venv .venv
```

Then enter it (run this line in cmd)
```bat
.venv\Scripts\activate.bat
```

> If you wish to exit the virtual environment, run `deactivate` 

Finally install the required python packages
```bat
pip install -r requirements.txt
```

## Running the server
```bat
flask --app api/main run
```

## Running the tests
```bat
python -m unittest discover -s tests
```
