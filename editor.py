from Tkinter import * # Enables use of GUI
from tkFileDialog import * # Enables manipulation of files

filename = None # Creates filename variable

#Functions
def newFile():
    global filename # Loads 'filename' variable into function
    filename = 'Untitled' # Assigns text to 'filename' variable
    text.delete(0.0, END) # Clears previous text from window

def saveFile():
    global filename # Loads 'filename' variable into function
    t = text.get(0.0, END) # Assigns contents of window to 't'
    f = open(filename, 'w') # Assigns the opened file in write mode to 'f'
    f.write(t) # Writes the contents of 't' to 'f'
    f.close() # Closes the file contained in 'f'

def saveAs():
    f = asksaveasfile(mode = 'w', defaultextension = '.txt') # Assigns 'f' to open save dialogue, set mode to write and default file extension to '.txt'
    t = text.get(0.0, END) # Assigns contents of window to 't'
    try: # In case of error, run fallback code
        f.write(t.rstrip()) # Trims trailing whitespace from 't', writes it to 'f'
    except: # If above code fails, print an error message
        showerror(title='Oops', message='Unable to save file.')

def openFile():
    f = askopenfile(mode='r') # Assign 'f' to open file dialogue in read mode
    t = f.read() # Assigns 't' to contents of file contained in 'f'
    text.delete(0.0, END) # Clears text in window
    text.insert(0.0, t) # Writes text in 't' to the window

root = Tk() # Standard code to begin assigning of Tkinter attributes
root.title('PyTE') # Title of window
root.minsize(width=400, height=400) # Minimum adjustable size
root.maxsize(width=400, height=400) # Maximum adjustable size
# Minimum and maximum size are the same, window cannot be resized
# The text covering a fixed rectangle causes the need for a constant window size

text = Text(root, width=400, height=400) # 'text' assigned to a text box, the same size as the window
text.pack() # "packs" the text into the size specified

menubar = Menu(root) # 'menubar' assigned to the Menu function of Tkinter
filemenu = Menu(menubar) # 'filemenu' is a sub-menu of 'menubar'
filemenu.add_command(label='New', command=newFile) # "New" option assigned to the 'newFile' function
filemenu.add_command(label='Open', command=openFile) # "Open" option assigned to the 'openFile' function
filemenu.add_command(label='Save', command=saveFile) # "Save" option assigned to the 'saveFile' function
filemenu.add_command(label='Save as', command=saveAs)# "Save as" option assigned to the 'saveAs' function
filemenu.add_separator() # A separator to keep the file manipulation options separate from the "Quit" option
filemenu.add_command(label='Quit', command=root.quit) # Assigns the built-in 'quit' function to "Quit" option
menubar.add_cascade(label='File', menu=filemenu) # Sets 'filemenu' and its nested menus to a drop-down labeled "File"

root.config(menu=menubar) # Configures the window, setting the menu to the 'menubar' variab;e
root.mainloop() # Begins loop over code, so the application refreshes and works
