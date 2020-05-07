"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE


def get_foo_text():
    with open('./src/foo.txt') as r:
        for line in r:
            print(line)
    r.close()


get_foo_text()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

new_file = open("bar.txt", "w")
new_file.writelines(["I am the egg man,\n", "They are the egg men,\n",
                     "I am the walrus,\n", "Goo goo g'joob"])
new_file.close()
