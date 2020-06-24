'''
Upload "e5_temperature_logging.ino" sketch to arduino 
Use Pyhton 3.7 
Install respective packages if its missing or you get module not found error
Please take care of indenting your code
'''
#Import following packages
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter
import numpy as np
import tk_tools
import serial 
import csv
import datetime

#Declare Global variable
data = np.array([])
condition = False

#Connect to arduino via serial port 
#com6 --> Change port accordingly to yours
arduino = serial.Serial('COM6',9600);

#Plot your data
def plot_data():
    global condition, data #declare global variables again 

    if (condition == True):
        
        a = arduino.readline() #read data from arduino
        b= float(a[0:len(a)-2].decode("utf-8"))  #convert to integer
        a.decode() #decode a for later use
        print(b)
        ss.set_value(str(b))  #set the value to seven segment display
        
        #Open a csv file and save data to it 
        with open("test_data.csv","a", newline='') as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%Y, %m, %d, %H, %M, %S'),str(b)])
          
        if(len(data) < 100):
            data = np.append(data,float(a[0:4]))
        else:
            data[0:99] = data[1:100]
            data[99] = float(a[0:4])
		
        lines.set_xdata(np.arange(0,len(data)))
        lines.set_ydata(data)
        canvas.draw()
    
    # in after method 1 miliseconds 
    # is passed i.e after seconds 
    # main window will get plotted with data
    window.after(1,plot_data)

#start the plot
def plot_start():
    global condition
    condition = True
    start_button.config(state = 'disabled')
    stop_button.config(state = 'normal')
    arduino.reset_input_buffer()

#pause the data plot
def plot_stop():
    global condition
    condition = False
    stop_button.config(state = 'disabled')
    start_button.config(state = 'normal')

#exit function
def close_window():
    arduino.close()
    window.destroy()   


#MAIN LOOP
window = tkinter.Tk() #create tkinter window
window.title('Temperature sensor plot') #give title
window.configure(background = 'white') #set background color 
window.geometry("900x720") # set the window size

#-create Plot object on GUI
# add figure canvas
fig = Figure(figsize=(8, 4), dpi=100);
ax = fig.add_subplot(111)

#display only 100 samples
ax.set_title('Temperature sensor data');
ax.set_xlabel('time')
ax.set_ylabel('Temperature in deg C')
ax.grid(True, linestyle='-.')
ax.set_xlim(0,100)
ax.set_ylim(0,100)
lines = ax.plot([],[],color='C1',marker='o', markersize=6)[0]

canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
canvas.get_tk_widget().grid(row=0,column=0, rowspan =2, columnspan =2, padx=30, pady=30)
canvas.draw()

#create buttons, other widgets
start_button = tkinter.Button(window, text = "Start data logging", 
                              font=('Verdana',14),padx=10, pady =10, 
                              bg = 'green', fg= 'white', 
                              command = lambda: plot_start())


stop_button = tkinter.Button(window, text = "Pause data logging", 
                             font=('Verdana',14), padx=10, pady =10, 
                             command = lambda:plot_stop())

button_exit = tkinter.Button(window, text="Exit", font=('Verdana',14), 
                             padx=300, pady =10, 
                             command = close_window)


name_tag = tkinter.Label(window, text= "Ambient temperature data from sensor:                       ", 
                         font=('Verdana',18), bg="White")

ss = tk_tools.SevenSegmentDigits(window, digits=4, background='white',  
                                 digit_color='black', height=60)


#pack your widgets
start_button.grid(row=3,column=0, pady=20)
stop_button.grid(row=3,column=1, pady=20)
button_exit.grid(row=4,column=0, columnspan =2)
name_tag.grid(row=2, column=0, columnspan =2)
ss.grid(row=2, column=1, pady=10)

arduino.reset_input_buffer()

window.after(1,plot_data)

#execute the loop
window.mainloop()





