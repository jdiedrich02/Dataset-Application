import tkinter as tk
import tkinter.ttk as ui
from tkinter import filedialog
import matplotlib as plot

class Window:
    graph = ''
    label = ''
    filename = ''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def renderWindow(self):
        # Basic Window
        window = tk.Tk()
        window.geometry(self.width + 'x' + self.height)
        window.title('Data Reader')

        # Left Button Frame (Swap out to have a menu frame and a graph frame)
        menuFrame = tk.LabelFrame(window, text='Menu Options', padx=10, pady=10, width=170, height=300, labelanchor='n')
        menuFrame.pack(expand="yes", padx=20, pady=20, side='left')
        menuFrame.propagate(False)

        # New Window Button
        button = ui.Button(menuFrame, text='New Window', command = self.renderWindow)
        button.place(x=0, y=0)
        button.config(width = 20)

        # Settings Button
        button = ui.Button(menuFrame, text='Settings', command=self.openSettings)
        button.place(x=0, y=40)
        button.config(width = 20)

        # Upload Data Button
        button = ui.Button(menuFrame, text='Upload Data', command=self.parseData)
        button.place(x=0, y=80)
        button.config(width=20)

        # Dropdown Menu
        dropdown = ui.Combobox(
            menuFrame,
            state = 'readonly',
            values = [
                'Bar',
                'Pie',
                'Line'
            ]
        )
        dropdown.place(x=0, y=120)
        dropdown.current(0)
        self.graph = 'Bar'

        # Start Render Button
        button = ui.Button(menuFrame, text='Start Render', command=self.startRender)
        button.place(x=0, y=160)
        button.config(width=20)

        # Graph Frame
        graphFrame = tk.LabelFrame(window, text='Data Enhancement', padx=10, pady=10, width=1100, height=500, labelanchor='n')
        graphFrame.pack(expand="yes", padx=20, pady=20)
        graphFrame.propagate(False)

        # Add Graph in graphFrame

        # Log Frame
        logFrame = tk.LabelFrame(window, text='Logs', padx=10, pady=10, width=1500, height=100, labelanchor='n')
        logFrame.pack(expand="yes", padx=20, pady=20)
        logFrame.propagate(False)

        # Log Label
        self.label = tk.Label(logFrame, text='Welcome!')
        self.label.pack(expand="yes", padx=20, pady=20)

        # Mainloop call at the end of the rendering
        tk.mainloop()

    def openSettings(self):
        # Settings window
        settings = tk.Tk()
        settings.geometry('500x500')
        settings.title('Settings')

    def parseData(self):
        filetypes = (
            ('text files', '*.txt'),
            ('Excel files', '*.xlsx'),
            ('CSV Files', '*.csv')
        )
        self.filename = filedialog.askopenfilename(filetypes=filetypes)
        self.updateLogMessage('Successfully Uploaded File: ' + self.filename)

    def startRender(self):
        if self.filename == '':
            self.updateLogMessage('ERROR: There is No File Attached')
            return
        
        self.updateLogMessage('Rendering a ' + self.graph + ' graph from file: ' + self.filename)
        print('rendering data')

    def updateWindow(width, height):
        print('updating width and height of window')

    def updateLogMessage(self, message):
        self.label.config(text=message)

    def setGraph(self, graph):
        self.graph = graph