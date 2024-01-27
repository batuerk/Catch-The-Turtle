from tkinter import *

#Window
window = Tk()
window.title("Python Tkinter")
window.minsize(width=500, height=500)
window.config(pady=150)
number = ["0","1","2","3","4","5","6","7","8","9"]

def calculate_body_index():
    b = False
    c = False
    constant = 0
    for i in number:
        if b == False:
            print(i)
            for a in height_entry.get():
                if b == False:
                    print(a)
                    if i == a and b == False:
                        constant += 1

                        if constant == len(height_entry.get()):
                            h_value = int(height_entry.get())
                            w_value = int(weight_entry.get())
                            b = True
                            c = True
            
                            
                        else:
                            continue

                    else:
                        
                        continue 
                else:
                    break       
        else:
            break              
        
    if c == True:
        if h_value and w_value is not int:
            calculation = w_value / ((h_value * 0.01) **2)
    
            if calculation < 18.5:
                result_label.config(text="Your BMI is Underweight")               
            elif 18.5 < calculation < 24.9:
                result_label.config(text="Your BMI is Normal")
            elif 25 < calculation < 29.9:
                result_label.config(text="Your BMI is Overweight")
            elif 30 < calculation:
                result_label.config(text="Your BMI is Obese")

                          
            
    else:
        result_label.config(text="Please enter a valid number")               


#Weight
weight_label = Label(text="Enter Your Weight (kg)")
weight_label.pack()
weight_entry = Entry(width=15)
weight_entry.pack()


#Height
height_label = Label(text="Enter Your Height (cm)")
height_label.pack()
height_entry = Entry(width=15)
height_entry.pack()

#Button
calculate_button = Button(text="Calculate", command=calculate_body_index)
calculate_button.pack(pady=10)

#Result
result_label = Label()
result_label.pack()

window.mainloop()