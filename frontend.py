from tkinter import *
import backend
root = Tk()
root.title('library managing')

def clear_list():
    list1.delete(0, END)

def fill_list(books):
    for book in books:
        list1.insert(END, book)

lbl1 = Label(root, text='Title')
lbl1.grid(row=0, column=0)

lbl2 = Label(root, text='Author')
lbl2.grid(row=0, column=2)

lbl3 = Label(root, text='Year')
lbl3.grid(row=1, column=0)

lbl4 = Label(root, text='ISBN')
lbl4.grid(row=1, column=2)



title_text = StringVar
entry1 = Entry(root, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text = StringVar
entry2 = Entry(root, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text = StringVar
entry3 = Entry(root, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar
entry4 = Entry(root, textvariable=isbn_text)
entry4.grid(row=1, column=3)



list1 = Listbox(root, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)



scr1= Scrollbar(root)
scr1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scr1.set)
scr1.configure(command=list1.yview)

def get_selected_row(event):
    global selected_book
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_book[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_book[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_book[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_book[4])



list1.bind('<<ListboxSelect>>', get_selected_row)

def view_command():
    clear_list()
    books = backend.view()
    fill_list(books)

btn1 = Button(root, text='View All', width=12, command=view_command)
btn1.grid(row=2, column=3)

def search_command():
    clear_list()
    books = backend.search(entry1.get(), entry2.get(), entry3.get(), entry4.get())
    fill_list(books)

btn1 = Button(root, text='Search Entry', width=12, command=search_command)
btn1.grid(row=3, column=3)

def add_command():
    books = backend.insert(entry1.get(), entry2.get(), entry3.get(), entry4.get())
    view_command()

btn1 = Button(root, text='Add Entry', width=12, command=add_command)
btn1.grid(row=4, column=3)

def update_command():
    backend.update(selected_book[0], entry1.get(), entry2.get(), entry3.get(), entry4.get())
    view_command()

btn1 = Button(root, text='Update selected', width=12, command=update_command)
btn1.grid(row=5, column=3)


def delete_command():
    backend.delete(selected_book[0])
    view_command()

btn1 = Button(root, text='Delete Selected', width=12, command=delete_command)
btn1.grid(row=6, column=3)

btn1 = Button(root, text='Close', width=12, command=root.destroy)
btn1.grid(row=7, column=3)

view_command()

root.mainloop()