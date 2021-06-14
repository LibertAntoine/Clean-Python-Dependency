from backend.interfaces import api
from frontend import application

if __name__ == "__main__":
    api.config.default()
    application.launch()


