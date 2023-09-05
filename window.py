import tkinter as tk
import tkinter.ttk as ui
from tkinter import filedialog
import matplotlib.pyplot as plot
from  matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import algorithms as alg
import numpy as numpy

class Window:
    app = None
    data = None
    label = None
    filename = None

    # User Interface
    downloadBtn = None
    uploadDataBtn = None
    clearDataBtn = None
    dropdown = None
    renderBtn = None
    settingBtn = None
    backgroundColor = None
    fontColor = None
    fontSize = None
    settingsChangeLabel = None

    # Graph Attributes
    graphFigure = None
    axes = None    # Here we can specify which type we want through axes.bar, axes.line, etc.
    graphCanvas = None
    size = None  # (x, y) tuple

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.backgroundColor = 'White'
        self.fontColor = 'Black'
        self.fontSize = '12px'

    def renderWindow(self):
        # Basic Window
        self.app = tk.Tk()
        self.app.geometry(self.width + 'x' + self.height)
        self.app.title('Data Reader')
        self.app.resizable(width=0, height=0)
        self.app.protocol("WM_DELETE_WINDOW", self.exit)

        # Menu Button Frame
        menuFrame = tk.LabelFrame(self.app, text='Menu Options', padx=10, pady=10, width=170, height=300, labelanchor='n')
        menuFrame.pack(expand="yes", padx=20, pady=20, side='left')
        menuFrame.propagate(False)

        # Download PDF Button
        self.downloadBtn = ui.Button(menuFrame, text='Download Data', command = self.downloadFrame)
        self.downloadBtn.place(x=0, y=0)
        self.downloadBtn.config(width = 20)
        self.downloadBtn['state'] = 'disabled'

        # Settings Button
        self.settingBtn = ui.Button(menuFrame, text='Settings', command=self.openSettings)
        self.settingBtn.place(x=0, y=40)
        self.settingBtn.config(width = 20)

        # Upload Data Button
        self.uploadDataBtn = ui.Button(menuFrame, text='Upload Data', command=self.parseData)
        self.uploadDataBtn.place(x=0, y=80)
        self.uploadDataBtn.config(width=20)

        # Dropdown Menu
        self.dropdown = ui.Combobox(
            menuFrame,
            state = 'readonly',
            values = [
                'Bar',
                'Pie',
                'Line'
            ]
        )
        self.dropdown.place(x=0, y=120)
        self.dropdown.bind('<<ComboboxSelected>>', lambda event, arg=self.dropdown: self.setGraph(arg))
        self.dropdown.current(0)
        self.graphType = self.dropdown.get()

        # Start Render Button
        self.renderBtn = ui.Button(menuFrame, text='Start Render', command=self.startRender)
        self.renderBtn.place(x=0, y=160)
        self.renderBtn.config(width=20)

        # Clear Data Button
        self.clearDataBtn = ui.Button(menuFrame, text='Clear Graph Frame', command=self.clearGraphFrame)
        self.clearDataBtn.place(x=0, y=200)
        self.clearDataBtn.config(width=20)
        self.clearDataBtn['state'] = 'disabled'

        # Graph Frame
        graphFrame = tk.LabelFrame(self.app, text='Data Enhancement', padx=10, pady=10, width=1100, height=500, labelanchor='n')
        graphFrame.pack(expand="yes", padx=20, pady=20)
        graphFrame.propagate(False)

        # Add Empty Graph in graphFrame
        self.graphFigure = plot.figure()

        # Graph Canvas
        self.graphCanvas = FigureCanvasTkAgg(self.graphFigure, graphFrame)
        self.graphCanvas._tkcanvas.pack(fill=tk.BOTH, expand=1)

        # Log Frame
        logFrame = tk.LabelFrame(self.app, text='Logs', padx=10, pady=10, width=1500, height=100, labelanchor='n')
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
        settings.geometry('400x400')
        settings.title('Settings')
        settings.resizable(width=0, height=0)

        # Settings includes background color change, font color change, and font size
        settingsFrame = tk.LabelFrame(settings, text='Settings', padx=10, pady=10, width=250, height=300, labelanchor='n')
        settingsFrame.pack(expand="yes", padx=20, pady=20, side='left')
        settingsFrame.propagate(False)

        # Background Color
        bgColorLabel = tk.Label(settingsFrame, text='Background Color')
        colors = [
            'White',
            'Black',
            'Blue',
            'Purple'
        ]
        bgColorLabel.pack()
        bgColor = ui.Combobox(
            settingsFrame,
            state = 'readonly',
            values = colors
        )
        bgColor.place(x=20, y=20)
        bgColor.pack(pady=5)
        bgColor.bind('<<ComboboxSelected>>', lambda event, arg=bgColor: self.setBackgroundColor(arg))
        bgColor.current(colors.index(self.backgroundColor))

        # Font Color
        fontColorLabel = tk.Label(settingsFrame, text='Font Color')
        fontColors = [
            'Black',
            'White',
            'Red',
            'Purple'
        ]
        fontColorLabel.pack()
        fontColorDropdown = ui.Combobox(
            settingsFrame,
            state = 'readonly',
            values = fontColors
        )
        fontColorDropdown.pack(pady=5)
        fontColorDropdown.bind('<<ComboboxSelected>>', lambda event, arg=fontColorDropdown: self.setFontColor(arg))
        fontColorDropdown.current(fontColors.index(self.fontColor))

        # Font size
        fontSizeLabel = tk.Label(settingsFrame, text='Font Size')
        sizes = [
            '12px',
            '14px',
            '16px',
            '18px',
            '24px'
        ]
        fontSizeLabel.pack()
        fontSizeDropdown = ui.Combobox(
            settingsFrame,
            state = 'readonly',
            values = sizes
        )
        fontSizeDropdown.pack(pady=5)
        fontSizeDropdown.bind('<<ComboboxSelected>>', lambda event, arg=fontSizeDropdown: self.setFontSize(arg))
        fontSizeDropdown.current(sizes.index(self.fontSize))

        # Change settings label
        self.settingsChangeLabel = tk.Label(settingsFrame)
        self.settingsChangeLabel.pack(pady=5)

        # Close Button
        closeBtn = tk.Button(settingsFrame, text='Close', command=lambda: self.closeSettings(settings))
        closeBtn.pack()

    def parseData(self):
        filetypes = (
            ('text files', '*.txt'),
            ('Excel files', '*.xlsx'),
            ('CSV Files', '*.csv')
        )
        self.filename = filedialog.askopenfilename(filetypes=filetypes)
        self.updateLogMessage('Successfully Uploaded File: ' + self.filename)

        # Parse the data with an algorithm (depending on the file type)
        if (self.filename.find('.txt')):
            self.data = alg.parseTxt(self.filename)
        elif (self.filename.find('.csv')):
            self.data = alg.parseCSV(self.filename)
        elif (self.filename.find('.xlsx')):
            self.data = alg.parseExcel(self.filename)

    def startRender(self):
        if self.filename == None:
            self.updateLogMessage('ERROR: There is No File Attached')
            return

        self.disableAll()
        self.updateLogMessage('Rendering a ' + self.graphType + ' graph from file: ' + self.filename)
        self.renderGraph()

    def updateLogMessage(self, message):
        self.label.config(text=message)

    def setGraph(self, combobox):
        self.graphType = combobox.get()
    
    def downloadFrame(self):
        self.graphFigure.savefig('graph.png')
        self.updateLogMessage('Downloaded Graph as PNG')

    def clearGraphFrame(self):
        self.graphFigure.clear()
        self.graphCanvas.draw()
        self.downloadBtn['state'] = 'disabled'
        self.clearDataBtn['state'] = 'disabled'

    def disableAll(self):
        # Disable all the buttons
        self.clearDataBtn['state'] = 'disabled'
        self.downloadBtn['state'] = 'disabled'
        self.renderBtn['state'] = 'disabled'
        self.dropdown['state'] = 'disabled'
        self.settingBtn['state'] = 'disabled'
        self.uploadDataBtn['state'] = 'disabled'

    def enableAll(self):
        # Enable all the buttons
        self.clearDataBtn['state'] = 'enabled'
        self.downloadBtn['state'] = 'enabled'
        self.renderBtn['state'] = 'enabled'
        self.dropdown['state'] = 'enabled'
        self.settingBtn['state'] = 'enabled'
        self.uploadDataBtn['state'] = 'enabled'

    def setBackgroundColor(self, combobox):
        self.backgroundColor = combobox.get()
        self.settingsChangeLabel.config(text='Background Color Updated Successfully')

    def setFontColor(self, combobox):
        self.fontColor = combobox.get()
        self.settingsChangeLabel.config(text='Font Color Updated Successfully')

    def setFontSize(self, combobox):
        self.fontSize = combobox.get()
        self.settingsChangeLabel.config(text='Font Size Updated Successfully')

    def closeSettings(self, settings):
        settings.destroy()

    # Add parameters for data, size, etc.
    def renderGraph(self):
        self.axes = self.graphFigure.add_subplot()

        # Mock test
        data = (20, 35, 30, 35, 27)
        ind = numpy.arange(5)
        
        if self.graphType == 'Bar':
            self.axes.bar(ind, data)
        elif self.graphType == 'Line':
            self.axes.plot(data)

        self.graphCanvas.draw()
        self.enableAll()

    def exit(self):
        self.app.quit()
        self.app.destroy()