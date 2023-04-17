from tkinter import *

# create a function to save the note to a file
def save_note():
    note = text_box.get(1.0, END)
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    text_box.delete(1.0, END)

# create a function to view the saved notes
def view_notes():
    with open("notes.txt", "r") as file:
        notes = file.read()
    notes_window = Toplevel(root)
    notes_window.title("Saved Notes")
    notes_text = Text(notes_window, height=10, width=50)
    notes_text.pack()
    notes_text.insert(END, notes)

# create the GUI
root = Tk()
root.title("Note Taking App")

# create a text box for the user to input their note
text_box = Text(root, height=10, width=50)
text_box.pack()

# create a save button that saves the note to a file when clicked
save_button = Button(root, text="Save", command=save_note)
save_button.pack()

# create a view button that opens a new window with the saved notes
view_button = Button(root, text="View Notes", command=view_notes)
view_button.pack()

# start the main loop of the program
root.mainloop()
