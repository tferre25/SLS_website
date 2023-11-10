from flaskblog import db
from run import app
from flask import request
app.app_context().push()

# mdp admin : M42,7R}g=-sxXwW$
# mdp louis : XRXuS574t6jxt2
# mdp theo : J5Q7eR4a8Zegt8
# mdp julien : pH3Y6A85Ynnj3r

from flaskblog.models import Grant, Project, User, Post, Project_request, Comment

'''p = User.query.all()

project_id = "3fce71d5f1872b956b368bb4a2bf113164687f15b44a3e0d92b90bf4d75bdbf5"
proj_req = Project_request.query.filter_by(project_id = project_id).first()
db.session.delete(proj_req)
db.session.commit()
'''

import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('flaskblog/site.db')

# Création d'un objet curseur
cursor = conn.cursor()

# Exécution d'une requête SQL (exemple)
cursor.execute('SELECT * FROM Comment;')
resultats = cursor.fetchall()

# Affichage des résultats (exemple)
for row in resultats:
    print(row)

# Fermeture de la connexion à la base de données
conn.close()

