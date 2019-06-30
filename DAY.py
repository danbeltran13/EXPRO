

# TODO: ADD FEATURES TO PROGRAM - WORK ON DISPLAYING WEIGHT, TIME, BD
# TODO: FIND MAX OF THE EXCERSISE, VOLUME

# total volume for excersice, volume for a set, max of excercise,



import tkinter
import datetime
import matplotlib
import pro as list
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as dates

MAXED = False

class board:
    # WILL DISPLAY GRAPH BASED ON VALUES GIVEN FROM LISTBOXES
    def drawGraph(self, box_x,box_y):
        # GETS SELECTED VALUES OF THE LISTBOXES
        x = box_x.get(tkinter.ACTIVE)
        y = box_y.get(tkinter.ACTIVE)

        x_values = []
        y_values = []

        #GETS THE X AND Y VALUES
        if x in ('DATE','TIME' , 'WEIGHT' ,'BODY FAT'):
            x_values = list.returnList(x,Volume = False)
        else:
            x_values = list.returnList(x, MAX = MAXED)

        if y in ('DATE',  'TIME', 'WEIGHT', 'BODY FAT'):

            y_values = list.returnList(y,Volume = False)
        else:
            y_values = list.returnList(y, MAX = MAXED)



        # FIXES THE LENGHT OF THE LISTS
        list.fixLenght(x_values,y_values)



        fig = Figure(figsize=(13,9))
        a = fig.add_subplot(111)



        # PRINT BASED ON WHAT IS ASKED

        xd= False
        yd = False

        if x == 'DATES':
            xd = True

            for i in range(0,len(x_values)):
                x_values[i]=dates.datestr2num(x_values[i])



        if y == 'DATES':
            yd = True
            # IF X AND Y ARE BOTH DATES THEY SHARE THE SAME MEMORY ADRESS THEREFORE A CHANGE IS ONLY REQUIRED IN 1
            if x != 'DATES':
                for i in range(0,len(x_values)):

                    y_values[i]=dates.datestr2num(y_values[i])



        for i in range(0,len(x_values)):
            a.plot_date(x_values[i],y_values[i],  xdate=xd, ydate = yd)


        a.set_title(x +' vs. '+y , fontsize=12)
        a.set_ylabel(y ,fontsize=12)
        a.set_xlabel(x, fontsize=12)
        a.grid()

        canvas = FigureCanvasTkAgg(fig, master=self.Frame)

        canvas.get_tk_widget().grid(column=0, row=1, columnspan=4, padx=20, pady=20)
        canvas.draw()





    def __init__(self, Frame, arraylist, int,gwidth, gheight):


        '''ARRAY LIST WILL BE THE LIST OF DAYS DICTIONARY, FRAME WILL BE THE LOCATION OF THE BOARD'''
        self.Frame = Frame

        # WIDGETS
        label = tkinter.Label(Frame, text = str(int) + '  Choose EX (Scrollable)')
        graph_x = tkinter.Listbox(Frame, width =30, height = 1)
        graph_y = tkinter.Listbox(Frame, width=30, height=1)
        enter_button = tkinter.Button(Frame, text="ENTER", command = lambda: self.drawGraph(graph_x,graph_y))



        # INSERTING ITEMS LISTBOXES
        for i in range(0, len(arraylist)):
            graph_x.insert(i, arraylist[i])

        for i in range(0, len(arraylist)):
            graph_y.insert(i, arraylist[i])

        # PLACING WIDGETS ON SCREEN
        label.grid(column=0, row = 0)
        graph_x.grid(column=1, row=0)
        graph_y.grid(column=2, row=0)
        enter_button.grid(column=3, row=0)




graph_number = ['1x1']

exList = ['1','2','3','4','5','6']

def save_graph_number(grid):
    # CLEARS CONTENT
    for widget in window.winfo_children():
       widget.destroy()
    # REDRAWS MENU
    draw_menu()

    graph_number[0] = grid
    graph_array = graph_number[0].split('x')

    for i in range(0,len(graph_array)):
        graph_array[i] = int(graph_array[i])

    # FINDS WIDTH AND HEIGHT OF GRAPHS
    window.update_idletasks()
    graph_width = window.winfo_width()/graph_array[0]-50
    graph_height = window.winfo_height()/graph_array[1] - 50

    for i in range(graph_array[0]):
        for j in range(graph_array[1]):


            frame = tkinter.Frame(window)
            frame.grid(column=i, row=j)
            board(frame,exList, i+1, graph_width,graph_height)



def update_grid_size():
    update_grid_window = tkinter.Toplevel(window)
    update_grid_window.geometry('300x100')
    # WIDGETS
    label = tkinter.Label(update_grid_window, text="Enter Graph Grid (CxR): ")
    enter_box = tkinter.Entry(update_grid_window)
    enter_box.insert(0, graph_number[0])
    enter_button = tkinter.Button(update_grid_window, text= "Enter", command = lambda:save_graph_number((enter_box.get().strip())))

    # PUTS WIDGETS TO SCREEN
    label.grid()
    enter_box.grid(column=0,row = 1)
    enter_button.grid(column=1, row=1)

# MENU BAR NEEDS TO BE REDRAW WHEN DISPLAY IS REDRAWN
def draw_menu():
    menuBar = tkinter.Menu(window)
    gridMenu = tkinter.Menu(menuBar)
    menuBar.add_cascade(label='GRID', menu=gridMenu)
    gridMenu.add_command(label='AMOUNT OF GRAPHS', command=update_grid_size)
    window.config(menu=menuBar)

# WINDOW SETTING
window = tkinter.Tk()
window.title("Program")
window.geometry("800x600")

draw_menu()



# EXAMPLE LIST
exList = list.ExList().copy()


save_graph_number('1x1')


window.mainloop()









