# Flask

virtualenv .
source /bin/activate
pip install flask
export FLASK_APP=filename.py
export FLASK_DEBUG=1
flask run

## To create DB
Go to shell python3
from home import db
db.create_all()
from home.models import Users
user = Users(firstname='',...)
db.session.add(user)
db.session.commit()
Users.query.all()
User.query.filter_by(email='').first()