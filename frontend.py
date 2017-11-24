#! python3

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
from backend import Database

database = Database('books.db')

class Window(object):

    def __init__(self, window):

        self.window = window
        self.window.title('Book Search')

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
        self.title_text = tk.StringVar()
        self.e1 = tk.Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)
        self.author_text = tk.StringVar()
        self.e2 = tk.Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)
        self.year_text = tk.StringVar()
        self.e3 = tk.Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)
        self.isbn_text = tk.StringVar()
        self.e4 = tk.Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        # create listbox to list books
        self.listbox1 = tk.Listbox(window, height=6, width=35)
        self.listbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # create scrollbar
        self.scroll1 = tk.Scrollbar(window)
        self.scroll1.grid(row=2, column=2, rowspan=6, sticky='nsw')

        # configure scroll and listbox
        self.listbox1.configure(yscrollcommand=self.scroll1.set)
        self.scroll1.configure(command=self.listbox1.yview)

        self.listbox1.bind('<<ListboxSelect>>', self.get_selected_row)

        # create buttons
        self.b1 = tk.Button(window, text='View all', width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)
        self.b2 = tk.Button(window, text='Search entry', width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)
        self.b3 = tk.Button(window, text='Add entry', width=12, command=self.add_command)
        self.b3.grid(row=4, column=3)
        self.b4 = tk.Button(window, text='Update selected', width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)
        self.b5 = tk.Button(window, text='Delete selected', width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)
        self.b6 = tk.Button(window, text='Close', width=12, command=self.window.destroy)
        self.b6.grid(row=7, column=3)


    # function tied to <<ListboxSelect>> event
    def get_selected_row(self, event):
        try:
            # global selected_tuple
            index = self.listbox1.curselection()[0]
            self.selected_tuple = self.listbox1.get(index)
            self.e1.delete(0, tk.END)
            self.e1.insert(tk.END, self.selected_tuple[1])
            self.e2.delete(0, tk.END)
            self.e2.insert(tk.END, self.selected_tuple[2])
            self.e3.delete(0, tk.END)
            self.e3.insert(tk.END, self.selected_tuple[3])
            self.e4.delete(0, tk.END)
            self.e4.insert(tk. END, self.selected_tuple[4])
        except IndexError:
            pass


    # populate the listbox
    def view_command(self):
        self.listbox1.delete(0, tk.END)  # clear the box each time
        for row in database.view():
            self.listbox1.insert(tk.END, row)

    # search db wrapper function
    def search_command(self):
        self.listbox1.delete(0, tk.END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.listbox1.insert(tk.END, row)

    # add book to wrapper function
    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.listbox1.delete(0, tk.END)
        self.listbox1.insert(tk.END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    # remove book from db wrapper function
    def delete_command(self):
        database.delete(self.selected_tuple[0])

    # update book in db wrapper function
    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

window = tk.Tk()
Window(window)

window.mainloop()
