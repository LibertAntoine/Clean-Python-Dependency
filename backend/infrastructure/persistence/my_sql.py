from backend.core.ports.persistence import Persistence


class MySQL(Persistence):

    def __init__(self, options):
        self.url = options.get("url", None)
        self.pseudo = options.get("pseudo", None)
        self.password = options.get("password", None)

    def create(self, entity):
        print(f"La création de {entity.name} a bien été réalisé sur MySQL"
              f" à l'url : {self.url}")
