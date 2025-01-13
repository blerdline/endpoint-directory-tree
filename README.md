# endpoint-directory-tree

## The problem

A common method of organizing files on a computer is to store them in hierarchical directories. For instance:

```
photos/
  birthdays/
    joe/
    mary/
  vacations/
  weddings/

```

In this challenge, you will implement commands that allow a user to create, move and delete directories.

A successful solution will take the following input:

```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST

```

and produce the following output

```
CREATE fruits

LIST
fruits

CREATE vegetables

LIST
fruits
vegetables

CREATE grains

LIST
fruits
grains
vegetables


CREATE fruits/apples

LIST
fruits
  apples
grains
vegetables

CREATE fruits/apples/fuji

LIST
fruits
  apples
    fuji
grains
vegetables

CREATE grains/squash

LIST
fruits
  apples
    fuji
grains
  squash
vegetables

MOVE grains/squash vegetables

LIST
fruits
  apples
    fuji
grains
vegetables
  squash

CREATE foods

LIST
foods
fruits
  apples
    fuji
grains
vegetables
  squash


MOVE grains foods

LIST
foods
  grains
fruits
  apples
    fuji
vegetables
  squash

MOVE fruits foods

LIST
foods
  fruits
    apples
      fuji
  grains
vegetables
  squash

MOVE vegetables foods

LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash

DELETE fruits/apples
Cannot delete fruits/apples - fruits does not exist

LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash

DELETE foods/fruits/apples

LIST
foods
  fruits
  grains
  vegetables
    squash

```

## Initial Thoughts on the Solution

I'll need to create a class that will represent the directory tree structure. This class will have methods to create, move and delete directories. I'll also need to implement a method to list the directories in the tree. In addition, I'll need to implement a method to check if the directory exists before moving or deleting it. For listing, it seems like this will be a good use case for a recursive function to traverse the tree structure. It's late now though, so I'll start on this Monday morning.

## To Run

```
python main.py
```

This can be run as a script where the user can specify a file to read the commands from. If no file is specified, the user can enter the commands manually.

### Commands

The following commands are available in interactive mode:

- CREATE <directory_name> - Creates a directory with the specified name.
- MOVE <source_directory> <destination_directory> - Moves the source directory to the destination directory.
- DELETE <directory_name> - Deletes the specified directory.
- LIST - Lists the directories in the tree.
- EXIT - Exits the program.
