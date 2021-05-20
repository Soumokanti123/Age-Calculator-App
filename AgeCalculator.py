import datetime
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x700")
root.title("AGE CALCULATOR APP")
name = tk.Label(text="Name")
name.grid(column=0, row=1)
year = tk.Label(text="Year")
year.grid(column=0, row=2)
month = tk.Label(text="Month")
month.grid(column=0, row=3)
date = tk.Label(text="Date")
date.grid(column=0, row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)


def getInput():
    name = nameEntry.get()
    person = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
    textArea = tk.Text(master=root, height=10, width=25, bg="lightgreen")
    textArea.grid(column=1, row=6)
    answer = "Hey {person}!!!. You are {age} years old!!! ".format(person=name, age=person.age())
    textArea.insert(tk.END, answer)


button = tk.Button(root, text="Calculate Age", command=getInput, bg="lightblue")
button.grid(column=1, row=5)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


image = Image.open('unnamed.png')
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)
root.mainloop()
