
from file_system import FileSystem


def main():

    #Create a file system object
    fs = FileSystem()
    while True:
        try:
            command_line = input("Enter command (or type EXIT to quit): ").strip()

            if not command_line:
                continue

            #Check for EXIT Command
            if command_line.upper() == "EXIT":
                print("Exiting the program.")
                break

            #Split the command line into parts
            command_parts = command_line.split()

            #get first part of command
            command = command_parts[0].upper()

            if command == "CREATE":
                #Call the create function
                fs.create(command_parts[1])
            elif command == "DELETE":
                #Call the delete function
                fs.delete(command_parts[1])
            elif command == "LIST":
                #Call the list function
                fs.list()
            elif command == "MOVE":
                #Call the move function
                fs.move(command_parts[1], command_parts[2])
            else:
                print("Invalid command. Please try again.")
        except Exception as e:
            print("An error occurred: ", e)

if __name__ == "__main__":
    main()
            