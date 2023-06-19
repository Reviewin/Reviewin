import pkg_resources
import ast

# Chemin vers le fichier Python à analyser
chemin_fichier = 'C:/Users/33769/Documents/Github/Reviewin/api-server-fastapi/api.py'

# Récupérer la liste de tous les packages installés
packages_installes = [dist.project_name for dist in pkg_resources.working_set]

# Analyser le fichier Python pour extraire les noms des modules importés
modules_utilises = set()
with open(chemin_fichier, 'r') as f:
    tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules_utilises.update(alias.name.split('.')[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules_utilises.add(node.module.split('.')[0])

# Afficher chaque module utilisé avec sa version s'il est installé
for module in modules_utilises:
    if module in packages_installes:
        version = pkg_resources.get_distribution(module).version
        print(f"{module} ({version})")
    else:
        print(f"{module} (non installé)")
