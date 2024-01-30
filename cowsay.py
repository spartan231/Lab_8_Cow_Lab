# imports sys
import sys

# imports heifer_generator
from heifer_generator import HeiferGenerator

# list all f the avariable cows
def list_cows(cows):
    # creates an empty list to create the string
    list_of_cows = ""

    list_of_dragons = ""
    # iterates over the list of cows
    for cow in cows:
        # adds these cows to the string
        list_of_cows += (cow.name) + " "

    # returns the string
    return list_of_cows

def list_file_cows(file):
    list_of_cows_file = ""
    for fc in file:
        list_of_cows_file += fc.name + " "
    return list_of_cows_file
def find_cow(name, cows):
    # iterates over cows
    for cow in cows:
        # checks to see if the name given is in the cows list
        if name == cow.name:
            # if it is return that name
            return cow.name

    # else return None if not in the list
    return None

def find_filecow(name, fcows):
    for file in fcows:
        if name == file.filename:
            return file.filename

    return None


if __name__ == '__main__':
    # list of Cow objects
    # intializes the HeiferGenerator class
    cows = HeiferGenerator.get_cows()
    file_cs = HeiferGenerator.get_file_cows()

    # checks to see if one of the argvs is -l
    if sys.argv[1] == "-l":
        # prints the available cows
        print("Cows available: " + list_cows(cows))
        print("File cows available: " + list_file_cows(file_cs))
    # checks to see if one of the argvs is -n
    elif sys.argv[1] == '-n':
        # checks to see if that cow is in the cows list
        cow = find_cow(sys.argv[2], cows)

        # checks to see if the cow is not in the cows
        if cow == None:
            # prints this statement
            print(f"Could not find {sys.argv[2]} cow!")

        # if cow is in the cows
        elif cow != None:
            # prints the message
            message = ""
            for i in (sys.argv[3:]):
                message += i + " "
            print(message)

            # iterates over the cows list
            for i in cows:
                # checks to see if i name is equal to the name of the cow
                # if it is it will get that image and print
                if i.get_name() == cow:
                    print(i.get_image())
                    # checks to see if the name is dragon
                    # if so prints this dragon can breathe fire
                    if i.get_name() == "dragon":
                        print("This dragon can breathe fire.")
                    # if the name is ice-dragon print cannot breathe fire
                    if i.get_name() == "ice-dragon":
                        print("This dragon cannot breathe fire.")

    elif sys.argv[1] == "-f":
        file_c = find_cow(sys.argv[2], file_cs) # checks to see if that file cow is in the file cows list

        if file_c == None: # checks to see if the file cow is not in the file cows
            print(f"Could not find {sys.argv[2]} cow!")
        elif file_c != None:
            message = ""
            for i in sys.argv[3:]:
                message += i + " "
            print(message) # prints the message
            # GETS THE FILE IMAGE
            for i in file_cs:
                if i.get_name() == file_c:

                    print(i.get_image())

    else:
        # prints the message
        message = ""
        for i in sys.argv[1:]:
            message += i + " "

        print(message)
        # prints the default image of the cow
        print(cows[0].get_image())

