#import imghdr
from cProfile import label
from email.mime import image
from operator import ge
from tkinter import *
from tkinter import messagebox
from tkinter.tix import IMAGETEXT
from PIL import ImageTk, Image


#from PIL import Image, ImageTk
#from tkinter.ttk import *
def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('easy BMI', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('easy BMI', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('easy BMI', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('easy BMI', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('easy BMI', 'something went wrong!')   

bm = Tk()

bm.title('easy BMI')

bm.config(bg='black')
bm.geometry("350x400")
var = IntVar()

frame = Frame(bm, width=1000, height=800)
frame.pack(expand= True)
frame.place(anchor='center', relx=0.5, rely=0.5)

img= (Image.open("rrr.jpg"))

resized_image= img.resize((1000,1000), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

label = Label(frame, image = new_image)
label.pack()


#img = ImageTk.PhotoImage(Image.open("myproject\sr.jpg"))

#label = Label(frame, image = img)
#label.pack()




age_lb = Label(
    label,
    text="   Enter Age   ",font=('calibre') ,bg="#E549B9"
)
age_lb.pack()
age_lb.grid(row = 1, column = 1 , pady=25, padx=25)

age_tf = Entry(
    label, 
)
age_tf.grid(row=1, column=2, pady=25, padx=25)

gen_lb = Label(
    label,
    text="     Gender     ",font=('calibre'),bg="#E389B9"
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    label
)
frame2.grid(row=2, column=2,pady=25, padx=25)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    label,
    text=" Height (cm)  " , font=('calibre') , bg="#E389B9"
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    label,
    text=" Weight (kg)  ", font=('calibre') , bg="#E389B9"

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    label,
)
height_tf.grid(row=3, column=2, pady=25, padx=25)

weight_tf = Entry(
    label,
)
weight_tf.grid(row=4, column=2, pady=25)

frame3 = Frame(
    label
)
frame3.grid(row=5, columnspan=3, pady=25)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='  Reset  ',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='  Exit  ',
    command=lambda:bm.destroy()
)
exit_btn.pack(side=RIGHT)

bm.mainloop()



