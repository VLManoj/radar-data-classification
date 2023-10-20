import tkinter as tk
import random
import openpyxl
from tkinter import filedialog
from tkinter import ttk


def function1():
    def generate_inputs_and_save():
        try:
            min_frequency = float(min_frequency_entry.get())
            max_frequency = float(max_frequency_entry.get())
            min_pri = float(min_pri_entry.get())
            max_pri = float(max_pri_entry.get())
            min_pulse_width = float(min_pulse_width_entry.get())
            max_pulse_width = float(max_pulse_width_entry.get())
        except ValueError:
            result_label.config(text="Invalid input. Please enter valid numbers.")
            return

        if min_frequency >= max_frequency or min_pri >= max_pri or min_pulse_width >= max_pulse_width:
            result_label.config(text="Min range should be less than max range for all three specifications.")
            return

        # Generate random data
        radar_data = []
        for _ in range(10000):
            frequency = random.uniform(min_frequency, max_frequency)
            pri = random.uniform(min_pri, max_pri)
            pulse_width = random.uniform(min_pulse_width, max_pulse_width)

            # Round the values to two decimal places
            frequency = round(frequency, 2)
            pri = round(pri, 2)
            pulse_width = round(pulse_width, 2)

            radar_data.append([frequency, pri, pulse_width])

        try:
            # Ask the user to choose a directory to save the file
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

            if file_path:
                # Create a new Excel workbook and add data to it
                workbook = openpyxl.Workbook()
                worksheet = workbook.active

                # Add headers
                worksheet.append(["Frequency (Hz)", "PRI (s)", "Pulse Width (s)"])

                # Add data to three columns
                for row in radar_data:
                    worksheet.append(row)

                # Save the workbook to the chosen file path
                workbook.save(file_path)
                result_label.config(text=f"Generated 10000 data points and saved to '{file_path}'.")
        except Exception as e:
            result_label.config(text=f"Error saving to Excel: {str(e)}")

    # Create the main window
    window = tk.Tk()
    window.title("Radar Specifications")

    # Set the window size
    window.geometry("600x400+320+200")
    window.resizable(True, True)

    lbl = tk.Label(window, text="Radar Parameters", font=("times new roman", 30, 'bold'), fg='blue')
    lbl.place(relx=0.3, rely=0.03)

    # Create a frame for the input fields and button
    frame = ttk.Frame(window, borderwidth=5, relief="solid", style="My.TFrame")
    frame.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)

    # Configure frame background color to a light blue-gray
    style = ttk.Style()
    style.configure("My.TFrame", background="#E0E8E8")

    # Create and place widgets for the Frequency
    ttk.Label(frame, text="Frequency (MHz):", font=("times new roman", 15)).place(relx=0.40, rely=0.05)
    min_frequency_entry = ttk.Entry(frame)
    min_frequency_entry.place(relx=0.2, rely=0.20)
    frelbl = tk.Label(frame, text="Min Range:")
    frelbl.place(relx=0.05, rely=0.20)
    max_frequency_entry = ttk.Entry(frame)
    max_frequency_entry.place(relx=0.7, rely=0.20)
    frelbl1 = tk.Label(frame, text="Max Range:")
    frelbl1.place(relx=0.55, rely=0.20)

    # Create and place widgets for the PRI
    ttk.Label(frame, text="PRI (s):", font=("times new roman", 15)).place(relx=0.42, rely=0.30)
    min_pri_entry = ttk.Entry(frame)
    min_pri_entry.place(relx=0.2, rely=0.40)
    prilbl = tk.Label(frame, text="Min Range:")
    prilbl.place(relx=0.05, rely=0.40)
    max_pri_entry = ttk.Entry(frame)
    max_pri_entry.place(relx=0.7, rely=0.40)
    prilbl1 = tk.Label(frame, text="Max Range:")
    prilbl1.place(relx=0.55, rely=0.40)

    # Create and place widgets for the pulse width
    ttk.Label(frame, text="Pulse Width (s):", font=("times new roman", 15)).place(relx=0.4, rely=0.50)
    min_pulse_width_entry = ttk.Entry(frame)
    min_pulse_width_entry.place(relx=0.2, rely=0.60)
    pwilbl = tk.Label(frame, text="Min Range:")
    pwilbl.place(relx=0.05, rely=0.60)
    max_pulse_width_entry = ttk.Entry(frame)
    max_pulse_width_entry.place(relx=0.7, rely=0.60)
    pwilbl1 = tk.Label(frame, text="Max Range:")
    pwilbl1.place(relx=0.55, rely=0.60)

    # Create a button to generate and save data
    generate_button = ttk.Button(frame, text="Generate", command=generate_inputs_and_save)

    # Configure button style for hover effect
    generate_button.configure(style="Hover.TButton")
    generate_button.place(relx=0.70, rely=0.75, height=40, width=130)

    # Create a style for the button hover effect
    style.configure("Hover.TButton", background="#90EE90")

    # Create a label for displaying results
    result_label = ttk.Label(frame, text="", foreground="black", background="#E0E8E8")
    result_label.place(relx=0.05, rely=0.89)

    # Start the Tkinter main loop
    window.mainloop()


