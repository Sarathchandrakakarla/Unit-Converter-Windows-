#Importing Modules

from tkinter import *
from tkinter import ttk
from pint import UnitRegistry
import math

u=UnitRegistry(autoconvert_offset_to_baseunit = True)
decade=10*u('year')
u.define('quintal = 100*kg = quin')

#Creating a Window
window=Tk()
window.geometry('650x500+500+200')
window.title('Unit Converter')
window.state('zoomed')
#Image variables
bg=PhotoImage(file=r"C:\Users\kakar\Desktop\Icons\gradient1.png")
head=PhotoImage(file=r"C:\Users\kakar\Desktop\Icons\unit_heading1.png")
double_arrow=PhotoImage(file=r"C:\Users\kakar\Desktop\Icons\double-arrows.png")

#Creating Function for Changing units according to quantities
def change(event):
    var=main_var.get()
    if var=='Length':
        unit1['values'],unit2['values']=length,length
        unit1.current(1)
        unit2.current(2)
    elif var=='Weight':
        unit1['values'],unit2['values']=weight,weight
        unit1.current(1)
        unit2.current(2)
    elif var=='Temperature':
        unit1['values'],unit2['values']=temperature,temperature
        unit1.current(0)
        unit2.current(1)
    elif var=='Time':
        unit1['values'],unit2['values']=time,time
        unit1.current(0)
        unit2.current(1)
    elif var=='Area':
        unit1['values'],unit2['values']=area,area
        unit1.current(1)
        unit2.current(2)
    elif var=='Volume':
        unit1['values'],unit2['values']=volume,volume
        unit1.current(1)
        unit2.current(4)
        
#Creating Functions for Buttons

def clear():
    inp.delete(0,'end')
    out_var.set('')
def convert(event):
    global l,out_value
    var1=unit1.get()
    var2=unit2.get()
    inp_value=float(inp.get())
    l=['SqCentimeter','SqMeter','SqFeet','SqYard']
    v=['CubicMillimeter','CubicCentimeter','CubicMeter']
    def area():
        global b,out_value
        if (var1 in l) and (var2 not in l):
            b=inp_value*u(var1[2:].lower()+'**2')
            out_value= b.to(var2.lower())
        elif (var1 in l) and (var2 in l):
            b=inp_value*u(var1[2:].lower()+'**2')
            out_value= b.to(var2[2:].lower()+'**2')
        elif (var1 not in l) and (var2 in l):
            b=inp_value*u(var1.lower())
            out_value= b.to(var2[2:].lower()+'**2')
        
        else:
            b=inp_value*u(var1.lower())
            out_value= b.to(var2.lower())


    def temp():
        global b,out_value
        b = inp_value*u('deg'+var1[0])
        out_value = round(b.to('deg'+var2[0]),3)
    def volume():
        global b,out_value

        if (var1 in v) and (var2 not in v):
            b=inp_value*u(var1[5:].lower()+'**3')
            out_value= round(b.to(var2.lower()),3)
        elif (var1 in v) and (var2 in v):
            b=inp_value*u(var1[5:].lower()+'**3')
            out_value= round(b.to(var2[5:].lower()+'**3'),3)
        elif (var1 not in v) and (var2 in v):
            b=inp_value*u(var1.lower())
            out_value= round(b.to(var2[5:].lower()+'**3'),3)
        
        else:
            b=inp_value*u(var1.lower())
            out_value= round(b.to(var2.lower()),3)

    def speed():
        global b,out_value
        

    if main.get()=='Area':
        area()
    elif main.get()=='Temperature':
        temp()
    elif main.get()=='Volume':
        volume()
    elif var1=='Decade' or var2=='Decade':
        if var1=='Decade':
            y=inp_value*10
            out_value = (y*u('year')).to(var2.lower())
        elif var2=='Decade':
            y=(inp_value*u(var1.lower())).to('year')
            out_value=y/10
    elif var1=='Quintal' or var2=='Quintal':
        if var1=='Quintal':
            b=inp_value*100
            out_value= (b*u('kg')).to(var2.lower())
        elif var2=='Quintal':
            b=(inp_value*u(var1.lower())).to('kg')
            out_value=b/100
    else:
        b=inp_value*u(var1.lower())
        out_value= b.to(var2.lower())
    
    if math.modf(out_value.magnitude)[0]!=(0.0):
        out_var.set(out_value.magnitude)
    else:
        out_var.set(int(out_value.magnitude))
    

