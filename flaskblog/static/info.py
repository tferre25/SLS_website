

login = '''
   Info login
'''
register = '''
    ==> Info for registration.
    Un compte ici vous permettre de soumettre un projet, une subvention, 
    ou même partager un post avec tous les visiteurs de cette plateforme web
'''
account = '''
    ==> accout info.
    Un titre en rouge 'Admin Account' apparaîtra sous l'username, si vous êtes administrateur. 
    Vous avez l'opportunité de faire une mise à jour de toutes les informations de votre profil.
'''
about = '''
    ==> À propos de MediResearchDepot : Bienvenue sur MediResearchDepot , le reseau qui sera dedier au depot de projets de recherche au sein de l'AP-HP.
    ==> Vision : Créer des opportunités pour les chercheurs de pouvoir deposer leurs projets en toute securiter. Ainsi dans le but de soliciter l'aide
        de la cellule bioinformatique de l'APHP.
    ==> Mission : La mission de MediResearchDepot est simple : mettre en relation des chercheurs et des bioinformaticiens de l'APHP  pour les rendre plus performants et productifs.\n
'''
post = '''
    Ici, vous avez l'oportunitee de partager des posts. Échanger les idées,
    partager ses résultats ou une actualité importante pour un utilisateur.
    Vous n'êtes pas obligé à vous connecter pour avoir accès à cette page de posts.
    Vous avez la possibilité de faire une recherche d'un post à travers un mot-clé grâce à la fonctionnalité 'search'.
    Accessible sur cette page via la barre de navigation.
'''
projects = '''
    Ici, vous avez accès a tous les projets ayant déjà et consultée et accepter par la cellule bioinfo de l'aphp
    Vous devez être connecté pour avoir accès à cette fonctionnalité.
    Les admins (les bioinformaticiens) peuvent modifier, voir supprimer un projet.
    Vous pouvez aussi consulter tous les projets de l'utilisateur en question, ainsi que son profil. 
'''
grants = '''
    Ici, vous avez accès a tous les Grants ayant déjà et consultée et accepter par la cellule bioinfo de l'aphp
    Vous devez être connecté pour avoir accès à cette fonctionnalité.
    Les admins (les bioinformaticiens) peuvent modifier, voir supprimer un Grant.
    Vous pouvez aussi consulter tous les Grants de l'utilisateur en question, ainsi que son profil. 
'''
about_us = '''
    Présentation brève de la cellule bio-informatique de l'hôpital 
    St-Louis. En tant que visiteur, vous aurez aussi accès a une brève 
    documentation de quelques domaines médicaux sur lesquelles, 
    nos bioinformaticiens peuvent y être utiles et vous apporter leur aide et conseils. 
'''

new_project = '''
    Vous pouvez créer un Projet à travers ce formulaire.
    À la suite de la validation du formulaire, celui-ci sera envoyé automatiquement à la cellule bioinfo et aux membres de le comité de recherche au sein de l'hôpital St-Louis.
    Un mail avec un récapitulatif du Projet vous sera envoyé un mail aussi.
    Une fois, le Projet est accepté, il sera visible dans la page Projet que vous trouverez dans la barre de navigation.
    Si le Projet est refusé, un motif vous sera communiqué par mail. 

'''
new_post = '''
    Dans un post, il peut s'agit d'un article publié, d'une information particulière qui concerne la cellule BioInfo...
    Soyer réactif ! 
'''

# TO ACCESS INFO IN ROOT PAGES
def instructions(key):

    dico = {
        'login': login,
        'register': register,
        'account':account,
        'about': about,
        'post':post,
        'projects':projects,
        'grants':grants,
        'about_us':about_us,
        'new_project':new_project,
        'new_post':new_post

    }

    return dico[key]


