'''
Upload "e2_servo_control.ino" sketch to arduino 
Use Pyhton 3.7 
Install respective packages if its missing or you get module not found error
Please take care of indenting your code
'''
#Import following packages
import serial
import tkinter
import tk_tools

#Connect to arduino via serial port 
#com6 --> Change port accordingly to yours
arduino = serial.Serial('com6',9600)

#Function call to close your program
def close_window():
    arduino.close()
    window.destroy()

#Function call to move_servo button
def move_servo(var):
    speed_gauge.set_value(var) #set value to the speed gauge 
    print(var) #print value for cross-check
    
    #send servo angle value to arduino
    arduino.write(str(var).encode()) #write this value to arduino 
    
    #get servo angle  ack from arduino to cross-check
    reachedPos = str(arduino.readline()) #get value back from arduino 
    print (reachedPos)
   
# MAIN
window = tkinter.Tk() #create tkinter window
window.title("Servo angle control")  #give title
window.configure(background="white") #change background color 

# Create a slider for servo position
servo = tkinter.Scale(window, activebackground="blue", 
                      label = "        Set the Angle of your servo", 
                      bg = "white", font=('Verdana',16), from_=0, to=180, 
                      orient=tkinter.HORIZONTAL, length= 400, 
                      command = move_servo)

#Create a speed-gauge using tk-tools module
speed_gauge = tk_tools.Gauge(window, max_value=180, bg='white', 
                             label='Servo angle', unit='  deg', 
                             red=90, yellow=10, height = 300, width = 500)

button_exit = tkinter.Button(window, text="Exit", font=('Verdana',16), 
                             padx=100, pady = 10, 
                             command=close_window)

#pack your buttons, sliders
servo.grid(row=1, column=0)
speed_gauge.grid(row=0, column=0)
button_exit.grid(row=2,column=0, columnspan =2)

#execute the loop
window.mainloop()