# Flask

```bash
virtualenv .  
source /bin/activate  
pip install flask  
pip install flask-sqlalchemy  
pip install flask-login  
pip install flask-bcrypt  
pip install email_validator  
pip install flask-wtf  
~~export FLASK_APP=filename.py~~  
~~export FLASK_DEBUG=1~~  
OR pip install -r requirements.txt  
flask run
```

### To create DB
Go to python3 shell  
```python
from home import db  
db.create_all()  
from home.models import Users  
user = Users(firstname='',...)  
db.session.add(user)  
db.session.commit()  
Users.query.all()  
User.query.filter_by(email='').first()  
```