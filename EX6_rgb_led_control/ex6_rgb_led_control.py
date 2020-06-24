'''
Upload "e6_rgb_led_control.ino" sketch to arduino 
Use Pyhton 3.7 
Install respective packages if its missing or you get module not found error
Please take care of indenting your code
'''
#Import following packages
import serial
import tkinter
from tkcolorpicker import askcolor

#Connect to arduino via serial port 
#com6 --> Change port accordingly to yours
arduino = serial.Serial('com6',9600)

#Exit the window
def close_window():
    arduino.close()
    window.destroy()

#function call for switc    led_on button
def led_on():
    cc = askcolor((255, 0, 0), window) #open color picker and get color 
    r = cc[0][0] #get red value from tuple
    g = cc[0][1] #get green value from tuple
    b = cc[0][2] #get blue value from tuple
    c= cc[1] #get the hex value from tuple 
    color_label.config(bg= str(c))
    label.config(text= "Your color is:" + str(c))
    print(r,g,b) #print value for cross-check
    print(c)   #print value for cross-check 
    arduino.write(str(c).encode()) #write hex value to arduino 
    

# MAIN
window = tkinter.Tk() #create tkinter window
window.title("RGB LED control") #create title
window.configure(background="white") #set background color

#create widgets
button_on = tkinter.Button(window, text="Choose your color", 
                           font=('Verdana',12), padx=60, pady =10, 
                           bg="green",fg="white",
                           command = led_on)

label = tkinter.Label(window, text="Your color is: #FF0000", 
                      font=('Verdana',12),fg="black", bg ='white')

color_label = tkinter.Label(window,padx=135, pady =30, bg="red", fg="black")

button_exit = tkinter.Button(window, text="Exit", font=('Verdana',12), 
                             padx=120, pady =10, 
                             command = close_window)

#pack widgets
button_on.grid(row=2,column=0, columnspan =2, pady=10)
label.grid(row=0,column=0)
color_label.grid(row=1,column=0, columnspan =2)
button_exit.grid(row=4,column=0, columnspan =2)

#execute the loop
window.mainloop()