'''
Upload "e3_dc_motor_control.ino" sketch to arduino 
Use Pyhton 3.7 
Install respective packages if its missing or you get module not found error
Please take care of indenting your code
'''
#Import following packages
import serial
import tkinter
from PIL import Image, ImageTk

#Connect to arduino via serial port 
#com6 --> Change port accordingly to yours
arduino = serial.Serial('com6',9600)

#Function call to close your program
def close_window():
    arduino.close()
    window.destroy()

#function call to set speed of motor    
def speed1():  
    speed_scale.config(image = speed_low) #set image to button 
    arduino.write(b'4') #write to arduino

def speed2():  
    speed_scale.config(image = speed_medium) #set image to button 
    arduino.write(b'5') #write to arduino

def speed3():
    speed_scale.config(image = speed_high) #set image to button 
    arduino.write(b'6') #write to arduino
    
#function call to forward button    
def forward():
    arduino.write(b'1') #write to arduino

#function call to reverse button    
def backward():
    arduino.write(b'2') #write to arduino

#function call to stop button  
def stop():
    arduino.write(b'3') #write to arduino
    
# MAIN
window = tkinter.Tk() #create tkinter window
window.title("DC Motor control") #give title
window.configure(background="white") #change background color 
window.geometry("480x600") #set size of tkinter window

#create a frame to arrange the motor control buttons
#Note: Its not necessary to create frames. But it will provide a way to propely arrange your buttons
f1 = tkinter.Frame(window)
f1.grid(row=2, column=0, sticky="nsew", pady=40)
f1.configure(background="white")

'''
Declare the images 
Cgange the file path accordingly as per your folder 
var =  ImageTk.PhotoImage(Image.open("<---your file path--->"))
'''
stopped = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/stop.png"))
left = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/left.png"))
right = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/right.png"))
speed_low = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/exercises/speed1.png"))
speed_medium = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/exercises/speed2.png"))
speed_high = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/exercises/speed3.png"))



#define your widgets 
low_button = tkinter.Radiobutton(f1, text="Low",
                            indicatoron=False, value="low", width=8,font=('Verdana',14),  command = speed1)

medium_button = tkinter.Radiobutton(f1, text="Medium",
                             indicatoron=False, value="medium", width=8, font=('Verdana',14), command = speed2)

high_button = tkinter.Radiobutton(f1, text="High",
                             indicatoron=False, value="high", width=8, font=('Verdana',14), command = speed3)



button_exit = tkinter.Button(window, text="Exit", font=('Verdana',14), 
                             padx=100, pady = 10, 
                             command=close_window)

#create you buttons
buttonback = tkinter.Button(f1, image = left, bg = "white", command= forward, relief= tkinter.FLAT)
buttonquit = tkinter.Button(f1, image = stopped, bg = "white", command= stop, relief= tkinter.FLAT)
buttonnext = tkinter.Button(f1, image = right, bg ="white", command= backward, relief= tkinter.FLAT)
label_text = tkinter.Label(f1, text="Set your Speed and Control your motor", font=('Verdana',12), bg="white", fg="black")
speed_scale = tkinter.Button(window, image = speed_low, bg ="white", padx =100, pady=100, relief= tkinter.FLAT)

#Pack all your widgets
low_button.grid(row=2, column=0)
medium_button.grid(row=2, column=1)
high_button.grid(row=2, column=2)
button_exit.grid(row=6,column=0, columnspan =3)
buttonback.grid(row =3, column =0,pady =10, padx=50)
buttonquit.grid(row =3, column =1, pady =10, padx=50)
buttonnext.grid(row =3, column =2, padx=30, pady =20)
label_text.grid(row=1, column=0,  padx=10, pady =20, columnspan =3)
speed_scale.grid(row =0, column =0)

#execute the loop
window.mainloop()