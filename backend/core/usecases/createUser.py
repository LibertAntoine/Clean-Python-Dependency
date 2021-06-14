from backend.core.entities import User
from backend.core.ports import Config


class CreateUser:
    def __init__(self):
        self.persistence = Config.persistence

    def create(self, user):
        new_user = User()
        new_user.hydrate(user)
        self.persistence.create(new_user)

