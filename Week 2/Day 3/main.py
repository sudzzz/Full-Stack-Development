# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    file = open("file.txt", "w")
    lines = ["This is file Handling, \n In Python, \n Thanks \n"]
    file.write(f'Hello There {name}\n ')
    file.writelines(lines)
    file.close()

def print_hi2(name):
    file = open("file2.txt",)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Sudhir')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
