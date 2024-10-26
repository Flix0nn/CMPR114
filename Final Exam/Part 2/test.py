import tkinter as tk
from tkinter import messagebox

def submit_answers():
    question1_answer = question1_var.get()  # Get the selected value for Question 1
    question2_answer = question2_var.get()  # Get the selected value for Question 2

    messagebox.showinfo("Selected Answers", 
                        f"Question 1 Answer: {question1_answer}\nQuestion 2 Answer: {question2_answer}")

# Create the main window
window = tk.Tk()
window.title("Answer the Questions")

# Create Tkinter variables to hold the selected values for each question
question1_var = tk.StringVar(value="Option1A")  # Default value for Question 1
question2_var = tk.StringVar(value="Option2A")  # Default value for Question 2

# Create and place labels and radio buttons for Question 1
question1_label = tk.Label(window, text="Question 1: What is your favorite color?")
question1_label.pack(pady=5)

tk.Radiobutton(window, text="Red", variable=question1_var, value="Red").pack(anchor=tk.W)
tk.Radiobutton(window, text="Blue", variable=question1_var, value="Blue").pack(anchor=tk.W)
tk.Radiobutton(window, text="Green", variable=question1_var, value="Green").pack(anchor=tk.W)

# Create and place labels and radio buttons for Question 2
question2_label = tk.Label(window, text="Question 2: What is your favorite animal?")
question2_label.pack(pady=5)

tk.Radiobutton(window, text="Cat", variable=question2_var, value="Cat").pack(anchor=tk.W)
tk.Radiobutton(window, text="Dog", variable=question2_var, value="Dog").pack(anchor=tk.W)
tk.Radiobutton(window, text="Bird", variable=question2_var, value="Bird").pack(anchor=tk.W)

# Create and place the Submit button
submit_button = tk.Button(window, text="Submit", command=submit_answers)
submit_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
