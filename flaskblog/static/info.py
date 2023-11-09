
racine = '''
    Les bioinformaticiens transversaux de la cellule bioinformatique de l'hôpital Saint-Louis sont à 
    votre disposition pour réaliser vos projets, que ce soit à des fins de recherche ou pour des 
    diagnostics de routine. Cette plateforme vous offre également l’opportunité de solliciter de 
    l’aide pour la rédaction de la partie bioinformatique de vos demandes de financement. 
    Notre expertise englobe plusieurs domaines, allant des diverses méthodes -omics 
    (génomique, transcriptomique, multiomique) à la métagénomique, sans oublier l'intelligence artificielle. 
    Cliquez sur l'un des boutons ci-contre en fonction de vos besoins.
'''

login = '''
    S'authentifier vous donnera la possibilité de partager des nouveaux postes, de soumettre un projet ou une subvention à la cellules bioinformatique
'''
register = '''
    Attention, l'Username, l'email et le numéro APHP sont des informations uniques. 
'''
account = '''
    Un titre 'Admin Account' apparaîtra sous l'username, si vous êtes administrateur. 
    Vous avez l'opportunité de faire une mise à jour de toutes les informations de votre profil.
'''
about = '''
    Bienvenue sur HelpBioinfo , le reseau qui sera dedier au depot de projets de recherche au sein de l'AP-HP.
    Vision : Créer des opportunités pour les chercheurs de pouvoir deposer leurs projets en toute securiter.
    Ainsi dans le but de soliciter l'aide de la cellule bioinformatique de l'APHP.
    La mission de HelpBioinfo est simple? mettre en relation des chercheurs et des bioinformaticiens de l'APHP  
    pour les rendre plus performants et productifs.\n
'''
post = '''
    Ici, vous avez l'opportunité de partager des posts. Échanger les idées,
    partager ses résultats ou une actualité importante pour un utilisateur.
    Seul l'utilisateur authentifié peut créer un nouveau poste.
    Vous avez la possibilité de faire une recherche d'un poste à travers un mot-clé 
    grâce à la fonctionnalité 'search' accessible sur cette page via la barre de navigation.
'''
projects = '''
    Les administrateurs (bioinformaticiens) peuvent modifier, voir supprimer un projet quelconque.
    Vous pouvez aussi consulter tous les projets de l'utilisateur en question, ainsi que son profil.
    Enfin, les projets de diagnostic acceptés ne sont visibles que par les administrateurs,
    tandis que les projets de recherches acceptés peuvent être consultés par tous les utilisateurs authentifiés.
'''
grants = '''
    Les administrateurs (bioinformaticiens) peuvent modifier, voir supprimer une demande de subvention (Grant) quelconque.
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
profile = '''
    Info profile
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
        'new_post':new_post,
        'racine':racine,
        'profile':profile

    }

    return dico[key]


