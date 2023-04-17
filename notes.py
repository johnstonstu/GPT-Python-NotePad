import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


def save_note():
    note = note_entry.get(1.0, "end-1c")
    if note:
        with open("notes.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{note} ({timestamp})\n")
        note_entry.delete(1.0, "end")
        messagebox.showinfo("Note Taker", "Note has been saved.")
    else:
        messagebox.showerror("Note Taker", "Cannot save empty note.")


def view_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            notes = [line.strip() for line in f.readlines()]
            if notes:
                # create new window
                view_window = tk.Toplevel(root)
                view_window.title("View Notes")
                view_window.geometry("400x300")

                # create treeview to display notes
                notes_treeview = ttk.Treeview(view_window, columns=("timestamp"))
                notes_treeview.heading("#0", text="Note")
                notes_treeview.heading("timestamp", text="Timestamp")
                notes_treeview.column("timestamp", width=150)
                notes_treeview.pack(fill="both", expand=True)

                # insert notes into treeview
                for note in notes:
                    note_text, timestamp = note.split(" (")
                    timestamp = timestamp[:-1]
                    notes_treeview.insert("", "end", text=note_text, values=timestamp)
                    notes_treeview.item(notes_treeview.get_children()[-1], open=True)
            else:
                messagebox.showwarning("Note Taker", "No notes found.")
    except FileNotFoundError:
        messagebox.showwarning("Note Taker", "No notes found.")


root = tk.Tk()
root.title("Note Taker")
root.geometry("400x300")

# create label and entry for note input
note_label = tk.Label(root, text="Enter note:")
note_label.pack()
note_entry = tk.Text(root, height=5)
note_entry.pack()

# create save and view buttons
save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.pack(pady=10)
view_button = tk.Button(root, text="View Notes", command=view_notes)
view_button.pack(pady=10)

root.mainloop()
