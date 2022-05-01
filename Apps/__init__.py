from flask import Flask



app = Flask(__name__)



from Apps import config
from Apps import routes

