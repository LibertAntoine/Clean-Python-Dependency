from backend.core.ports.persistence import Persistence


class ElasticSearch(Persistence):

    def __init__(self, options):
        self.url = options.get("url", None)

    def create(self, entity):
        print(f"La création de {entity.name} a bien été réalisé sur Elastic Search"
              f" à l'url : {self.url}")
