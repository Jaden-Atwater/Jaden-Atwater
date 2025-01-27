from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Your personal grocery list :) ")
root.geometry("1000x550")

#Defining our font
my_font = Font(
    family = "Helvetica",
    size = 45,
    weight= "bold")
 
#creating my frame   
my_frame= Frame(root)
my_frame.pack(pady=10)

#creating my listbox
my_list = Listbox(my_frame,
    font= my_font,
    width= 25,
    height= 5,
    bg = "SystemButtonFace",
    bd = 0,
    fg = "#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

# Adding gorcery file
groceries = open("item_cost.txt")
#Adding a list base program
for item in groceries:
    my_list.insert(END, item)

#Creating a scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
    

#Adding the scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)


# create entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Functions
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
    
def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    # Getting rid of the bar under the text
    my_list.selection_clear(0, END)
        
def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    




# adding a button
delete_button = Button(button_frame, text="delete it", command=delete_item)
add_button = Button(button_frame, text="add it", command=add_item)
cross_off_button = Button(button_frame, text="Cross off item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross item", command=uncross_item)

delete_button.grid(row=1, column=0)
add_button.grid(row=1, column=1, padx=20)
cross_off_button.grid(row=1, column=2)
uncross_button.grid(row=1, column=3, padx=20)



root.mainloop() 