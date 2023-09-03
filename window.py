import tkinter as tk
import tkinter.ttk as ui
from tkinter import filedialog
import matplotlib as plot
import algorithms as alg

class Window:
    graph = None
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

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.backgroundColor = 'White'
        # Set Font size

    def renderWindow(self):
        # Basic Window
        window = tk.Tk()
        window.geometry(self.width + 'x' + self.height)
        window.title('Data Reader')
        window.resizable(width=0, height=0)

        # Menu Button Frame
        menuFrame = tk.LabelFrame(window, text='Menu Options', padx=10, pady=10, width=170, height=300, labelanchor='n')
        menuFrame.pack(expand="yes", padx=20, pady=20, side='left')
        menuFrame.propagate(False)

        # Download PDF Button
        self.downloadBtn = ui.Button(menuFrame, text='Download Data', command = self.downloadFramePDF)
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
        self.graph = self.dropdown.get()

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
        settings.geometry('400x400')
        settings.title('Settings')
        settings.resizable(width=0, height=0)

        # Settings includes background color change, font color change, and font size
        settingsFrame = tk.LabelFrame(settings, text='Settings', padx=10, pady=10, width=250, height=300, labelanchor='n')
        settingsFrame.pack(expand="yes", padx=20, pady=20, side='left')
        settingsFrame.propagate(False)

        # Background Color
        bgColorLabel = tk.Label(settingsFrame, text='Background Color')
        bgColorLabel.pack()
        bgColor = ui.Combobox(
            settingsFrame,
            state = 'readonly',
            values = [
                'White',
                'Black',
                'Blue',
                'Purple'
            ]
        )
        bgColor.place(x=20, y=20)
        bgColor.pack(pady=5)
        bgColor.bind('<<ComboboxSelected>>', lambda event, arg=bgColor: self.setBackgroundColor(arg))
        bgColor.current(0)

        # Font Color
        fontColorLabel = tk.Label(settingsFrame, text='Font Color')
        fontColorLabel.pack()
        fontColorDropdown = ui.Combobox(
            settingsFrame,
            state = 'readonly',
            values = [
                'White',
                'Black',
                'Red',
                'Purple'
            ]
        )
        fontColorDropdown.pack(pady=5)
        fontColorDropdown.bind('<<ComboboxSelected>>', lambda event, arg=fontColorDropdown: self.setFontColor(arg))
        fontColorDropdown.current(0)

        # Font size
        fontSizeLabel = tk.Label(settingsFrame, text='Font Size')
        fontSizeLabel.pack()
        fontSizeDropdown = ui.Combobox(
            settingsFrame,
            state = 'readonly',
            values = [
                '12px',
                '14px',
                '16px',
                '18px',
                '24px'
            ]
        )
        fontSizeDropdown.pack(pady=5)
        fontSizeDropdown.bind('<<ComboboxSelected>>', lambda event, arg=fontSizeDropdown: self.setFontSize(arg))
        fontSizeDropdown.current(0)

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
        self.updateLogMessage('Rendering a ' + self.graph + ' graph from file: ' + self.filename)
        print('rendering data')

    def updateLogMessage(self, message):
        self.label.config(text=message)

    def setGraph(self, combobox):
        self.graph = combobox.get()
    
    def downloadFramePDF(self):
        print('Downloading PDF of data')

    def clearGraphFrame(self):
        print('Clearing Graph Frame')

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