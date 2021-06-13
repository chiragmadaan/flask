from home import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    """docstring for User"""
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(length=15), nullable=False)
    lastname = db.Column(db.String(length=15))
    email = db.Column(db.String(length=30), unique=True)
    phone_number = db.Column(db.String(length=10))
    password_hash = db.Column(db.String(length=60), nullable=False)
    # fk = db.Column(db.Integer(), db.ForeignKey('other_table/model.id'))
    # clm = db.relationship('Table/Model', backref='reference_name', lazy=False)

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, password_text):
        self.password_hash = bcrypt.generate_password_hash(password_text).decode('utf-8')

    def verify_password(self, password_text):
        return bcrypt.check_password_hash(self.password_hash, password_text)
