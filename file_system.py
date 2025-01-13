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
        #Split the path into parts
        parts: list[str] = path.split('/')

        # Set a parent directory to the one level above the last part of the path
        parent_directory: Directory = self.root
        for part in parts[:-1]:
            parent_directory = parent_directory.get_subdirectories(part)

        # If path does not exist print an error message
        if parent_directory is None or parts[-1] not in parent_directory.subdirectories:
            print("Path does not exist")
            return
        # Delete the last part of the path from the parent directory
        parent_directory.delete_subdirectory(parts[-1])

    def list(self) -> None:
        # need a recursive function to help keep the indentation consistent
        # and to print the subdirectories.  This function will be called
        # from the list method
        self._list(self.root, 0)

    def _list(self, directory: Directory, level) -> None:
        # Print the name of the directory
        for name in sorted(directory.subdirectories.keys()):
            print("  " * level + name)
            self._list(directory.get_subdirectories(name), level + 1)

    def move(self, source: str, destination: str) -> None:
        pass