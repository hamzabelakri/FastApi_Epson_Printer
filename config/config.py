import configparser
from pathlib import Path

# Create a configparser object
config = configparser.ConfigParser()

try:
    # Read the INI file
    filename = Path("./config/config.ini")
    config.read(filename.absolute())
except configparser.Error as e:
    print(f"Error reading configuration file: {e}")

# config.get('SECTION', 'VARIABLE', fallback='DEFAULT IF NOT THERE')
#  config.get   dict(config.items) # get dictionarry key value
#  config.getint
#  config.getboolean
#
SERVER_HOST = config.get('APP', 'SERVER_HOST', fallback='0.0.0.0')
SERVER_PORT = int(config.getint('APP', 'SERVER_PORT', fallback=8100))
SERVER_WORKERS = int(config.getint('APP', 'SERVER_WORKERS', fallback=1))
RELOAD = config.getboolean('APP', 'RELOAD', fallback=False)
UVICORN_LOG_LEVEL = config.get('APP', 'UVICORN_LOG_LEVEL', fallback='info')

LEVEL = config.get('LOG', 'LEVEL', fallback='INFO')
LOG_ON_FILE = config.getboolean('LOG', 'LOG_ON_FILE', fallback=False)
FILENAME = config.get('LOG', 'FILENAME', fallback='app.log')
FILE_SIZE = config.getint('LOG', 'FILE_SIZE', fallback=10)


DB_URL = config.get('DATABASE', 'DB_URL', fallback='127.0.0.1')
DB_PORT = int(config.getint('DATABASE', 'SERVER_PORT', fallback=27017))
DB_USERNAME = config.get('DATABASE', 'DB_USERNAME', fallback='admin')
DB_PASSWORD = config.get('DATABASE', 'DB_PASSWORD', fallback='admin')
DATABASE_NAME = config.get('DATABASE', 'DATABASE_NAME', fallback='my_db')

ALLOWED_ORIGINS = str(config.get('SECURITY',
                                 'ALLOWED_ORIGINS', fallback='http://*.*')).split(",")


del config
