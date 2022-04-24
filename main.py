from app import app
import os

IS_DEV = app.env == 'Entorno'

if __name__=='__main__':
    os.environ['FLASK_ENV'] = 'Entorno'
    app.run(debug=True)