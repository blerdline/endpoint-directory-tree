
def main():

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
                pass
            elif command == "DELETE":
                #Call the delete function
                pass
            elif command == "LIST":
                #Call the list function
                pass
            elif command == "MOVE":
                #Call the move function
                pass
            else:
                print("Invalid command. Please try again.")
        except Exception as e:
            print("An error occurred: ", e)

if __name__ == "__main__":
    main()
            