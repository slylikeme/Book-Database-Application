"""
A program that stores this book information: Title, Author, Year, ISBN
=====================
User can:
View all records, Search an entry, Add entry, Update entry, Delete, Close program
"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import backend

# function tied to <<ListboxSelect>> event
def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox1.curselection()[0]
        selected_tuple = listbox1.get(index)
        e1.delete(0, tk.END)
        e1.insert(tk.END, selected_tuple[1])
        e2.delete(0, tk.END)
        e2.insert(tk.END, selected_tuple[2])
        e3.delete(0, tk.END)
        e3.insert(tk.END, selected_tuple[3])
        e4.delete(0, tk.END)
        e4.insert(tk. END, selected_tuple[4])
    except IndexError:
        pass


# populate the listbox
def view_command():
    listbox1.delete(0, tk.END)  # clear the box each time
    for row in backend.view():
        listbox1.insert(tk.END, row)

# search db wrapper function
def search_command():
    listbox1.delete(0, tk.END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox1.insert(tk.END, row)

# add book to wrapper function
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox1.delete(0, tk.END)
    listbox1.insert(tk.END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

# remove book from db wrapper function
def delete_command():
    backend.delete(selected_tuple[0])

# update book in db wrapper function
def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = tk.Tk()
window.title('Book Search')

# create labels that correspond to entry fields
l1 = tk.Label(window, text='Title')
l1.grid(row=0, column=0)
l2 = tk.Label(window, text='Author')
l2.grid(row=0, column=2)
l3 = tk.Label(window, text='Year')
l3.grid(row=1, column=0)
l4 = tk.Label(window, text='ISBN')
l4.grid(row=1, column=2)

# create entry fields that correspond to labels
title_text = tk.StringVar()
e1 = tk.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = tk.StringVar()
e2 = tk.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text = tk.StringVar()
e3 = tk.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
isbn_text = tk.StringVar()
e4 = tk.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# create listbox to list books
listbox1 = tk.Listbox(window, height=6, width=35)
listbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

# create scrollbar
scroll1 = tk.Scrollbar(window)
scroll1.grid(row=2, column=2, rowspan=6, sticky='nsw')

# configure scroll and listbox
listbox1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=listbox1.yview)

listbox1.bind('<<ListboxSelect>>', get_selected_row)

# create buttons
b1 = tk.Button(window, text='View all', width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = tk.Button(window, text='Search entry', width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = tk.Button(window, text='Add entry', width=12, command=add_command)
b3.grid(row=4, column=3)
b4 = tk.Button(window, text='Update selected', width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = tk.Button(window, text='Delete selected', width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = tk.Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
