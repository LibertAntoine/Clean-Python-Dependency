class User:
    name = str,
    age = int

    def __init__(self, data=None):
        self.hydrate(data)

    def hydrate(self, data):
        if not data:
            return
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
