# Flask + Google Cloud SQL Example (Simplified)

Important! Please first create the file `config.py` containing the following variables:

```
SECRET_KEY = os.urandom (256)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# GCP
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = ''
CLOUDSQL_DATABASE = ''
CLOUDSQL_CONNECTION_NAME = ''
LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@127.0.0.1:3306/{dbn}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
)

LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
    con=CLOUDSQL_CONNECTION_NAME,
)

if os.environ.get ('GAE_INSTANCE'):
    SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
else:
    SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI

# Override to SQLITE (for testing ...)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
```

## Instructions

Download the proxy:

`$ wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy`

Make the proxy executable:

`$ chmod +x cloud_sql_proxy`

If you created a new Google Cloud SQL instance for this project, make sure to create a database per the `CLOUDSQL_DATABASE` variable in the `config.py` file.

Create a service account in the GCP console with permissions to access your Google Cloud SQL instance. Download it/rename it to `key.json`.

Run the proxy with the command:

`$ GOOGLE_APPLICATION_CREDENTIALS=key.json ./cloud_sql_proxy -instances="<CLOUDSQL_CONNECTION_NAME>"=tcp:3306`

... where `CLOUDSQL_CONNECTION_NAME` is your instance's connection name (found in the GCP console.)

In another terminal window within this project's directory, create a python3 virtual environment. Activate it and install the required dependencies to this project.

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt
```

Run this project locally.

`$ python main.py`