#Label for background image
lb1=Label(window,image=bg,width=2000,height=800)
lb1.place(x=0,y=0)

#Label for Heading Image
lb2=Label(window,image=head,width=300,height=50)
lb2.pack(pady=20)

#Creating a Frame for selecting quantity widgets
f1=Frame(window,bg="#21B4A1")
f1.pack()

#Label for Selecting a Quantity
lb3=Label(f1,text='Select a Quantity:')
lb3.grid(row=0,column=1)

#Menu Lists
quantities=('Length','Weight','Temperature','Time','Area','Volume')
length=('Millimeter','Centimeter','Meter','Kilometer','Inch','Feet','Mile','Yard','Micrometer','Nanometer','Picometer','Light_Year')
weight=('Milligrams','Grams','Kilograms','Pounds','Quintal','Tonne')
temperature=('Celsius','Farenheit','Kelvin')
time=('Second','Minute','Hour','Day','Week','Month','Year','Decade','Century')
currency=('Rupee','Dollar','Dinar','Euro')
area=('SqCentimeter','SqMeter','SqFeet','SqYard','Acre','Hectare')
volume=('CubicMillimeter','CubicCentimeter','CubicMeter','MilliLitre','Litre')

#Creating a Combobox for selecting a quantity
main_var = StringVar()
main = ttk.Combobox(f1, width = 27, textvariable = main_var)
  
# Adding combobox drop down list
main['values'] = quantities
main.current(0)
main.grid(row=0,column=5,padx=10)

main.bind('<<ComboboxSelected>>',change)


#Creating a Frame for Selecting Units, Input, Output and Buttons
f2=Frame(window,bg="#0174AD")
f2.pack(pady=30,padx=10)

#Creating a From unit combobox
unit1_var=StringVar()
unit1 = ttk.Combobox(f2,width=15,textvariable=unit1_var)
unit1['values']=length
unit1.current(1)
unit1.grid(row=0,column=1,padx=30,pady=10)

#Creating a label for placing an Double Arrow image 
lb4=Label(f2,image=double_arrow,width=50,height=30,borderwidth=0)
lb4.grid(row=0,column=2,pady=10)

#Creating a To unit combobox
unit2_var=StringVar()
unit2 = ttk.Combobox(f2,width=15,textvariable=unit2_var)
unit2['values']=length
unit2.current(2)
unit2.grid(row=0,column=3,padx=30)

#Creating a Label to give input
lb4=Label(f2,text='Enter the Input:',borderwidth=5,relief='raised')
lb4.grid(row=3,column=1,pady=70)

#Creating an Entry Box for Taking an Input value
inp_var=StringVar()
inp=Entry(f2,textvariable=inp_var,width=50)
inp.grid(row=3,column=2,pady=70)
inp.focus()
window.bind('<Return>',lambda event:convert(event))
#Creating a Label to give Output
lb5=Label(f2,text='Your Output:',borderwidth=7,relief='raised')
lb5.grid(row=4,column=1)

#Creating an Entry Box for Giving Output value
out_var=StringVar()
out=Entry(f2,textvariable=out_var,width=50,state='readonly')
out.grid(row=4,column=2)

#Creating a Button to Convert input from one unit to another unit
btn1=Button(f2,text='Convert',relief='ridge',borderwidth=8,command=lambda:convert(event=None))
btn1.grid(row=5,column=1,pady=25,columnspan=2)

#Creating a Button to Clear the input and output fields
btn2=Button(f2,text='Clear',relief='ridge',borderwidth=8,command=clear)
btn2.grid(row=5,column=2,columnspan=2)


window.mainloop()
