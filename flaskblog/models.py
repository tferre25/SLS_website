from flaskblog import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime #into --init--
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    projects = db.relationship('Project', backref='author', lazy=True)
    grants = db.relationship('Grant', backref='author', lazy=True)

    def get_reset_token(self, expires_sec= 1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    project_title = db.Column(db.String(120), unique=False, nullable=True)
    application = db.Column(db.String(20), unique=False, nullable=True)
    organism = db.Column(db.String(20), unique=False, nullable=True)
    principal_investigator = db.Column(db.String(20), unique=False, nullable=True)

    promotor = db.Column(db.String(20), unique=False, nullable=True)
    urgency_of_request = db.Column(db.String(20), unique=False, nullable=True)
    if_urgency = db.Column(db.Text, unique=False, nullable=True)

    project_context = db.Column(db.Text, unique=False, nullable=True)
    project_context_private = db.Column(db.Text, unique=False, nullable=True)
    project_summary = db.Column(db.Text, unique=False, nullable=True)
    bioF_needs = db.Column(db.Text, unique=False, nullable=True)

    data_available = db.Column(db.Boolean, unique=False, nullable=True)
    access_data = db.Column(db.String(120), unique=False, nullable=True)
    data_owner = db.Column(db.String(20), unique=False, nullable=True)

    regulatory_requirements = db.Column(db.Boolean, unique=False, nullable=True)
    if_regulatory_requirements = db.Column(db.String(20), unique=False, nullable=True)
    data_type = db.Column(db.String(20), unique=False, nullable=True)

    data_size = db.Column(db.Integer, unique=False, nullable=True)
    add_info = db.Column(db.Text, unique=False, nullable=True)
    
    def __repr__(self) -> str:
        return f"Project('{self.username}','{self.project_title}','{self.application}')"
    
class Grant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    project_title = db.Column(db.String(120), unique=False, nullable=True)
    application = db.Column(db.String(20), unique=False, nullable=True)
    organism = db.Column(db.String(20), unique=False, nullable=True)
    principal_investigator = db.Column(db.String(20), unique=False, nullable=True)

    promotor = db.Column(db.String(20), unique=False, nullable=True)
    funding_type = db.Column(db.String(20), unique=False, nullable=True)
    total_amount = db.Column(db.Numeric(10, 2), unique=False, nullable=True)
    deadline = db.Column(db.Date(), unique=False, nullable=True)
    urgency_of_request = db.Column(db.String(20), unique=False, nullable=True)
    if_urgency = db.Column(db.Text, unique=False, nullable=True)

    project_context = db.Column(db.Text, unique=False, nullable=True)
    project_context_private = db.Column(db.Text, unique=False, nullable=True)
    project_summary = db.Column(db.Text, unique=False, nullable=True)
    bioF_needs = db.Column(db.Text, unique=False, nullable=True)

    data_available = db.Column(db.Boolean, unique=False, nullable=True)
    access_data = db.Column(db.String(120), unique=False, nullable=True)
    data_owner = db.Column(db.String(20), unique=False, nullable=True)

    regulatory_requirements = db.Column(db.Boolean, unique=False, nullable=True)
    if_regulatory_requirements = db.Column(db.String(20), unique=False, nullable=True)
    data_type = db.Column(db.String(20), unique=False, nullable=True)

    data_size = db.Column(db.Integer, unique=False, nullable=True)
    add_info = db.Column(db.Text, unique=False, nullable=True)
    
    def __repr__(self) -> str:
        return f"Project('{self.username}','{self.project_title}','{self.application}', '{self.total_amount}, '{self.deadline}')"
    
