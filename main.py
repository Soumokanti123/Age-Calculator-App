import tkinter as tk


def doorbell(event):
    print("You rang the Doorbell")


# creating window
root = tk.Tk()
root.title("DOORBELL APP")
root.geometry("300x200")
# creating Labelmylabel = tk.Label(text="OpenAI is the Future Technologies")
# # mylabel.grid(column=0, row=0)
mybutton = tk.Button(root, text="Doorbell")
mybutton.grid(column=1, row=1)
mybutton.bind("<Button-1>", doorbell)
# We made a button called mybutton.
# Then, we bound it to the window of the app using the bind method.
# The bind method has two parameters.
#
# The first parameter <Button-1> is the left click short key of the mouse.
# When you left-click the button with the mouse, then the event occurs.
# The second parameter is the name of the event function.
root.mainloop()
