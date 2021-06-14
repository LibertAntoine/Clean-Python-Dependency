from backend.core.ports.config import Config
from backend.infrastructure.persistence import ElasticSearch, MySQL


class PersistenceInjector(Config):
    available_persistence = {
        "ElasticSearch": ElasticSearch,
        "MySQL": MySQL,
    }

    def apply_default_config(self):
        options = {"url": "http://elastic_search_default.fr"}
        Config.persistence = self.available_persistence["ElasticSearch"](options)

    def set_persistence(self, persistence_name, options):
        self._check_persistence_name(persistence_name)
        Config.persistence = self.available_persistence[persistence_name](options)

    def _check_persistence_name(self, persistence_name):
        if not self.available_persistence.get(persistence_name, False):
            raise ValueError("Given persistence name is not available")

# Example of various injection libraries in python
"""
import inject
from backend.core.ports import Persistence
from backend.infrastructure.persistence import ElasticSearch, MySQL


class Config:
    binder = inject.Binder()

    available_persistence = {
        "ElasticSearch": ElasticSearch,
        "MySQL": MySQL,
    }

    @staticmethod
    def setup():
        inject.configure(Config._default_configuration)

    @staticmethod
    def _default_configuration(binder):
        binder.bind(Persistence, Config.available_persistence["ElasticSearch"]())
"""


# Example of Dependency Injection Container with auto-wiring by type
"""
from lagom import Container
from backend.core.ports import Persistence
from backend.infrastructure.persistence import elastic_search, my_sql


class Config:
    container = Container()

    @staticmethod
    def setup():
        Config.container[Persistence] = lambda: elastic_search.ElasticSearch()
"""

# Other example of Dependency Injection Container
"""
from dependency_injector import providers, containers
from backend.infrastructure.persistence import elastic_search, my_sql

available_persistence = {
    "ElasticSearch": elastic_search.ElasticSearch,
    "MySQL": my_sql.MySQL,
}


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration(default={
        "url": "http://test-url3.fr"
    })
    persistence = providers.Singleton(available_persistence["ElasticSearch"], config)

    @staticmethod
    def change_persistence(name):
        Configs.persistence = providers.Singleton(available_persistence[name], Configs.config)
"""

"""
list of python injector: 
    * lagom
    * inject
    * injector
    * dependency-injector
    * serum 

"""