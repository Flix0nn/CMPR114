import tkinter as tk
from tkinter import messagebox

def submit():
    lastname = lastname_entry.get()
    firstname = firstname_entry.get()
    
    if not lastname or not firstname:
        messagebox.showerror("Invalid Input", "Please enter both your last name and first name.")
        return
    
    if any(char.isdigit() for char in lastname) or any(char.isdigit() for char in firstname):
        messagebox.showerror("Invalid Input", "Please do not include numbers.")
        lastname_entry.delete(0, tk.END)
        firstname_entry.delete(0, tk.END)
        return

    answers = [
        option_var1.get(),
        option_var2.get(),
        option_var3.get(),
        option_var4.get(),
        option_var5.get()
    ]
    
    correct_answers = ["Option1", "Option3", "Option2", "Option1", "Option3"]
    
    score = sum(answer == correct_answer for answer, correct_answer in zip(answers, correct_answers))
    total_questions = len(correct_answers)
    
    grade = (score / total_questions) * 100
    grade = round(grade, 2)
    
    results = [answer == correct_answer for answer, correct_answer in zip(answers, correct_answers)]
    
    if all(results):
        message = "All answers are correct!"
    else:
        message = "Some answers are incorrect.\n"
        for i, result in enumerate(results):
            if not result:
                message += f"Question {i+1}: The correct answer is Option {correct_answers[i]}.\n"
    
    message += f"\nYour score is {score}/{total_questions} ({grade}%)"
    
    messagebox.showinfo("Result", f"{firstname} {lastname} received a {grade}% test score")
    
    with open("Final Exam/Part 2/Data.txt", "a") as file:
        file.write(f"Last Name: {lastname}\n")
        file.write(f"First Name: {firstname}\n")
        file.write(f"Score: {score}/{total_questions}\n")
        file.write(f"Grade: {grade}%\n")
        file.write("\n")

window = tk.Tk()
window.geometry('400x750+520+25')
window.title("Test")

window_color = 'lightblue'
border_color = '#4682B4'
text_color = '#4682B4'
window.configure(bg=window_color)

option_var1 = tk.StringVar()
option_var2 = tk.StringVar()
option_var3 = tk.StringVar()
option_var4 = tk.StringVar()
option_var5 = tk.StringVar()

lastname_label = tk.Label(window, text="Last Name", bg=window_color)
lastname_label.pack(pady=5)
lastname_entry = tk.Entry(window, bg=window_color, fg=text_color, bd=0, highlightbackground=border_color, highlightcolor=border_color)
lastname_entry.pack(pady=5)

firstname_label = tk.Label(window, text="First Name", bg=window_color)
firstname_label.pack(pady=5)
firstname_entry = tk.Entry(window, bg=window_color, fg=text_color, bd=0, highlightbackground=border_color, highlightcolor=border_color)
firstname_entry.pack(pady=5)

#--------------------------------------------------------------------------------------------------------------------------------------
question1 = tk.Label(window, text="Question 1: Who was our Profesor for CMPR114?", bg=window_color)
question1.pack(pady=5)

tk.Radiobutton(window, text="Jason Sim", bg=window_color, fg=text_color, variable=option_var1, value="Option1").pack(anchor=tk.W)
tk.Radiobutton(window, text="Thomas Jefferson", bg=window_color, fg=text_color, variable=option_var1, value="Option2").pack(anchor=tk.W)
tk.Radiobutton(window, text="Rowley Jefferson", bg=window_color, fg=text_color, variable=option_var1, value="Option3").pack(anchor=tk.W)

#--------------------------------------------------------------------------------------------------------------------------------------
question2 = tk.Label(window, text="Question 2: What Programing Language did we learn in CMPR114?", bg=window_color)
question2.pack(pady=5)

tk.Radiobutton(window, text="Brain F**k", bg=window_color, fg=text_color, variable=option_var2, value="Option1").pack(anchor=tk.W)
tk.Radiobutton(window, text="JavaScript", bg=window_color, fg=text_color, variable=option_var2, value="Option2").pack(anchor=tk.W)
tk.Radiobutton(window, text="Python", bg=window_color, fg=text_color, variable=option_var2, value="Option3").pack(anchor=tk.W)

#--------------------------------------------------------------------------------------------------------------------------------------
question3 = tk.Label(window, text="Question 3: Exercise I thought you said...", bg=window_color)
question3.pack(pady=5)

tk.Radiobutton(window, text="Extra price", bg=window_color, fg=text_color, variable=option_var3, value="Option1").pack(anchor=tk.W)
tk.Radiobutton(window, text="Extra fries", bg=window_color, fg=text_color, variable=option_var3, value="Option2").pack(anchor=tk.W)
tk.Radiobutton(window, text="Extra prize", bg=window_color, fg=text_color, variable=option_var3, value="Option3").pack(anchor=tk.W)

#--------------------------------------------------------------------------------------------------------------------------------------
question4 = tk.Label(window, text="Question 4: What do you call cheese that isn't yours?", bg=window_color)
question4.pack(pady=5)

tk.Radiobutton(window, text="Nacho cheese", bg=window_color, fg=text_color, variable=option_var4, value="Option1").pack(anchor=tk.W)
tk.Radiobutton(window, text="Cheese that isnt yours", bg=window_color, fg=text_color, variable=option_var4, value="Option2").pack(anchor=tk.W)
tk.Radiobutton(window, text="Not funny didnt laugh", bg=window_color, fg=text_color, variable=option_var4, value="Option3").pack(anchor=tk.W)

#--------------------------------------------------------------------------------------------------------------------------------------
question5 = tk.Label(window, text="A particle of mass m starts from rest and is subjected \n to a variable force F(x) = kx^2, where k is a positive constant \n and x is the displacement from the origin. Determine the \n velocity of the particle when it reaches a position x = d.", bg=window_color)
question5.pack(pady=5)

tk.Radiobutton(window, text="um what", bg=window_color, fg=text_color, variable=option_var5, value="Option1").pack(anchor=tk.W)
tk.Radiobutton(window, text="idk the answer blawg", bg=window_color, fg=text_color, variable=option_var5, value="Option2").pack(anchor=tk.W)
tk.Radiobutton(window, text="vd = square root of 2kd^3/3m.", bg=window_color, fg=text_color, variable=option_var5, value="Option3").pack(anchor=tk.W)

#--------------------------------------------------------------------------------------------------------------------------------------
submit_button = tk.Button(window, text="Submit", command=submit, bg=window_color, fg=text_color,
                         highlightbackground=window_color, highlightcolor=window_color)
submit_button.pack(pady=10)

window.mainloop()
