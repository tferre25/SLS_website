from flaskblog import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime #into --init--
from flask import current_app
from sqlalchemy import Float

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    aphp_num = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,default='default.png')
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)
    projects = db.relationship('Project', backref='author', lazy=True)
    grants = db.relationship('Grant', backref='author', lazy=True)
    requests = db.relationship('Project_request', backref='author', lazy=True)

    def __init__(self, username, email, aphp_num, status, password, is_admin=False, image_file='default.png'):
        self.username = username
        self.email = email
        self.aphp_num = aphp_num
        self.status = status
        self.is_admin = is_admin
        self.password = password
        self.image_file = image_file

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
        return f"User('{self.username}', '{self.is_admin}' '{self.email}', '{self.image_file}')"    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Project_request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(70), unique=True, nullable=False)
    asking_for = db.Column(db.String(70), unique=False, nullable=False)
    project_request = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    motif = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Poject_request('{self.project_id}','{self.project_request}','{self.date_posted}','{self.motif}')"

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #REQUIRED ==> nullable=False
    username = db.Column(db.String(20), unique=False, nullable=False)
    project_title = db.Column(db.String(120), unique=True, nullable=False)
    project_context = db.Column(db.Text, unique=True, nullable=False)
    project_summary = db.Column(db.Text, unique=True, nullable=False)
    bioF_needs = db.Column(db.Text, unique=False, nullable=False)
    data_owner = db.Column(db.String(20), unique=False, nullable=False)
    data_type = db.Column(db.String(20), unique=False, nullable=False)
    data_size = db.Column(db.Integer, unique=False, nullable=False)
    # NOT REQUIRED ==> nullable=True
    email = db.Column(db.String(120), nullable=False, default='noCopyMail@mail.com')
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    is_accepted = db.Column(db.Boolean, default=False, nullable=True)
    project_token = db.Column(db.String(120), unique=True, nullable=True)
    urgency_of_request = db.Column(db.String(20), unique=False, nullable=True)
    if_urgency = db.Column(db.Text, unique=False, nullable=True)
    project_context_private = db.Column(db.Text, unique=False, nullable=True)
    data_available = db.Column(db.String(20), unique=False, nullable=True)
    access_data = db.Column(db.String(120), unique=False, nullable=True)
    if_regulatory_requirements = db.Column(db.String(20), unique=False, nullable=True)
    add_info = db.Column(db.Text, unique=False, nullable=True)
    regulatory_requirements = db.Column(db.String(20), unique=False, nullable=True)
    application = db.Column(db.String(20), unique=False, nullable=True)
    clinical_service = db.Column(db.String(20), unique=False, nullable=True)
    laboratories = db.Column(db.String(20), unique=False, nullable=True)
    if_no_laboratory = db.Column(db.String(20), unique=False, nullable=True)
    organism = db.Column(db.String(20), unique=False, nullable=True)
    principal_investigator = db.Column(db.String(20), unique=False, nullable=True)
    promotor = db.Column(db.String(20), unique=False, nullable=True)
    
    def __repr__(self) -> str:
        return f"Project('{self.project_token}','{self.username}','{self.project_title}','{self.application}','{self.is_accepted}')"
    
class Grant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #REQUIRED ==> nullable=False
    username = db.Column(db.String(20), unique=False, nullable=False)
    project_title = db.Column(db.String(120), unique=True, nullable=False)
    project_context = db.Column(db.Text, unique=True, nullable=False)
    project_summary = db.Column(db.Text, unique=True, nullable=False)
    bioF_needs = db.Column(db.Text, unique=False, nullable=False)
    data_owner = db.Column(db.String(20), unique=False, nullable=False)
    data_type = db.Column(db.String(20), unique=False, nullable=False)
    data_size = db.Column(db.Integer, unique=False, nullable=False)
    funding_type = db.Column(db.String(20), unique=False, nullable=False)
    total_amount = db.Column(db.String(20), unique=False, nullable=False)
    deadline = db.Column(db.Date(), unique=False, nullable=False)

    #NOT REQUIRED ==> nullable=True
    email = db.Column(db.String(120), nullable=False, default='noCopyMail@mail.com')
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    is_accepted = db.Column(db.Boolean, default=False, nullable=True)
    project_token = db.Column(db.String(120), unique=False, nullable=True)
    urgency_of_request = db.Column(db.String(20), unique=False, nullable=True)
    if_urgency = db.Column(db.Text, unique=False, nullable=True)
    project_context_private = db.Column(db.Text, unique=False, nullable=True)
    data_available = db.Column(db.String(20), unique=False, nullable=True)
    access_data = db.Column(db.String(120), unique=False, nullable=True)
    if_regulatory_requirements = db.Column(db.String(20), unique=False, nullable=False)
    add_info = db.Column(db.Text, unique=False, nullable=False)
    regulatory_requirements = db.Column(db.String(20), unique=False, nullable=True)
    application = db.Column(db.String(20), unique=False, nullable=True)
    clinical_service = db.Column(db.String(20), unique=False, nullable=True)
    organism = db.Column(db.String(20), unique=False, nullable=True)
    laboratories = db.Column(db.String(20), unique=False, nullable=True)
    if_no_laboratory = db.Column(db.String(20), unique=False, nullable=True)
    principal_investigator = db.Column(db.String(20), unique=False, nullable=True)
    promotor = db.Column(db.String(20), unique=False, nullable=True)

    def __repr__(self) -> str:
        return f"Grant('{self.project_token}','{self.username}','{self.project_title}','{self.application}','{self.is_accepted}')"




