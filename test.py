from flaskblog import db
from run import app
from flask import request
app.app_context().push()

from flaskblog.models import Grant, Project, User, Post, Project_request

print(f'--------------------------> Post')
print(Post.query.all())
p= Post.query.get(1)
print(p.image_file)

print(f'--------------------------> Project')
#projects = list(Project.query.filter_by(is_accepted=False).all())
#PROJECTS = Project.query.filter_by(is_accepted=True)
#print(PROJECTS)
print(Project.query.all())

print(f'--------------------------> User')
u=User.query.get(2)
u.is_admin=True
db.session.commit()
print(u)

print(f'--------------------------> Grant')
'''grants = list(Grant.query.filter_by(is_accepted=False).all())
g=Grant.query.get_or_404(1)
print(g.total_amount)
print(g)'''

print(f'--------------------------> Project_request')
print(Project_request.query.all())



