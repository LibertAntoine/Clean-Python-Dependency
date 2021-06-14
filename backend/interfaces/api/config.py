from backend.infrastructure.injector.persistence_injector import PersistenceInjector


def default():
    PersistenceInjector().apply_default_config()


def persistence(persistence_name, options):
    PersistenceInjector().set_persistence(persistence_name, options)


