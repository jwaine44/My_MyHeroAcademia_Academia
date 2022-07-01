from flask import Flask

app = Flask(__name__)

app.secret_key = "secret project"           # Needs to be added for session; secret_key can be set to anything in the string

# Set database to the name of the schema in MySQL Workbench
database = "mmhaa_schema"