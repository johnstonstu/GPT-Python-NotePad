from tkinter import *
from tkinter import ttk
from datetime import datetime

notes = []


def save_note():
    note = note_entry.get(1.0, END)
    notes.append((note, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    note_entry.delete(1.0, END)


def view_notes():
    notes_window = Toplevel(root)
    notes_window.title("Saved Notes")
    notes_window.geometry("500x400")

    notes_treeview = ttk.Treeview(notes_window)
    notes_treeview.pack(expand=YES, fill=BOTH)

    notes_treeview["columns"] = ("note", "timestamp")
    notes_treeview.column("#0", width=0, stretch=NO)
    notes_treeview.column("note", anchor=W, width=400)
    notes_treeview.column("timestamp", anchor=W, width=100)

    notes_treeview.heading("#0", text="", anchor=W)
    notes_treeview.heading("note", text="Note", anchor=W)
    notes_treeview.heading("timestamp", text="Timestamp", anchor=W)

    for i, note in enumerate(notes):
        notes_treeview.insert(parent="", index=i, text="", values=(note[0], note[1]))

    def edit_note():
        selected_item = notes_treeview.selection()
        if selected_item:
            item_text = notes_treeview.item(selected_item, "values")[0]
            edit_window = Toplevel(notes_window)
            edit_window.title("Edit Note")
            edit_window.geometry("500x400")

            edit_note_entry = Text(edit_window, wrap=WORD)
            edit_note_entry.pack(expand=YES, fill=BOTH)
            edit_note_entry.insert(INSERT, item_text)

            def save_edited_note():
                edited_note = edit_note_entry.get(1.0, END)
                notes_treeview.item(selected_item, values=(edited_note, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                edit_window.destroy()

            edit_note_button = Button(edit_window, text="Save", command=save_edited_note)
            edit_note_button.pack()

    edit_note_button = Button(notes_window, text="Edit", command=edit_note)
    edit_note_button.pack()

root = Tk()
root.title("Note Taker")

note_entry = Text(root, wrap=WORD)
note_entry.pack(expand=YES, fill=BOTH)

save_button = Button(root, text="Save", command=save_note)
save_button.pack()

view_notes_button = Button(root, text="View Notes", command=view_notes)
view_notes_button.pack()

root.mainloop()
