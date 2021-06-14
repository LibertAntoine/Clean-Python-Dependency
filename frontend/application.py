from backend.interfaces import api


def launch():
    api.user.create("Adam", 12)
    
    my_sql_options = {
        "url": "http://my_sql.fr",
        "pseudo": "admin",
        "password": "root"
    }
    api.config.persistence("MySQL", my_sql_options)
    api.user.create("Rick", 16)
