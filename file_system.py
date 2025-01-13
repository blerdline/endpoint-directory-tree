#use the directory class to manage the file system
from directory import Directory


class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("")

    def create(self, path: str) -> None:
        pass

    def delete(self, path: str) -> None:
        pass

    def list(self) -> None:
        pass

    def move(self, source: str, destination: str) -> None:
        pass