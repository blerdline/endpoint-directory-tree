#use the directory class to manage the file system
from directory import Directory


class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("")

    # As I was building out the move functionality I realized 
    # I was going to need to do the same thing I did for 
    # delete so creating a helper function to handle that 
    # problem
    def _traverse_path(self, path_parts: str) -> Directory:
        current_directory: Directory = self.root
        for part in path_parts:
            current_directory = current_directory.get_subdirectories(part)
            if current_directory is None:
                return None
        return current_directory

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
        
        print(f"CREATE {path}")

    def delete(self, path: str) -> None:
        #Split the path into parts
        parts: list[str] = path.split('/')

        # Set a parent directory to the one level above the last part of the path
        parent_directory: Directory = self._traverse_path(parts[:-1])
        
        print(f"DELETE {path}")
        # If path does not exist print an error message
        if parent_directory is None or parts[-1] not in parent_directory.subdirectories:
            print(f"Cannot delete {path} - {'/'.join(parts[:-1])} does not exist")
            return
        # Delete the last part of the path from the parent directory
        parent_directory.delete_subdirectory(parts[-1])


    def list(self) -> None:
        # need a recursive function to help keep the indentation consistent
        # and to print the subdirectories.  This function will be called
        # from the list method
        print("LIST")
        self._list(self.root, 0)

    def _list(self, directory: Directory, level) -> None:
        # Print the name of the directory
        for name in sorted(directory.subdirectories.keys()):
            print("  " * level + name)
            self._list(directory.get_subdirectories(name), level + 1)

    def move(self, source: str, destination: str) -> None:
        #Split the source path into parts
        source_parts: list[str] = source.split('/')
        #Split the destination path into parts
        destination_parts: list[str] = destination.split('/')

        # Set a parent directory of source to the one level above the last part of the source path
        source_parent_directory: Directory = self._traverse_path(source_parts[:-1])
    
        # Set a parent directory of destination to the path of the destination parts
        destination_parent_directory: Directory = self._traverse_path(destination_parts)
        
        # If source path does not exist print an error message
        if source_parent_directory is None or source_parts[-1] not in source_parent_directory.subdirectories:
            print(f"Cannot move {source} - {'/'.join(source_parts)} does not exist")
            return


        # If destination path does not exist print an error message
        if destination_parent_directory is None:
            print(f"Cannot move {source} - {destination} does not exist")
            return
        
        directory_to_move: Directory = source_parent_directory.get_subdirectories(source_parts[-1])
        # Move the source directory to the destination directory
        destination_parent_directory.add_subdirectory(source_parts[-1])
        destination_parent_directory.subdirectories[source_parts[-1]] = directory_to_move
        source_parent_directory.delete_subdirectory(source_parts[-1])

        print(f"MOVE {source} {destination}")