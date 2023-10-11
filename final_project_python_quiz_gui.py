"""
Harper Morgan FA23 SDEV 140
Quiz Game Using Python Tinker
FINAL PROJECT
"""
from tkinter import *
from tkinter import ttk
y = 0
a = ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)


root = ttk.Frame(a)

def quiz(a):
    a.add(frame1, text = "Q1")
    a.add(frame2, text = "Q2")
    a.add(frame3, text = "Q3")
    a.add(frame4, text = "Q4")
    a.add(frame5, text = "Q5")

    Label(frame1, text = "Which keyword allows us to load a module in Python? ", \
           font = ("Arial", 50, "bold")).grid(row = 2, column = 2)
    Button(frame1, text = "Import",font = ("Arial", 50, "bold"), bg = "light pink").grid(row = 3, column = 1) # correct answer
    Button(frame1, text = "Library",font = ("Arial", 50, "bold"), bg = "light blue").grid(row = 3, column = 2)
    Button(frame1, text = "Load",font = ("Arial", 50, "bold"), bg = "light green").grid(row = 3, column = 3)
      
    Label(frame2, text = "Which one from the following objects in Python is immutable? ", \
           font = ("Arial", 50, "bold")).grid(row = 2, column = 2)
    Button(frame2, text = "Lists",font = ("Arial", 50, "bold"), bg = "light pink").grid(row = 3, column = 1)
    Button(frame2, text = "Set(s)",font = ("Arial", 50, "bold"), bg = "light blue").grid(row = 3, column = 2)
    Button(frame2, text = "Tuple",font = ("Arial", 50, "bold"), bg = "light green").grid(row = 3, column = 3) # correct answer

    Label(frame3, text = "Give the output of the following code: <pre code = 'Python>a = 'Python Quiz' print (a[2:5]) </pre> ", \
           font = ("Arial", 50, "bold")).grid(row = 2, column = 2)
    Button(frame3, text = "ytho",font = ("Arial", 50, "bold"), bg = "light pink").grid(row = 3, column = 1) # correct answer
    Button(frame3, text = "thon",font = ("Arial", 50, "bold"), bg = "light blue").grid(row = 3, column = 2)
    Button(frame3, text = "tho",font = ("Arial", 50, "bold"), bg = "light green").grid(row = 3, column = 3)      

    Label(frame4, text = "Which function can add elements to the end of a list? ", \
           font = ("Arial", 50, "bold")).grid(row = 2, column = 2)
    Button(frame4, text = "append()",font = ("Arial", 50, "bold"), bg = "light pink").grid(row = 3, column = 1) # correct answer
    Button(frame4, text = "insert()",font = ("Arial", 50, "bold"), bg = "light blue").grid(row = 3, column = 2)
    Button(frame4, text = "Add()",font = ("Arial", 50, "bold"), bg = "light green").grid(row = 3, column = 3)

    Label(frame5, text = "Give the output of the following code: for i in range(0,10,3): print(i) ", \
           font = ("Arial", 50, "bold")).grid(row = 2, column = 2)
    Button(frame5, text = "0 3 6 9",font = ("Arial", 50, "bold"), bg = "light pink").grid(row = 3, column = 1) # correct answer
    Button(frame5, text = "1 4 7 10",font = ("Arial", 50, "bold"), bg = "light blue").grid(row = 3, column = 2)
    Button(frame5, text = "1 3 5 7 9",font = ("Arial", 50, "bold"), bg = "light green").grid(row = 3, column = 3)

    def a_correct():
        Label(frame1)

quiz(a)




root.mainloop()

