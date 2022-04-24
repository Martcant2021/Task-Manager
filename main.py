from app import app
import os

IS_DEV = app.env == 'Entorno'

if __name__=='__main__':
    assert os.path.exists('.env')
    os.environ['FLASK_ENV'] = 'Entorno'
    app.run(debug=True)