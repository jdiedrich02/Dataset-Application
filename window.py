import tkinter as tk
import tkinter.ttk as ui
from tkinter import filedialog

class Window:
    graph = ''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def renderWindow(self):
        # Basic Window
        window = tk.Tk()
        window.geometry(self.width + 'x' + self.height)
        window.title('Data Reader')

        # New Window Button
        button = ui.Button(window, text = 'New Window', command = self.renderWindow)
        button.place(x = 10, y = 10)
        button.config(width = 20)

        # Settings Button
        button = ui.Button(window, text = 'Settings', command = self.openSettings)
        button.place(x = 10, y = 50)
        button.config(width = 20)

        # Upload Data Button
        button = ui.Button(window, text = 'Upload Data', command = self.parseData)
        button.place(x = 10, y = 90)
        button.config(width = 20)

        # Dropdown Menu
        dropdown = ui.Combobox(
            state = 'readonly',
            values = [
                'Bar',
                'Pie',
                'Line'
            ]
        )
        dropdown.place(x = 10, y = 130)

        # Start Render Button
        button = ui.Button(window, text = 'Start Render', command = self.startRender)
        button.place(x = 10, y = 170)
        button.config(width = 20)

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
        filename = filedialog.askopenfilename(filetypes = filetypes)
        print(filename)

    def startRender(self):
        print('rendering data')

    def updateWindow(width, height):
        print('updating width and height of window')