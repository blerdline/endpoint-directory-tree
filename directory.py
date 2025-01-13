class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}

    def add_subdirectory(self, name):
        if name not in self.subdirectories:
            self.subdirectories[name] = Directory(name)

    def delete_subdirectory(self, name):
        if name in self.subdirectories:
            del self.subdirectories[name]

    def get_subdirectories(self, name):
        return self.subdirectories.get(name)