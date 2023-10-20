import tkinter as tk
from tkinter import ttk
from part1 import function1
from part2 import function2
from part3 import function3
from part4 import function4

def call_function_1():
    result_label.config(text=function1())
    
def call_function_2():
    result_label.config(text=function2())

def call_function_3():
    result_label.config(text=function3())

def call_function_4():
    result_label.config(text=function4())    


# Create the main window with a specific size
window = tk.Tk()
window.title("")
window.geometry("500x450+370+80")  # Set window size
window.resizable(False, False)

# Create a style for ttk widgets
style = ttk.Style()
style.configure("TButton", foreground="light grey", background="red", font=("Arial", 12, "bold"))
style.configure("TLabel", foreground="black", font=("Arial", 15, "bold"))




# Create a label for the title with big and bold letters
title_label = ttk.Label(window, text="Radar System Classification", foreground="black", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=(20, 0),padx=60)


# Create a frame for each button with a label to the side
frame1 = ttk.Frame(window)
frame1.grid(row=1, column=0, padx=20, pady=30)

frame2 = ttk.Frame(window)
frame2.grid(row=2, column=0, padx=20, pady=30)

frame3 = ttk.Frame(window)
frame3.grid(row=3, column=0, padx=20, pady=30)

frame4 = ttk.Frame(window)
frame4.grid(row=4, column=0, padx=20, pady=30)

# Create labels to the left of buttons with space in between
label1 = ttk.Label(frame1, text="Data Generation ", font=("Arial", 12))
label1.pack(side="left",padx=31)

button1 = ttk.Button(frame1, text="Step 1",cursor="hand2",command=call_function_1)
button1.pack(side="right")

label2 = ttk.Label(frame2, text="Data Classification 1 ", font=("Arial", 12))
label2.pack(side="left",padx=17)

button2 = ttk.Button(frame2, text="Step 2",cursor="hand2", command=call_function_2)
button2.pack(side="right")

label3 = ttk.Label(frame3, text="Data Classification 2 ", font=("Arial", 12))
label3.pack(side="left",padx=17)

button3 = ttk.Button(frame3, text="Step 3",cursor="hand2", command=call_function_3)
button3.pack(side="right")

label4 = ttk.Label(frame4, text="Related Data Identification ", font=("Arial", 12))
label4.pack(side="left")

button4 = ttk.Button(frame4, text="Step 4",cursor="hand2", command=call_function_4)
button4.pack(side="right")

# Create a label for displaying results
result_label = ttk.Label(window, text="", foreground="black", font=("Arial", 12))
result_label.grid(row=1, column=1, rowspan=3, columnspan=2, padx=20, pady=20)

# Start the Tkinter main loop
window.mainloop()