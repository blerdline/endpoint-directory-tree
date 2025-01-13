#use the directory class to manage the file system
from directory import Directory


class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("")

    def create(self, path: str) -> None:

        #Split the path into parts
        parts: list[str] = path.split('/')

        #Set the base directory to the root
        current_directory: Directory = self.root

        # Add each part of the path to the directory by adding the first part
        # then setting the current directory to the subdirectory we just added
        # repeat until we reach the end of the path
        for part in parts:
            current_directory.add_subdirectory(part)
            current_directory = current_directory.get_subdirectories(part)
        

    def delete(self, path: str) -> None:
        pass

    def list(self) -> None:
        pass

    def move(self, source: str, destination: str) -> None:
        pass