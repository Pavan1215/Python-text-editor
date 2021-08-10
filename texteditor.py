from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title('PQUAD TEXT EDITOR !!!')
root.geometry("1200x680")

# set variable for open file name
global open_status_name
open_status_name=False

global selected
selected=False

# create new file function
def new_file():
    my_text.delete("1.0", END)
    root.title("New File -PQUAD!")
    status_bar.config(text="New File        ")
    global open_status_name
    open_status_name=False
    
# create open file function
def open_file():
    my_text.delete("1.0", END)
    
    # grab file name
    text_file=filedialog.askopenfilename(initialdir="E:/Programs/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),("Python Files", "*.py"), ("C File", "*.c"), ("Java Files", "*.java"), ("All files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name=text_file
        
    name = text_file
    status_bar.config(text=f'{name}         ')
    name = name.replace("E:/Programs/", "")
    root.title(f'{name} - PQUAD Text editor')
    
    # open the file
    text_file=open(text_file, 'r')
    stuff=text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

# create save as function
def save_as_file():
    text_file= filedialog.asksaveasfilename(defaultextension=".*", initialdir="E:/programs/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),("Python Files", "*.py"), ("C File", "*.c"), ("Java Files", "*.java"), ("All files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("E:/programs/", "")
        root.title(f'{name} - PQUAD Text editor')
        
        #save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        #close file
        text_file.close()

# create save file function
def save_file():
    global open_status_name
    if open_status_name:
        #save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        #close file
        text_file.close()
        status_bar.config(text=f'Saved: {open_status_name}        ')
    else:
        save_as_file()
                

#create cut function
def cut_text(e):
        global selected
        #check see if used keyboard shortcut
        if e:
                selected=root.clipboard_get()
        else:
                if my_text.selection_get():
                        #grab selected text from text box
                        selected=my_text.selection_get()
                        #delete selected text from text box
                        my_text.delete("sel.first", "sel.last")
                        root.clipboard_clear()
                        root.clipboard_append(selected)
        
                
#create copy function
def copy_text(e):
        global selected
        #check see if used keyboard shortcut
        if e:
                selected=root.clipboard_get()
        
        if my_text.selection_get():
                #grab selected text from text box
                selected=my_text.selection_get()
                #clear clipboard and append
                root.clipboard_clear()
                root.clipboard_append(selected)

#create paste function
def paste_text(e):
        global selected
        #cjheck if there is keyboard shortcut is used
        if e:
                selected=root.clipboard_get()
        else:
                        
                if selected:
                        position = my_text.index(INSERT)
                        my_text.insert(position, selected)
        
#create bold and italics function
def bold_text():
        bold_font=font.Font(my_text, my_text.cget("font"))
        bold_font.configure(weight="bold")
        #configure tag
        my_text.tag_configure("bold", font=bold_font)
        current_tags=my_text.tag_names("sel.first")
        
        #if statement to see if tag is set
        if "bold" in current_tags:
                my_text.tag_remove("bold", "sel.first", "sel.last")
        else:
                my_text.tag_add("bold", "sel.first", "sel.last")
                

def italic_text():
        italic_font=font.Font(my_text, my_text.cget("font"))
        italic_font.configure(slant="italic")
        #configure tag
        my_text.tag_configure("italic", font=italic_font)
        current_tags=my_text.tag_names("sel.first")
        
        #if statement to see if tag is set
        if "italic" in current_tags:
                my_text.tag_remove("italic", "sel.first", "sel.last")
        else:
                my_text.tag_add("italic", "sel.first", "sel.last")


# function to change text color

def text_color():
        
        #pick a color
        my_color=colorchooser.askcolor()[1]
        if my_color:
                
                color_font=font.Font(my_text, my_text.cget("font"))
                
                #configure tag
                my_text.tag_configure("colored", font=color_font, foreground=my_color)
                current_tags=my_text.tag_names("sel.first")
                
                #if statement to see if tag is set
                if "colored" in current_tags:
                        my_text.tag_remove("colored", "sel.first", "sel.last")
                else:
                        my_text.tag_add("colored", "sel.first", "sel.last")
        

#function to change bg color

def bg_color():
        my_color=colorchooser.askcolor()[1]
        if my_color:
                my_text.config(bg=my_color)
                
#function to change all text color

def all_text_color():
        my_color=colorchooser.askcolor()[1]
        if my_color:
                my_text.config(fg=my_color)
               
#select all text function
def select_all(e):
        #add sel tag to select all text
        my_text.tag_add('sel', '1.0', 'end')

#clear all text
def clear_all():
        my_text.delete(1.0, END)

#create nightmode function
def nightmode_on():
        main_color="#000000"
        second_color="#373737"
        text_color="green"
        
        root.config(bg=main_color)
        status_bar.config(bg=main_color, fg=text_color)
        my_text.config(bg=second_color)
        toolbar_frame.config(bg=main_color)
        #toolbar buttons
        bold_button.config(bg=second_color)
        italic_button.config(bg=second_color)
        color_text_button.config(bg=second_color)
        #file menu colors
        file_menu.config(bg=main_color, fg=text_color)
        edit_menu.config(bg=main_color, fg=text_color)
        color_menu.config(bg=main_color, fg=text_color)
        options_menu.config(bg=main_color, fg=text_color)

def nightmode_off():
        main_color="SystemButtonFace"
        second_color="SystemButtonFace"
        text_color="black"
        
        root.config(bg=main_color)
        status_bar.config(bg=main_color, fg=text_color)
        my_text.config(bg="white")
        toolbar_frame.config(bg=main_color)
        #toolbar buttons
        bold_button.config(bg=second_color)
        italic_button.config(bg=second_color)
        color_text_button.config(bg=second_color)
        #file menu colors
        file_menu.config(bg=main_color, fg=text_color)
        edit_menu.config(bg=main_color, fg=text_color)
        color_menu.config(bg=main_color, fg=text_color)
        options_menu.config(bg=main_color, fg=text_color)

#create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)


        
# create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# create scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
hor_scroll=Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)
#create text box
my_text = Text(my_frame, selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set ,width=97, height=25, font=("Helvetica", 16), wrap='none')
my_text.pack()

# configure our scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# create menu
my_menu= Menu(root)
root.config(menu=my_menu)

#add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu )
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#add edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu )
edit_menu.add_command(label="Cut     ctrl+x", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy    ctrl+c", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste   ctrl+v", command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo)
edit_menu.add_command(label="Redo", command=my_text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Select All   ctrl+A", command=lambda: select_all(True))
edit_menu.add_command(label="Clear All", command=clear_all)


#add color menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu )
color_menu.add_command(label="Change Selected Text", command=text_color)
color_menu.add_command(label="All text", command=all_text_color)
color_menu.add_command(label="Change background color", command=bg_color)

#create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu )
options_menu.add_command(label="Nightmode On", command=nightmode_on)
options_menu.add_command(label="Nightmode Off", command=nightmode_off)
# add status bar
status_bar= Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

#edit bindings(synchro cut-copy-paste keyboaard shortcuts with menu functions)
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('Control-A', select_all)

#create button for bold and italics
bold_button = Button(toolbar_frame, text="Bold", command=bold_text)
bold_button.grid(row=0, column=0, sticky=W, padx=5)

italic_button = Button(toolbar_frame, text="Italics", command=italic_text)
italic_button.grid(row=0, column=1, sticky=W, padx=5)

# create text color button
color_text_button=Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=2, padx=5)

root.mainloop()