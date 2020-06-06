# doskey todo=python "C:\Users\anime\Documents\Python Scripts\todo_list_maker\todo_list_maker.py" $*
# todo --do "write a blog about this windows aliasing for a do-to list maker over the weekend." --name new_list.txt -v -n -l
# "" are used only when the argument has a space in it

import sys

# A function for exiting the script after printing a message  
def q(text = ''):
    print(f'>{text}<')
    sys.exit()

import argparse, os

# Desktop path
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')

# Default to-do list file name
todo_list_name = 'todo_list.txt'

parser = argparse.ArgumentParser(description='Following are the arguments that can be passed form the terminal itself ! Cool huh ? :D')
parser.add_argument('--do', type = str, default = 'You were supposed to pass you to-do item here :p', help = 'This is the to-do item to be written into the todo_list.txt')
parser.add_argument('--path', type = str, default = desktop_path, help = 'Location of the do-to list')
parser.add_argument('--name', type = str, default = todo_list_name, help = 'Name of the do-to list')

parser.add_argument('-n','--new', action = 'store_true', help = 'Use -n if you want to make a new to-do list by deleting an already existing one') # args.new will return True if -n or --new is used in the terminal
parser.add_argument('-v','--verbose', action = 'store_true', help = 'Use -v if you want to see all the useful information printed on the terminal') # args.verbose will return True if -v or --verbose is used to display more information on the terminal
parser.add_argument('-l','--list', action = 'store_true', help = 'Use -l if you want to view all the to-do items present in the list') # args.list will return True if -l or --list is used in the terminal

args = parser.parse_args()

if __name__ == '__main__':

    # to-do-list file name file path
    todo_list_txt_file = os.path.join(args.path, args.name)

    # List all the to-do list items
    if args.list:
        with open(todo_list_txt_file, "r") as myfile:
            items = myfile.read()
            print(items)
        q('-----------------------------------------------------------------')

    if args.new:
        # Delete the file
        if os.path.exists(todo_list_txt_file):
            os.remove(todo_list_txt_file)
            if args.verbose:
                print(f'{todo_list_txt_file} deleted !\n')
        
    # Get to-do item from the terminal/command line
    todo_item = args.do
    
    if not os.path.exists(todo_list_txt_file):
        with open(todo_list_txt_file, "w") as myfile:
            myfile.write(todo_item)
    else:
        with open(todo_list_txt_file, "a") as myfile:
            myfile.write('\n' + todo_item)
            
    if args.verbose:  
        print(f'message \n{todo_item}\nappended at \n{todo_list_txt_file}')

# useful resources-
# https://www.youtube.com/watch?v=E_6Lklnakew
# https://stackoverflow.com/questions/14667922/doskey-macro-with-spaces-in-passed-variable