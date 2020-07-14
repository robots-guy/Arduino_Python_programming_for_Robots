'''
Upload "e8_4wheel_car_control_bluetoothl.ino" sketch to arduino 
Use Pyhton 3.7 
Install respective packages if its missing or you get module not found error
Please take care of indenting your code
'''
#Import following packages
import serial
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk

'''
Connect to HC-05 Bluetooth via serial port: Password: 1234
Goto --> Device manager to find the serail port number of BLE module
com7 --> Change port accordingly to yours as the bluetooth is connected 
'''
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

#function call to move your car forward     
def upp():
    arduino.write(b'1') 

#function call to move your car backward  
def downn():
    arduino.write(b'2') 

#function call to turn your car left
def left():
    arduino.write(b'7') 

#function call to turn your car right  
def right():
    arduino.write(b'8') 

#function call to stop your car
def stop():
    arduino.write(b'3') 
    
# MAIN
window = tkinter.Tk() #create tkinter window
window.title("4 Wheeled robot control") #give title
window.configure(background="white") #change background color 
window.geometry("1400x1000") #set size of tkinter window

#create frame to stack your control buttons 
f1 = tkinter.Frame(window)
f1.grid(row=2, column=0, sticky="nsew", pady=40)
f1.configure(background="white")


'''
Declare the images 
Change the file path accordingly as per your folder 
var =  ImageTk.PhotoImage(Image.open("<---your file path--->"))
'''
stopped = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/stop.png"))
up = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/up.png"))
down = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/down.png"))
left_turn = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/left_turn.png"))
right_turn = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/right_turn.png"))
car = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/car.png"))
speed_low = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/exercises/speed1.png"))
speed_medium = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/exercises/speed2.png"))
speed_high = ImageTk.PhotoImage(Image.open("C:/Users/User/Documents/scripts/exercises/speed3.png"))


#Create your widgets
low_button = tkinter.Radiobutton(f1, text="Low",
                            indicatoron=False, value="low", width=8,font=('Verdana',14),  command = speed1)

medium_button = tkinter.Radiobutton(f1, text="Medium",
                             indicatoron=False, value="medium", width=8, font=('Verdana',14), command = speed2)

high_button = tkinter.Radiobutton(f1, text="High",
                             indicatoron=False, value="high", width=8, font=('Verdana',14), command = speed3)

l1 = tkinter.Label(window, text="Control your Motor speed & direction using the buttons below", 
                   font=('Verdana',12), bg="white", fg="black")


button_exit = tkinter.Button(window, text="Exit", font = ('Verdana',14), 
              padx=100, command=close_window)


buttonup = tkinter.Button(f1, image = up, bg = "white", command= upp, 
                          relief= tkinter.FLAT )

buttonstop = tkinter.Button(f1, image = stopped, bg = "white", command= stop, 
                            relief= tkinter.FLAT)

buttondown = tkinter.Button(f1, image = down, bg ="white", command= downn, 
                            relief= tkinter.FLAT)

buttonleft = tkinter.Button(f1, image = left_turn, bg ="white", command= left, 
                    relief= tkinter.FLAT)

buttonright = tkinter.Button(f1, image = right_turn, bg ="white", command= right, 
                     relief= tkinter.FLAT)

#fun image for your car
#you can replcae with your car image 
car_image = tkinter.Button(window, image = car, bg ="white", 
                   relief= tkinter.FLAT)

speed_scale = tkinter.Button(window, image = speed_low, bg ="white", padx =100, pady=100, relief= tkinter.FLAT)


#pack all your widgets
low_button.grid(row=2, column=0, pady=5)
medium_button.grid(row=2, column=1, pady=5)
high_button.grid(row=2, column=2, pady=5)
l1.grid(row=1, column=0,  columnspan =3)
button_exit.grid(row=2,column=3)
buttonup.grid(row =3, column =1,pady =30, padx=50)
buttonstop.grid(row =4, column =1, pady =20, padx=50)      
buttondown.grid(row =5, column =1, padx=50, pady =20)
buttonleft.grid(row =4, column =0, padx=50, pady =20)
buttonright.grid(row =4, column =2, padx=50, pady =20)
car_image.grid(row =0, column =3, rowspan = 2)
speed_scale.grid(row =0, column =0)      

#execute the loop
window.mainloop()
