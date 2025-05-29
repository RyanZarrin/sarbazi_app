from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *
from sarbazi import Sarbazi


payankhedmat_list = read_from_file("payankhedmat.dat")


def load_data(payankhedmat_list):
    payankhedmat_list = read_from_file("payankhedmat.dat")
    for row in table.get_children():
        table.delete(row)

    for payankhedmat in payankhedmat_list:
        table.insert("", END, values=payankhedmat)


def reset_form():
    id.set(len(payankhedmat_list) + 1)
    serial_number.set("")
    start_date.set("")
    end_date.set("")
    city.set("")
    organ.set("")
    full_name.set("")
    load_data(payankhedmat_list)

def save_btn_click():
    payankhedmat = (id.get(), serial_number.get(), start_date.get(), end_date.get(), city.get(), organ.get(), full_name.get())
    errors = payankhedmat_validator(payankhedmat)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Person saved")
        payankhedmat_list.append(payankhedmat)
        write_to_file("payankhedmat.dat", payankhedmat_list)
        reset_form()


def table_select(x):
    selected_person = Sarbazi(*table.item(table.focus())["values"])
    if selected_person:
        id.set(selected_person.id)
        serial_number.set(selected_person.serial_number)
        start_date.set(selected_person.start_date)
        end_date.set(selected_person.end_date)
        city.set(selected_person.city)
        organ.set(selected_person.organ)
        full_name.set(selected_person.full_name)


def edit_btn_click():
    pass


def remove_btn_click():
    selected_person = (table.focus()[ "values" ])
    if selected_person:
        table.delete(selected_person)


window = Tk()
window.title("Person Info")
window.geometry("610x270")

# Id
Label(window, text="ID").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

# Serial number
Label(window, text="Serial Number").place(x=20, y=60)
serial_number = StringVar()
Entry(window, textvariable=serial_number).place(x=80, y=60)

# Start Date
Label(window, text="Start Date").place(x=20, y=100)
start_date = StringVar()
Entry(window, textvariable=start_date).place(x=80, y=100)

# End Date
Label(window, text="End Date").place(x=20, y=140)
end_date = IntVar()
Entry(window, textvariable=end_date).place(x=80, y=140)

# City
Label(window, text="City").place(x=20, y=180)
city = IntVar()
Entry(window, textvariable=city).place(x=80, y=180)

# Organ
Label(window, text="Organ").place(x=20, y=220)
organ = IntVar()
Entry(window, textvariable=organ).place(x=80, y=220)

# full_name
Label(window, text="Full Name").place(x=20, y=260)
full_name = IntVar(value=1)
Entry(window, textvariable=full_name).place(x=80, y=260)


table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6, 7], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Serial Number")
table.heading(3, text="Start Date")
table.heading(4, text="End Date")
table.heading(5, text="City")
table.heading(6, text="Organ")
table.heading(7, text="Full Name")

table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=170, y=350)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=110, y=350)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=50, y=350)
Button(window, text="Clear", width=6, command=reset_form).place(x=80, y=300, width=110)

reset_form()

window.mainloop()