import app
import os

from flask import Flask


if __name__=='__main__':
    os.environ['FLASK_ENV'] = 'Entorno'
    app.run(debug=True)