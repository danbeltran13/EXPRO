import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter
import pro as list
import matplotlib.dates as dates


window = tkinter.Tk()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = [1,2,3,4,5,6,7,8,9,10]

fig = Figure(figsize=(15,5))
a = fig.add_subplot(111)
dalist = list.returnList('Barbell Back Squat')
exlist = list.returnList('Bench Press')
list.fixLenght(dalist,exlist)

a.scatter(dalist,exlist)

# a.invert_yaxis()

a.set_title("Estimation Grid", fontsize=16)
a.set_ylabel("Y", fontsize=14)
a.set_xlabel("X", fontsize=14)
a.grid()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()
canvas.draw()

tkinter.Button(window, text = 'THIS IS   BUTTON').pack()


window.mainloop()