from tkinter import *

#Initial window creation
window = Tk()
window.title("Miles to kilometer converter")
window.config(padx=20,pady=20)

#Function to bind the calculate method
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

#Labels
#Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0,padx=10,pady=10)

#Equal to Label
is_equal_label= Label(text="is equal to ")
is_equal_label.grid(column=0,row=1)

#Result Label
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

#Km Label
kilometer_label = Label(text="Km")
kilometer_label.grid(column= 2, row=1)


#Entry
miles_input = Entry()
miles_input.grid(column=1,row=0)


#Buttton label 
#Calculate
calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=2,column=1)

window.mainloop()