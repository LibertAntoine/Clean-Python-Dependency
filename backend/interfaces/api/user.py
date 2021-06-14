from backend.core.usecases.createUser import CreateUser


def create(name, age):
    user = {"name": name, "age": age}
    CreateUser().create(user)
