# Age-Calculator-App
<strong>Age Calculator App Using Python Tkinter</strong>

##

![Image](unnamed.png)

##

<b>First things first, we need to import 3 libraries. The first one is the obvious one, which is tkinter. Then, we need datetime library to work with dates. Finally, we need PIL library which will help us to work with images.</b>
```ruby
import datetime
import tkinter as tk
from PIL import Image,ImageTk
```
<b>Now, let’s create a window for our app and name it as ‘Age Calculator App’.</b>
```ruby
root=tk.Tk()
root.geometry("620x780")
root.title(" Age Calculator App ")
```
<b>Now, create 4 labels, each for the name, year, month, and the date and put them in the grid.</b>
```ruby
name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date = tk.Label(text = "Day")
date.grid(column=0,row=4)
```
<b>For all the labels created, we will create corresponding entry fields in order to get the user inputs. Put them on the right side of corresponding labels using ‘grid’ method.</b>
```ruby
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)
```
<b>Let’s define a function to get the user inputs, called getInput(). Inside that, we create an object of the ‘Person‘ class (which will be defined later) and pass the name and birth date to ‘__init__‘ method of that class.

Note that we use the predefined ‘int()’ method to convert values into integer format. Then, we create a text area that will display the age of the user as output.</b>


