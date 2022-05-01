import os
from Apps import app
from Apps.models import db


if __name__=='__main__':
    db.create_all()
    os.environ['FLASK_ENV'] = 'Entorno'
    app.run(debug=True)

