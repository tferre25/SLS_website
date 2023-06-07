from flaskblog import db
from run import app
from flask import request
app.app_context().push()

# mdp admin : M42,7R}g=-sxXwW$
# mdp louis : XRXuS574t6jxt2
# mdp theo : J5Q7eR4a8Zegt8
# mdp julien : pH3Y6A85Ynnj3r

from flaskblog.models import Grant, Project, User, Post, Project_request

print(f'--------------------------> Post')
print(Post.query.all())

print(f'--------------------------> Project')
print(Project.query.all())

print(f'--------------------------> User')

'''u = User.query.get(1)
u.is_admin = True
db.session.commit()'''
print(User.query.all())


print(f'--------------------------> Grant')
'''g = Grant.query.get(1)
db.session.delete(g)
db.session.commit()'''
print(Grant.query.all())

print(f'--------------------------> Project_request')
print(Project_request.query.all())



