from tkinter import *

root = Tk()
root.title('Double Pendulum')

e = Entry(root, width='35', borderwidth=5, bg='blue', fg='white')
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
#e.insert(0, 'Enter your number: ')

#myLabel1 = Label(root, text='Hello world!').grid(row=0, column=0)
def myClick(number):
    e.delete(0,END)
    e.insert(0,number)
    return
myButton = Button(root, text='Enter your name', command=lambda: myClick('Bartek'), padx=50, pady=25, fg='#ffffff', bg='red')
myButton.grid(row=1,column=0)

root.mainloop()
