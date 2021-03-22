# The full code for my Computer Science 2020 Coursework.

# from database_module import CPU_DATA, CPU, CPU_NAMES, GPU_DATA, GPU, GPU_NAMES, GAME_DATA, GAME, GAME_NAMES
from PyQt5 import QtCore, QtGui, QtWidgets  # Importing the necessary PyQt5 modules.
from PyQt5.QtWidgets import QMessageBox
import sys  # Importing the sys module.
import json  # Required for the database.

# Loading the json file used to store the data used by the system.
with open('database2.json') as d:
    data = json.load(d)
    d.close()


class Ui_MainWindow(object):  # Class definition for the main window.
    # The main setupUi function, this creates all of the UI elements in the program.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # Giving the main window a name.
        MainWindow.resize(960, 540)  # Defining the size of the window.
        # These two lines of code make it so the window cannot be resized,
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        # as the max and min are already the current size of the window.
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);\n"  # The stylesheet of the main window, giving it a dark background.
                                 "font: 57 10pt \"Dubai\";\n"
                                 "\n"
                                 "line {\n"
                                 "background-color: white;\n"
                                 "}")

        # Creating stacked widget and the default stylesheet. This widget allows for multiple pages in my program.

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 941, 501))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet("QPushButton { \n"
                                         "border: 2px solid;\n"
                                         "border-color: rgb(97, 223, 255);\n"
                                         "border-radius: 20px;\n"
                                         "color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover { \n"
                                         "background: rgb(95, 95, 95);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QLineEdit {\n"
                                         "background: transparent;\n"
                                         "border: 2px solid;\n"
                                         "border-color: rgb(97, 223, 255);\n"
                                         "border-radius: 20px;\n"
                                         "color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel {\n"
                                         "color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox { \n"
                                         "color: white;\n"
                                         "border: 2px solid;\n"
                                         "border-color: rgb(97, 223, 255);\n"
                                         "border-radius: 5px;\n"
                                         "}\n"
                                         "QComboBox::drop-down { background-image: url(arrow.png); }\n"
                                         "\n"
                                         "QListView { color: white; }\n"
                                         "\n"
                                         "QTabWidget::pane { \n"
                                         "border-top: 1px solid white;\n"
                                         "}\n"
                                         "\n"
                                         "QTabBar::tab {\n"
                                         "background-color: rgb(77, 77, 77);\n"
                                         "color: white;\n"
                                         "padding: 7px;\n"
                                         "}\n"
                                         "\n"
                                         "QTabBar::tab:selected { \n"
                                         "background: rgb(93, 93, 93);\n"
                                         "}\n"
                                         "\n"
                                         "QTabBar::tab:hover {\n"
                                         "background: rgb(111, 111, 111);\n"
                                         "}\n"
                                         "\n"
                                         "QCheckBox {\n"
                                         "color: white;\n"
                                         "}")

        # Creating the main menu.

        self.MainMenuPage = QtWidgets.QWidget()
        self.MainMenuPage.setObjectName("MainMenuPage")
        self.MainMenuFrame = QtWidgets.QFrame(self.MainMenuPage)
        self.MainMenuFrame.setGeometry(QtCore.QRect(280, 60, 380, 370))

        # Defining and placing the Main Menu buttons as well as the Main Menu frame.

        self.MainMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainMenuFrame.setObjectName("MainMenuFrame")
        self.AdminButton = QtWidgets.QPushButton(self.MainMenuFrame)
        self.AdminButton.setGeometry(QtCore.QRect(100, 40, 180, 60))
        self.AdminButton.setObjectName("AdminButton")
        self.UserButton = QtWidgets.QPushButton(self.MainMenuFrame)
        self.UserButton.setGeometry(QtCore.QRect(100, 150, 180, 60))
        self.UserButton.setObjectName("UserButton")
        self.ExitButton = QtWidgets.QPushButton(self.MainMenuFrame)
        self.ExitButton.setGeometry(QtCore.QRect(100, 260, 180, 60))
        self.ExitButton.setObjectName("ExitButton")
        self.stackedWidget.addWidget(self.MainMenuPage)

        # Adding functionality to the buttons.

        self.UserButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Tools))
        self.AdminButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
        self.ExitButton.clicked.connect(lambda: sys.exit(0))

        # Login screen.

        self.LoginScreen = QtWidgets.QWidget()
        self.LoginScreen.setObjectName("LoginScreen")
        self.LoginFrame = QtWidgets.QFrame(self.LoginScreen)
        self.LoginFrame.setGeometry(QtCore.QRect(250, 40, 421, 421))

        # Creating the buttons and entry widgets for the login screen.

        self.LoginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginFrame.setObjectName("LoginFrame")
        self.Username = QtWidgets.QLineEdit(self.LoginFrame)
        self.Username.setGeometry(QtCore.QRect(50, 71, 311, 51))
        self.Username.setText("")
        self.Username.setObjectName("Username")

        self.Password = QtWidgets.QLineEdit(self.LoginFrame)
        self.Password.setGeometry(QtCore.QRect(50, 160, 311, 51))
        self.Password.setInputMask("")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")

        self.BackButton1 = QtWidgets.QPushButton(self.LoginFrame)
        self.BackButton1.setGeometry(QtCore.QRect(50, 280, 121, 41))
        self.BackButton1.setObjectName("BackButton1")

        self.LoginSubmitButton = QtWidgets.QPushButton(self.LoginFrame)
        self.LoginSubmitButton.setGeometry(QtCore.QRect(240, 280, 121, 41))
        self.LoginSubmitButton.setObjectName("LoginSubmitButton")
        self.stackedWidget.addWidget(self.LoginScreen)

        # Username and password lists.

        ADMIN_US = ['Admin1', 'Admin2', 'Admin3']
        ADMIN_PW = ['Adminpw1', 'Adminpw2']
        USER_US = ['User1', 'User2', 'User3']
        USER_PW = ['Userpw1', 'Userpw2']

        # Pop up function, this is used throughout the system as parameters can be passed in to create the desired output.

        def popup(title, text):  # Definition of the error prompt.
            msg = QMessageBox()  # Creating the messagebox object.
            msg.setIcon(QMessageBox.Warning)  # Giving it an icon.
            msg.setText(text)  # Giving it some text.
            msg.setStandardButtons(QMessageBox.Ok)  # Giving it an "Ok" button.
            msg.setWindowTitle(title)  # Giving it a title.

            x = msg.exec_()  # A variable needed to open the prompt.

        def message(title, text):  # Definition of the message prompt.
            msg = QMessageBox()  # Creating the messagebox object.
            msg.setIcon(QMessageBox.Information)  # Giving it an icon.
            msg.setText(text)  # Giving it some text.
            msg.setStandardButtons(QMessageBox.Ok)  # Giving it an "Ok" button.
            msg.setWindowTitle(title)  # Giving it a title.

            x = msg.exec_()  # A variable needed to open the prompt.

        def loginValidation():  # Login validation function.
            # This line works as a range check, and a presence check, as the input cannot be 0 characters long.
            if 0 < len(self.Username.text()) <= 12:
                # Checks if the inputs are for an admin.
                if self.Username.text() in ADMIN_US and self.Password.text() in ADMIN_PW:
                    self.stackedWidget.setCurrentWidget(self.Admin)  # Switches to the admin screen.
                    self.Username.clear()  # Clears the username field.
                    self.Password.clear()  # Clears the passworld field.
                    print("Taken to admin screen.")  # For debug use only.
                # Checks if the inputs are for a developer.
                elif self.Username.text() in USER_US and self.Password.text() in USER_PW:
                    # Switches to the developer screen.
                    self.stackedWidget.setCurrentWidget(self.Developer)
                    self.Username.clear()  # Clears the username field.
                    self.Password.clear()  # Clears the password field.
                    print("Taken to developer screen.")  # For debug use only.
            else:
                popup("Invalid Input", "The input is out of range.")  # Calling the popup function.

        # Adding functionality to the buttons.

        # Brings the user back to the main menu screen.
        self.BackButton1.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))
        # Calls the login validation function.
        self.LoginSubmitButton.clicked.connect(lambda: loginValidation())

        # Tools screen.

        self.Tools = QtWidgets.QWidget()

        # Tools buttons, entry fields and tabs.

        self.Tools.setObjectName("Tools")
        self.ToolsTabWidget = QtWidgets.QTabWidget(self.Tools)
        self.ToolsTabWidget.setGeometry(QtCore.QRect(0, 0, 941, 491))
        # Adding a tabbed menu to the tools screen.
        self.ToolsTabWidget.setObjectName("ToolsTabWidget")

        # Creating the tab used to compare games against the specifications of computers.
        self.GameTab = QtWidgets.QWidget()
        self.GameTab.setObjectName("GameTab")

        # Adding all of the buttons, comboboxes and entry fields to the game tab.

        self.BackButton2 = QtWidgets.QPushButton(self.GameTab)
        self.BackButton2.setGeometry(QtCore.QRect(10, 390, 121, 41))
        self.BackButton2.setObjectName("BackButton2")

        self.Line1 = QtWidgets.QFrame(self.GameTab)
        self.Line1.setGeometry(QtCore.QRect(0, 370, 941, 20))
        self.Line1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line1.setObjectName("Line1")
        self.Line1.setStyleSheet("color: white;")

        self.GameLabel1 = QtWidgets.QLabel(self.GameTab)
        self.GameLabel1.setGeometry(QtCore.QRect(280, 30, 121, 41))
        self.GameLabel1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GameLabel1.setObjectName("GameLabel1")
        self.GameCombo1 = QtWidgets.QComboBox(self.GameTab)
        self.GameCombo1.setGeometry(QtCore.QRect(420, 30, 161, 41))
        self.GameCombo1.setAutoFillBackground(False)
        self.GameCombo1.setCurrentText("")
        self.GameCombo1.setObjectName("GameCombo1")

        self.CPULabel1 = QtWidgets.QLabel(self.GameTab)
        self.CPULabel1.setGeometry(QtCore.QRect(290, 100, 121, 41))
        self.CPULabel1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CPULabel1.setObjectName("CPULabel1")
        self.CPUCombo1 = QtWidgets.QComboBox(self.GameTab)
        self.CPUCombo1.setGeometry(QtCore.QRect(420, 100, 161, 41))
        self.CPUCombo1.setObjectName("CPUCombo1")

        self.GPULabel1 = QtWidgets.QLabel(self.GameTab)
        self.GPULabel1.setGeometry(QtCore.QRect(290, 170, 121, 41))
        self.GPULabel1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GPULabel1.setObjectName("GPULabel1")
        self.GPUCombo1 = QtWidgets.QComboBox(self.GameTab)
        self.GPUCombo1.setGeometry(QtCore.QRect(420, 170, 161, 41))
        self.GPUCombo1.setObjectName("GPUCombo1")

        self.RamEnter1 = QtWidgets.QLineEdit(self.GameTab)
        self.RamEnter1.setGeometry(QtCore.QRect(420, 240, 161, 41))
        self.RamEnter1.setObjectName("RamEnter1")

        self.StorageEnter1 = QtWidgets.QLineEdit(self.GameTab)
        self.StorageEnter1.setGeometry(QtCore.QRect(420, 310, 161, 41))
        self.StorageEnter1.setObjectName("StorageEnter1")

        self.GameSubmit = QtWidgets.QPushButton(self.GameTab)
        self.GameSubmit.setGeometry(QtCore.QRect(800, 390, 121, 41))
        self.GameSubmit.setObjectName("GameSubmit")

        self.ToolsTabWidget.addTab(self.GameTab, "")

        # Creating the tab used for CPU to CPU comparison.

        self.CPUTab = QtWidgets.QWidget()
        self.CPUTab.setAutoFillBackground(False)
        self.CPUTab.setObjectName("CPUTab")

        # Adding all of the buttons, comboboxes and entry fields to the CPU comparison screen.

        self.BackButton3 = QtWidgets.QPushButton(self.CPUTab)
        self.BackButton3.setGeometry(QtCore.QRect(10, 390, 121, 41))
        self.BackButton3.setObjectName("BackButton3")

        self.CPUSubmit = QtWidgets.QPushButton(self.CPUTab)
        self.CPUSubmit.setGeometry(QtCore.QRect(800, 390, 121, 41))
        self.CPUSubmit.setObjectName("CPUSubmit")

        self.Line2 = QtWidgets.QFrame(self.CPUTab)
        self.Line2.setGeometry(QtCore.QRect(-20, 370, 971, 20))
        self.Line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line2.setObjectName("Line2")
        self.Line2.setStyleSheet("color: white;")

        self.CPULabel2 = QtWidgets.QLabel(self.CPUTab)
        self.CPULabel2.setGeometry(QtCore.QRect(250, 40, 131, 41))
        self.CPULabel2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CPULabel2.setObjectName("CPULabel2")

        self.CPUCombo2 = QtWidgets.QComboBox(self.CPUTab)
        self.CPUCombo2.setGeometry(QtCore.QRect(410, 40, 161, 41))
        self.CPUCombo2.setObjectName("CPUCombo2")

        self.CPULabel3 = QtWidgets.QLabel(self.CPUTab)
        self.CPULabel3.setGeometry(QtCore.QRect(250, 190, 131, 41))
        self.CPULabel3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CPULabel3.setObjectName("CPULabel3")

        self.CPUCombo3 = QtWidgets.QComboBox(self.CPUTab)
        self.CPUCombo3.setGeometry(QtCore.QRect(410, 190, 161, 41))
        self.CPUCombo3.setObjectName("CPUCombo3")

        self.ToolsTabWidget.addTab(self.CPUTab, "")

        # Creating the tab used for GPU to GPU comparison.

        self.GPUTab = QtWidgets.QWidget()
        self.GPUTab.setObjectName("GPUTab")

        # Adding all of the buttons, comboboxes and entry fields to the GPU comparison screen.

        self.GPUSubmit = QtWidgets.QPushButton(self.GPUTab)
        self.GPUSubmit.setGeometry(QtCore.QRect(800, 390, 121, 41))
        self.GPUSubmit.setObjectName("GPUSubmit")

        self.BackButton4 = QtWidgets.QPushButton(self.GPUTab)
        self.BackButton4.setGeometry(QtCore.QRect(10, 390, 121, 41))
        self.BackButton4.setObjectName("BackButton4")

        self.Line3 = QtWidgets.QFrame(self.GPUTab)
        self.Line3.setGeometry(QtCore.QRect(-20, 370, 971, 20))
        self.Line3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line3.setObjectName("Line3")
        self.Line3.setStyleSheet("color: white;")

        self.GPULabel2 = QtWidgets.QLabel(self.GPUTab)
        self.GPULabel2.setGeometry(QtCore.QRect(250, 40, 131, 41))
        self.GPULabel2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GPULabel2.setObjectName("GPULabel2")

        self.GPUCombo2 = QtWidgets.QComboBox(self.GPUTab)
        self.GPUCombo2.setGeometry(QtCore.QRect(410, 40, 161, 41))
        self.GPUCombo2.setObjectName("GPUCombo2")

        self.GPUCombo3 = QtWidgets.QComboBox(self.GPUTab)
        self.GPUCombo3.setGeometry(QtCore.QRect(410, 190, 161, 41))
        self.GPUCombo3.setObjectName("GPUCombo3")

        self.GPULabel3 = QtWidgets.QLabel(self.GPUTab)
        self.GPULabel3.setGeometry(QtCore.QRect(250, 190, 131, 41))
        self.GPULabel3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GPULabel3.setObjectName("GPULabel3")

        self.ToolsTabWidget.addTab(self.GPUTab, "")
        self.stackedWidget.addWidget(self.Tools)

        # Adding selection options to the comboboxes by making use of the addItem(s) method(s).

        self.CPUCombo1.addItem('')
        self.CPUCombo1.addItems(list(data['cpus'].keys()))
        self.CPUCombo2.addItem('')
        self.CPUCombo2.addItems(list(data['cpus'].keys()))
        self.CPUCombo3.addItem('')
        self.CPUCombo3.addItems(list(data['cpus'].keys()))

        self.GPUCombo1.addItem('')
        self.GPUCombo1.addItems(list(data['gpus'].keys()))
        self.GPUCombo2.addItem('')
        self.GPUCombo2.addItems(list(data['gpus'].keys()))
        self.GPUCombo3.addItem('')
        self.GPUCombo3.addItems(list(data['gpus'].keys()))

        self.GameCombo1.addItem('')
        self.GameCombo1.addItems(list(data['games'].keys()))

        def GameCompare():  # Function for comparing games to computer specifications.
            try:  # Try and except are employed here so if an error occurs a popup is diplayed.
                game_input1 = str(self.GameCombo1.currentText())
                if game_input1 in list(data['games'].keys()):
                    # Fetches the array containing the game's requirements: CPU_Min, GPU_Min, RAM_Min, CPU_Rec, GPU_Rec, RAM_Rec, Storage
                    game_1 = data['games'].get(game_input1)

                cpu_input1 = str(self.CPUCombo1.currentText())
                if cpu_input1 in list(data['cpus'].keys()):
                    # Fetches the information related to the selected CPU.
                    cpu_1 = data['cpus'].get(cpu_input1)

                gpu_input1 = str(self.GPUCombo1.currentText())
                if gpu_input1 in list(data['gpus'].keys()):
                    # Fetches the information related to the selected GPU.
                    gpu_1 = data['gpus'].get(gpu_input1)

                ram_input1 = self.RamEnter1.text()  # Fetches the entered amount of ram.

                # Fetches the entered amount of storage capacity.
                sto_input1 = self.StorageEnter1.text()

                # Setting the contents of the labels to display the desired outputs.
                self.YourCPULabel.setText("Your CPU: " + cpu_input1)
                self.YourGPULabel.setText("Your GPU: " + gpu_input1)
                # For these two string typecasting is used to avoid errors when ints are concatenated to strings.
                self.YourRAMLabel.setText("Your RAM: " + str(ram_input1) + "GB")
                self.YourStorageLabel.setText(
                    "Your available storage capacity: " + str(sto_input1) + "GB")

                # Selection chain to change the text and colour of the text to the correct state,
                # depending on what requirements have or haven't been met.

                # All of these values are stored in arrays, so thus references to the appropriate index are used.
                if game_1[0] <= cpu_1[0]:
                    self.ResultsMinCPU.setText("The CPU meets the minimum requirements.")
                    self.ResultsMinCPU.setStyleSheet("color: #7be898;")
                else:
                    self.ResultsMinCPU.setText("The CPU doesn't meet the minimum requirements.")
                    self.ResultsMinCPU.setStyleSheet("color: #f55d42;")

                if game_1[1] <= gpu_1[0]:
                    self.ResultsMinGPU.setText("The GPU meets the minimum requirements.")
                    self.ResultsMinGPU.setStyleSheet("color: #7be898;")
                else:
                    self.ResultsMinGPU.setText("The GPU doesn't meet the minimum requirements.")
                    self.ResultsMinGPU.setStyleSheet("color: #f55d42;")

                if game_1[2] <= int(ram_input1):
                    self.ResultsMinRAM.setText("The amount of RAM meets the minimum requirements.")
                    self.ResultsMinRAM.setStyleSheet("color: #7be898;")
                else:
                    self.ResultsMinRAM.setText(
                        "The amount of RAM doesn't meet the minimum requirements.")
                    self.ResultsMinRAM.setStyleSheet("color: #f55d42;")

                if game_1[3] <= cpu_1[0]:
                    self.ResultsRecCPU.setText("The CPU meets the recommended requirements.")
                    self.ResultsRecCPU.setStyleSheet("color: #7be898;")
                else:
                    self.ResultsRecCPU.setText("The CPU doesn't meet the recommended requirements.")
                    self.ResultsRecCPU.setStyleSheet("color: #f5b042;")

                if game_1[4] <= gpu_1[0]:
                    self.ResultsRecGPU.setText("The GPU meets the recommended requirements.")
                    self.ResultsRecGPU.setStyleSheet("color: #7be898;")
                else:
                    self.ResultsRecGPU.setText("The GPU doesn't meet the recommended requirements.")
                    self.ResultsRecGPU.setStyleSheet("color: #f5b042;")

                if game_1[5] <= int(ram_input1):
                    self.ResultsRecRAM.setText(
                        "The amount of RAM meets the recommended requirements.")
                    self.ResultsRecRAM.setStyleSheet("color: #7be898;")
                else:
                    self.ResultsRecRAM.setText(
                        "The amount of RAM doesn't meet the recommended requirements.")
                    self.ResultsRecRAM.setStyleSheet("color: #f5b042;")

                if game_1[6] <= int(sto_input1):
                    self.ResultsStorage.setText("The amount of storage capacity is sufficient.")
                    self.ResultsStorage.setStyleSheet("color: #7be898;")
                else:
                    self.ResultsStorage.setText("The amount of storage capacity is insufficient.")
                    self.ResultsStorage.setStyleSheet("color: ff55d42;")
                self.stackedWidget.setCurrentWidget(self.GameResultsScreen)

            except:
                # Popup called to warn the user that they've not filled all fields.
                popup("Fields Blank", "You have left fields blank.")

        def CPUCompare():
            try:  # Try and except are employed here so if an error occurs a popup is diplayed.
                # Grabbing the value used for the first CPU input.
                cpu_input2 = str(self.CPUCombo2.currentText())
                # Validating the presence of the value, and checking it is in the database.
                if cpu_input2 in list(data['cpus'].keys()) and len(cpu_input2) != 0:
                    # Fetching the array associated to the CPU containing its performance and price.
                    cpu_2 = data['cpus'].get(cpu_input2)
                else:
                    # Popup called to warn the user that they've not filled all fields.
                    popup("Field Blank", "There is no input for CPU #1")

                # Selection chain to set the image to one associated with the input.
                # Within the array associated to each CPU is a 2 character brand ID, and it is used here to place the correct image.

                if cpu_2[2] == 'r5':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/r5.png"))
                elif cpu_2[2] == 'i7':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/i7.png"))
                elif cpu_2[2] == 'r3':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/r3.png"))
                elif cpu_2[2] == 'r7':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/r7.png"))
                elif cpu_2[2] == 'r9':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/r9.png"))
                elif cpu_2[2] == 'i3':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/i3.png"))
                elif cpu_2[2] == 'i5':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/i5.png"))
                elif cpu_2[2] == 'i9':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/i9.png"))

                # Grabbing the value used for the first CPU input.
                cpu_input3 = str(self.CPUCombo3.currentText())
                # Validating the presence of the value, and checking it is in the database.
                if cpu_input3 in list(data['cpus'].keys()) and len(cpu_input3) != 0:
                    # Fetching the array associated to the CPU containing its performance and price.
                    cpu_3 = data['cpus'].get(cpu_input3)
                    # Switching to the screen holding the appropriate results.
                    self.stackedWidget.setCurrentWidget(self.CPUResultsScreen)

                    # Modifying the text of the appropriate labels.

                    self.cpunum1label.setText(cpu_input2)
                    self.cpuperf1.setText("This CPU has a performance score of: " + str(cpu_2[0]))
                    self.cpuprice1.setText("This CPU has a price of: £" + str(cpu_2[1]))

                    self.cpunum2label.setText(cpu_input3)
                    self.cpuperf2.setText("This CPU has a performance score of: " + str(cpu_3[0]))
                    self.cpuprice2.setText("This CPU has a price of: £" + str(cpu_3[1]))

                else:
                    # Popup called to warn the user that they've not filled all fields.
                    popup("Field Blank", "There is no input for CPU #2")

                # Selection chain to set the image to one associated with the input.

                if cpu_3[2] == 'r5':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/r5.png"))
                elif cpu_3[2] == 'i7':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/i7.png"))
                elif cpu_3[2] == 'r3':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/r3.png"))
                elif cpu_2[2] == 'r7':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/r7.png"))
                elif cpu_3[2] == 'r9':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/r9.png"))
                elif cpu_3[2] == 'i3':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/i3.png"))
                elif cpu_3[2] == 'i5':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/i5.png"))
                elif cpu_3[2] == 'i9':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/i9.png"))

            except:
                pass

        def GPUCompare():  # The GPU comparison function. Note for this function, all functionality is identical, just replace CPU with GPU.
            gpu_input2 = str(self.GPUCombo2.currentText())
            if gpu_input2 in list(data['gpus'].keys()) and len(gpu_input2) != 0:
                gpu_2 = data['gpus'].get(gpu_input2)
            else:
                popup("Field Blank", "There is no input for GPU #1")

            if gpu_2[2] == 'gx':
                self.gpuim1.setPixmap(QtGui.QPixmap("images/gt.png"))
            elif gpu_2[2] == 'rx':
                self.gpuim1.setPixmap(QtGui.QPixmap("images/rx.png"))
            elif gpu_2[2] == 'rt':
                self.gpuim1.setPixmap(QtGui.QPixmap("images/rt.png"))

            gpu_input3 = str(self.GPUCombo3.currentText())
            if gpu_input3 in list(data['gpus'].keys()) and len(gpu_input3) != 0:
                gpu_3 = data['gpus'].get(gpu_input3)
                self.stackedWidget.setCurrentWidget(self.GPUResultsScreen)

                self.gpunum1label.setText(gpu_input2)
                self.gpuperf1.setText("This GPU has a performance of: " + str(gpu_2[0]))
                self.gpuprice1.setText("This GPU has a price of: £" + str(gpu_2[1]))

                self.gpunum2label.setText(gpu_input3)
                self.gpuperf2.setText("This GPU has a performance score of: " + str(gpu_3[0]))
                self.gpuprice2.setText("This GPU has a price of: £" + str(gpu_3[1]))

            else:
                popup("Field Blank", "There is no input for GPU #2")

            if gpu_3[2] == 'gx':
                self.gpuim2.setPixmap(QtGui.QPixmap("images/gt.png"))
            elif gpu_3[2] == 'rx':
                self.gpuim2.setPixmap(QtGui.QPixmap("images/rx.png"))
            elif gpu_3[2] == 'rt':
                self.gpuim2.setPixmap(QtGui.QPixmap("images/rt.png"))

        # Making the buttons bring you to the appropriate place, and/or calling the appropriate function.

        self.CPUSubmit.clicked.connect(lambda: CPUCompare())
        self.GPUSubmit.clicked.connect(lambda: GPUCompare())
        self.GameSubmit.clicked.connect(lambda: GameCompare())
        self.BackButton2.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))
        self.BackButton3.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))
        self.BackButton4.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))

        # Results Screen for CPUs.
        # NOTE: For all Qt objects, they will require 3 lines each. The first for creating the object, the second for placing it (if need be)
        # and the third for giving it an object name. Although, in some instances other lines may be necessary for proper functionality and appearance.

        self.CPUResultsScreen = QtWidgets.QWidget()
        self.CPUResultsScreen.setObjectName("CPUResultsScreen")
        self.stackedWidget.addWidget(self.CPUResultsScreen)

        self.Line7 = QtWidgets.QFrame(self.CPUResultsScreen)
        self.Line7.setGeometry(QtCore.QRect(-10, 414, 961, 20))
        self.Line7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line7.setObjectName("Line7")
        self.Line7.setStyleSheet("color: white;")

        self.BackButton8 = QtWidgets.QPushButton(self.CPUResultsScreen)
        self.BackButton8.setGeometry(QtCore.QRect(10, 435, 121, 41))
        self.BackButton8.setObjectName("BackButton8")

        self.cpuim1 = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpuim1.setGeometry(QtCore.QRect(50, 50, 200, 200))
        self.cpuim1.setObjectName("cpuim1")
        self.cpuim1.setText("")
        self.cpuim1.setPixmap(QtGui.QPixmap("images/r5.png"))

        self.cpuim2 = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpuim2.setGeometry(QtCore.QRect(650, 50, 200, 200))
        self.cpuim2.setObjectName("cpuim2")
        self.cpuim2.setText("")
        self.cpuim2.setPixmap(QtGui.QPixmap("images/i7.png"))

        self.cpuperf1 = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpuperf1.setGeometry(QtCore.QRect(50, 260, 300, 40))
        self.cpuperf1.setObjectName("cpuperf1")
        self.cpuperf1.setText("Placeholder.")

        self.cpuperf2 = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpuperf2.setGeometry(QtCore.QRect(550, 260, 300, 40))
        self.cpuperf2.setObjectName("cpuperf2")
        self.cpuperf2.setText("Placeholder.")

        self.cpuprice1 = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpuprice1.setGeometry(QtCore.QRect(50, 310, 300, 40))
        self.cpuprice1.setObjectName("cpuprice1")
        self.cpuprice1.setText("Placeholder.")

        self.cpuprice2 = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpuprice2.setGeometry(QtCore.QRect(550, 310, 300, 40))
        self.cpuprice2.setObjectName("cpuprice2")
        self.cpuprice2.setText("Placeholder.")

        self.cpunum1label = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpunum1label.setGeometry(QtCore.QRect(50, 5, 200, 40))
        self.cpunum1label.setObjectName("cpunum1label")
        self.cpunum1label.setText("CPU #1 Name")
        self.cpunum1label.setStyleSheet("font-weight: bold;")

        self.cpunum2label = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpunum2label.setGeometry(QtCore.QRect(650, 5, 200, 40))
        self.cpunum2label.setObjectName("cpunum2label")
        self.cpunum2label.setText("CPU #2 Name")
        self.cpunum2label.setStyleSheet("font-weight: bold;")

        # This button brings you back to the main tools screen.
        self.BackButton8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Tools))

        # Results Screen for GPUs.
        # The same logic applies here for the CPU results screen.

        self.GPUResultsScreen = QtWidgets.QWidget()
        self.GPUResultsScreen.setObjectName("GPUResultsScreen")
        self.stackedWidget.addWidget(self.GPUResultsScreen)

        self.Line8 = QtWidgets.QFrame(self.GPUResultsScreen)
        self.Line8.setGeometry(QtCore.QRect(-10, 414, 961, 20))
        self.Line8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line8.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line8.setObjectName("Line8")
        self.Line8.setStyleSheet("color: white;")

        self.BackButton9 = QtWidgets.QPushButton(self.GPUResultsScreen)
        self.BackButton9.setGeometry(QtCore.QRect(10, 435, 121, 41))
        self.BackButton9.setObjectName("BackButton9")

        self.gpuim1 = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpuim1.setGeometry(QtCore.QRect(50, 50, 200, 200))
        self.gpuim1.setObjectName("gpuim1")
        self.gpuim1.setText("")
        self.gpuim1.setPixmap(QtGui.QPixmap("images/gtx1070.png"))

        self.gpuim2 = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpuim2.setGeometry(QtCore.QRect(650, 50, 200, 200))
        self.gpuim2.setObjectName("gpuim2")
        self.gpuim2.setText("")
        self.gpuim2.setPixmap(QtGui.QPixmap("images/rx480.png"))

        self.gpuperf1 = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpuperf1.setGeometry(QtCore.QRect(50, 260, 300, 40))
        self.gpuperf1.setObjectName("gpuperf1")
        self.gpuperf1.setText("Placeholder.")

        self.gpuperf2 = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpuperf2.setGeometry(QtCore.QRect(550, 260, 300, 40))
        self.gpuperf2.setObjectName("gpuperf2")
        self.gpuperf2.setText("Placeholder.")

        self.gpuprice1 = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpuprice1.setGeometry(QtCore.QRect(50, 310, 300, 40))
        self.gpuprice1.setObjectName("gpuprice1")
        self.gpuprice1.setText("Placeholder.")

        self.gpuprice2 = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpuprice2.setGeometry(QtCore.QRect(550, 310, 300, 40))
        self.gpuprice2.setObjectName("gpuprice2")
        self.gpuprice2.setText("Placeholder.")

        self.gpunum1label = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpunum1label.setGeometry(QtCore.QRect(50, 5, 200, 40))
        self.gpunum1label.setObjectName("gpunum1label")
        self.gpunum1label.setText("GPU #1 Name")
        self.gpunum1label.setStyleSheet("font-weight: bold;")

        self.gpunum2label = QtWidgets.QLabel(self.GPUResultsScreen)
        self.gpunum2label.setGeometry(QtCore.QRect(650, 5, 200, 40))
        self.gpunum2label.setObjectName("gpunum2label")
        self.gpunum2label.setText("GPU #2 Name")
        self.gpunum2label.setStyleSheet("font-weight: bold;")

        # This button brings you back to the main tools screen.
        self.BackButton9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Tools))

        # Results Screen for Game Comparisons.

        self.GameResultsScreen = QtWidgets.QWidget()
        self.GameResultsScreen.setObjectName("GameResultsScreen")
        self.stackedWidget.addWidget(self.GameResultsScreen)

        self.Line9 = QtWidgets.QFrame(self.GameResultsScreen)
        self.Line9.setGeometry(QtCore.QRect(-10, 414, 961, 20))
        self.Line9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line9.setObjectName("Line8")
        self.Line9.setStyleSheet("color: white;")

        self.BackButton10 = QtWidgets.QPushButton(self.GameResultsScreen)
        self.BackButton10.setGeometry(QtCore.QRect(10, 435, 121, 41))
        self.BackButton10.setObjectName("BackButton10")

        self.PcSpecsLabel = QtWidgets.QLabel(self.GameResultsScreen)
        self.PcSpecsLabel.setGeometry(QtCore.QRect(25, 5, 200, 40))
        self.PcSpecsLabel.setObjectName("PcSpecsLabel")
        self.PcSpecsLabel.setText("Your PCs Specifications")
        self.PcSpecsLabel.setStyleSheet("font-weight: bold;")

        self.YourCPULabel = QtWidgets.QLabel(self.GameResultsScreen)
        self.YourCPULabel.setGeometry(QtCore.QRect(25, 50, 200, 40))
        self.YourCPULabel.setObjectName("YourCPULabel")
        self.YourCPULabel.setText("Your CPU: ")

        self.YourGPULabel = QtWidgets.QLabel(self.GameResultsScreen)
        self.YourGPULabel.setGeometry(QtCore.QRect(25, 95, 200, 40))
        self.YourGPULabel.setObjectName("YourGPULabel")
        self.YourGPULabel.setText("Your GPU: ")

        self.YourRAMLabel = QtWidgets.QLabel(self.GameResultsScreen)
        self.YourRAMLabel.setGeometry(QtCore.QRect(25, 140, 200, 40))
        self.YourRAMLabel.setObjectName("YourRAMLabel")
        self.YourRAMLabel.setText("Your RAM: ")

        self.YourStorageLabel = QtWidgets.QLabel(self.GameResultsScreen)
        self.YourStorageLabel.setGeometry(QtCore.QRect(25, 185, 280, 40))
        self.YourStorageLabel.setObjectName("YourStorageLabel")
        self.YourStorageLabel.setText("Your Available Storage Capacity: ")

        self.ResultsLabel = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsLabel.setGeometry(QtCore.QRect(420, 5, 350, 40))
        self.ResultsLabel.setObjectName("ResultsLabel")
        self.ResultsLabel.setText("Results")
        self.ResultsLabel.setStyleSheet("font-weight: bold;")

        self.ResultsMinCPU = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsMinCPU.setGeometry(QtCore.QRect(420, 50, 420, 40))
        self.ResultsMinCPU.setObjectName("ResultsMinCPU")
        self.ResultsMinCPU.setText("Placeholder")

        self.ResultsRecCPU = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsRecCPU.setGeometry(QtCore.QRect(420, 95, 420, 40))
        self.ResultsRecCPU.setObjectName("ResultsRecCPU")
        self.ResultsRecCPU.setText("Placeholder")

        self.ResultsMinGPU = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsMinGPU.setGeometry(QtCore.QRect(420, 140, 420, 40))
        self.ResultsMinGPU.setObjectName("ResultsMinGPU")
        self.ResultsMinGPU.setText("Placeholder")

        self.ResultsRecGPU = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsRecGPU.setGeometry(QtCore.QRect(420, 185, 420, 40))
        self.ResultsRecGPU.setObjectName("ResultsRecGPU")
        self.ResultsRecGPU.setText("Placeholder")

        self.ResultsMinRAM = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsMinRAM.setGeometry(QtCore.QRect(420, 230, 480, 40))
        self.ResultsMinRAM.setObjectName("ResultsMinRAM")
        self.ResultsMinRAM.setText("Placeholder")

        self.ResultsRecRAM = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsRecRAM.setGeometry(QtCore.QRect(420, 275, 480, 40))
        self.ResultsRecRAM.setObjectName("ResultsRecRAM")
        self.ResultsRecRAM.setText("Placeholder")

        self.ResultsStorage = QtWidgets.QLabel(self.GameResultsScreen)
        self.ResultsStorage.setGeometry(QtCore.QRect(420, 320, 420, 40))
        self.ResultsStorage.setObjectName("ResultsStorage")
        self.ResultsStorage.setText("Placeholder")

        # This button brings you back to the main tools screen.
        self.BackButton10.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Tools))

        # Admin screen.

        self.Admin = QtWidgets.QWidget()

        # Creating admin buttons, tabs and entry fields.

        self.Admin.setObjectName("Admin")
        self.AdminTabWidget = QtWidgets.QTabWidget(self.Admin)
        self.AdminTabWidget.setGeometry(QtCore.QRect(0, -10, 941, 501))
        # Creating the tab widget used to hold all of the functions at the admins disposal.
        self.AdminTabWidget.setObjectName("AdminTabWidget")

        self.AddGameTab = QtWidgets.QWidget()
        # Adding the tab for the adding and removal of games.
        self.AddGameTab.setObjectName("AddGameTab")

        self.GameEnter2 = QtWidgets.QLineEdit(self.AddGameTab)
        self.GameEnter2.setGeometry(QtCore.QRect(190, 30, 171, 41))
        self.GameEnter2.setObjectName("GameEnter2")

        self.StorageEnter2 = QtWidgets.QLineEdit(self.AddGameTab)
        self.StorageEnter2.setGeometry(QtCore.QRect(190, 90, 171, 41))
        self.StorageEnter2.setObjectName("StorageEnter2")

        self.GameAddCPUMin = QtWidgets.QComboBox(self.AddGameTab)
        self.GameAddCPUMin.setGeometry(QtCore.QRect(190, 150, 170, 40))
        self.GameAddCPUMin.setObjectName("GameAddCPUMin")

        self.GameAddCPUMinLabel = QtWidgets.QLabel(self.AddGameTab)
        self.GameAddCPUMinLabel.setGeometry(QtCore.QRect(30, 150, 140, 40))
        self.GameAddCPUMinLabel.setObjectName("GameAddCPUMinLabel")

        self.GameAddGPUMin = QtWidgets.QComboBox(self.AddGameTab)
        self.GameAddGPUMin.setGeometry(QtCore.QRect(190, 210, 170, 40))
        self.GameAddGPUMin.setObjectName("GameAddGPUMin")

        self.GameAddGPUMinLabel = QtWidgets.QLabel(self.AddGameTab)
        self.GameAddGPUMinLabel.setGeometry(QtCore.QRect(30, 210, 140, 40))
        self.GameAddGPUMinLabel.setObjectName("GameAddGPUMinLabel")

        self.GameAddRAMMin = QtWidgets.QLineEdit(self.AddGameTab)
        self.GameAddRAMMin.setGeometry(QtCore.QRect(190, 270, 170, 40))
        self.GameAddRAMMin.setObjectName("GameAddRAMMin")

        self.GameAddCPURec = QtWidgets.QComboBox(self.AddGameTab)
        self.GameAddCPURec.setGeometry(QtCore.QRect(600, 30, 170, 40))
        self.GameAddCPURec.setObjectName("GameAddCPURec")

        self.GameAddCPURecLabel = QtWidgets.QLabel(self.AddGameTab)
        self.GameAddCPURecLabel.setGeometry(QtCore.QRect(440, 30, 140, 40))
        self.GameAddCPURecLabel.setObjectName("GameAddCPURecLabel")

        self.GameAddGPURec = QtWidgets.QComboBox(self.AddGameTab)
        self.GameAddGPURec.setGeometry(QtCore.QRect(600, 90, 170, 40))
        self.GameAddGPURec.setObjectName("GameAddGPURec")

        self.GameAddGPURecLabel = QtWidgets.QLabel(self.AddGameTab)
        self.GameAddGPURecLabel.setGeometry(QtCore.QRect(440, 90, 140, 40))
        self.GameAddGPURecLabel.setObjectName("GameAddGPURecLabel")

        self.GameAddRAMRec = QtWidgets.QLineEdit(self.AddGameTab)
        self.GameAddRAMRec.setGeometry(QtCore.QRect(600, 150, 170, 40))
        self.GameAddRAMRec.setObjectName("GameAddRAMRec")

        self.DeleteGame = QtWidgets.QPushButton(self.AddGameTab)
        self.DeleteGame.setGeometry(QtCore.QRect(390, 400, 171, 41))
        self.DeleteGame.setObjectName("DeleteGame")

        self.AddGameSubmit = QtWidgets.QPushButton(self.AddGameTab)
        self.AddGameSubmit.setGeometry(QtCore.QRect(810, 400, 121, 41))
        self.AddGameSubmit.setObjectName("AddGameSubmit")

        self.Line4 = QtWidgets.QFrame(self.AddGameTab)
        self.Line4.setGeometry(QtCore.QRect(0, 380, 961, 20))
        self.Line4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line4.setObjectName("Line4")
        self.Line4.setStyleSheet("color: white;")

        self.BackButton5 = QtWidgets.QPushButton(self.AddGameTab)
        self.BackButton5.setGeometry(QtCore.QRect(10, 400, 121, 41))
        self.BackButton5.setObjectName("BackButton5")

        self.AdminTabWidget.addTab(self.AddGameTab, "")

        # Creation of the tab used to edit the parameters of already existing games.
        self.EditTab = QtWidgets.QWidget()
        self.EditTab.setObjectName("EditTab")

        self.EditSubmit = QtWidgets.QPushButton(self.EditTab)
        self.EditSubmit.setGeometry(QtCore.QRect(810, 400, 121, 41))
        self.EditSubmit.setObjectName("EditSubmit")

        self.BackButton6 = QtWidgets.QPushButton(self.EditTab)
        self.BackButton6.setGeometry(QtCore.QRect(10, 400, 121, 41))
        self.BackButton6.setObjectName("BackButton6")

        self.Line5 = QtWidgets.QFrame(self.EditTab)
        self.Line5.setGeometry(QtCore.QRect(-10, 380, 961, 20))
        self.Line5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line5.setObjectName("Line5")
        self.Line5.setStyleSheet("color: white;")

        self.GameLabel4 = QtWidgets.QLabel(self.EditTab)
        self.GameLabel4.setGeometry(QtCore.QRect(240, 30, 131, 41))
        self.GameLabel4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GameLabel4.setObjectName("GameLabel4")

        self.GameCombo3 = QtWidgets.QComboBox(self.EditTab)
        self.GameCombo3.setGeometry(QtCore.QRect(390, 30, 171, 41))
        self.GameCombo3.setObjectName("GameCombo3")

        self.StorageEnter3 = QtWidgets.QLineEdit(self.EditTab)
        self.StorageEnter3.setGeometry(QtCore.QRect(390, 90, 171, 41))
        self.StorageEnter3.setObjectName("StorageEnter3")

        self.CpuLabel4 = QtWidgets.QLabel(self.EditTab)
        self.CpuLabel4.setGeometry(QtCore.QRect(200, 150, 151, 41))
        self.CpuLabel4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CpuLabel4.setObjectName("CpuLabel4")

        self.CPUCombo4 = QtWidgets.QComboBox(self.EditTab)
        self.CPUCombo4.setGeometry(QtCore.QRect(390, 150, 171, 41))
        self.CPUCombo4.setObjectName("CPUCombo4")

        self.GPULabel4 = QtWidgets.QLabel(self.EditTab)
        self.GPULabel4.setGeometry(QtCore.QRect(200, 210, 151, 41))
        self.GPULabel4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GPULabel4.setObjectName("GPULabel4")

        self.GPUCombo5 = QtWidgets.QComboBox(self.EditTab)
        self.GPUCombo5.setGeometry(QtCore.QRect(390, 210, 171, 41))
        self.GPUCombo5.setObjectName("GPUCombo5")

        self.RamEnter2 = QtWidgets.QLineEdit(self.EditTab)
        self.RamEnter2.setGeometry(QtCore.QRect(390, 270, 171, 41))
        self.RamEnter2.setObjectName("RamEnter2")

        self.MinCheck = QtWidgets.QCheckBox(self.EditTab)
        self.MinCheck.setGeometry(QtCore.QRect(390, 320, 121, 20))
        self.MinCheck.setObjectName("MinCheck")

        self.RecCheck = QtWidgets.QCheckBox(self.EditTab)
        self.RecCheck.setGeometry(QtCore.QRect(390, 350, 151, 20))
        self.RecCheck.setObjectName("RecCheck")

        self.AdminTabWidget.addTab(self.EditTab, "")

        self.CPUAddTab = QtWidgets.QWidget()
        # Creation of the tab used to add new CPUs to the database.
        self.CPUAddTab.setObjectName("CPUAddTab")

        self.NewNameCPUEnter = QtWidgets.QLineEdit(self.CPUAddTab)
        self.NewNameCPUEnter.setGeometry(QtCore.QRect(390, 30, 170, 40))
        self.NewNameCPUEnter.setObjectName("NewNameCPUEnter")

        self.NewPerfCPUEnter = QtWidgets.QLineEdit(self.CPUAddTab)
        self.NewPerfCPUEnter.setGeometry(QtCore.QRect(390, 90, 170, 40))
        self.NewPerfCPUEnter.setObjectName("NewPerfCPUEnter")

        self.NewBrandCPUCombo = QtWidgets.QComboBox(self.CPUAddTab)
        self.NewBrandCPUCombo.setGeometry(QtCore.QRect(390, 150, 170, 40))
        self.NewBrandCPUCombo.setObjectName("NewBrandCPUCombo")

        # This is a list of the brand IDs, used when generating the image used in a CPU comparison.
        cpu_brand_ids = ["i3", "i5", "i7", "i9", "r3", "r5", "r7", "r9"]
        self.NewBrandCPUCombo.addItem('')
        self.NewBrandCPUCombo.addItems(cpu_brand_ids)  # Adding this list to the comboboxes options.

        self.NewBrandCPUComboLabel = QtWidgets.QLabel(self.CPUAddTab)
        self.NewBrandCPUComboLabel.setGeometry(QtCore.QRect(150, 150, 180, 40))
        self.NewBrandCPUComboLabel.setObjectName("NewBrandCPUComboLabel")

        self.NewPriceCPUEnter = QtWidgets.QLineEdit(self.CPUAddTab)
        self.NewPriceCPUEnter.setGeometry(QtCore.QRect(390, 210, 170, 40))
        self.NewPriceCPUEnter.setObjectName("NewPriceCPUEnter")

        self.Line11 = QtWidgets.QFrame(self.CPUAddTab)
        self.Line11.setGeometry(QtCore.QRect(-10, 380, 961, 20))
        self.Line11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line11.setObjectName("Line11")
        self.Line11.setStyleSheet("color: white;")

        self.BackButton11 = QtWidgets.QPushButton(self.CPUAddTab)
        self.BackButton11.setGeometry(QtCore.QRect(10, 400, 121, 41))
        self.BackButton11.setObjectName("BackButton11")

        self.CPUAddSubmit = QtWidgets.QPushButton(self.CPUAddTab)
        self.CPUAddSubmit.setGeometry(QtCore.QRect(810, 400, 121, 41))
        self.CPUAddSubmit.setObjectName("CPUAddSubmit")

        self.AdminTabWidget.addTab(self.CPUAddTab, "")

        self.GPUAddTab = QtWidgets.QWidget()
        # Creation of the tab used to add new GPUs to the database.
        self.GPUAddTab.setObjectName("GPUAddTab")

        self.Line10 = QtWidgets.QFrame(self.GPUAddTab)
        self.Line10.setGeometry(QtCore.QRect(-10, 380, 961, 20))
        self.Line10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line10.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line10.setObjectName("Line10")
        self.Line10.setStyleSheet("color: white;")

        self.NewNameGPUEnter = QtWidgets.QLineEdit(self.GPUAddTab)
        self.NewNameGPUEnter.setGeometry(QtCore.QRect(390, 30, 170, 40))
        self.NewNameGPUEnter.setObjectName("NewNameGPUEnter")

        self.NewPerfGPUEnter = QtWidgets.QLineEdit(self.GPUAddTab)
        self.NewPerfGPUEnter.setGeometry(QtCore.QRect(390, 90, 170, 40))
        self.NewPerfGPUEnter.setObjectName("NewPerfGPUEnter")

        self.NewBrandGPUCombo = QtWidgets.QComboBox(self.GPUAddTab)
        self.NewBrandGPUCombo.setGeometry(QtCore.QRect(390, 150, 170, 40))
        self.NewBrandGPUCombo.setObjectName("NewBrandGPUCombo")

        gpu_brand_ids = ["gx", "rx", "rt"]  # A list of GPU brand IDs.
        self.NewBrandGPUCombo.addItem('')
        self.NewBrandGPUCombo.addItems(gpu_brand_ids)  # Adding these brand IDs to the combobox.

        self.NewBrandGPUComboLabel = QtWidgets.QLabel(self.GPUAddTab)
        self.NewBrandGPUComboLabel.setGeometry(QtCore.QRect(150, 150, 180, 40))
        self.NewBrandCPUComboLabel.setObjectName("NewBrandCPUComboLabel")

        self.NewPriceGPUEnter = QtWidgets.QLineEdit(self.GPUAddTab)
        self.NewPriceGPUEnter.setGeometry(QtCore.QRect(390, 210, 170, 40))
        self.NewPriceGPUEnter.setObjectName("NewPriceGPUEnter")

        self.BackButton12 = QtWidgets.QPushButton(self.GPUAddTab)
        self.BackButton12.setGeometry(QtCore.QRect(10, 400, 121, 41))
        self.BackButton12.setObjectName("BackButton12")

        self.GPUAddSubmit = QtWidgets.QPushButton(self.GPUAddTab)
        self.GPUAddSubmit.setGeometry(QtCore.QRect(810, 400, 121, 41))
        self.GPUAddSubmit.setObjectName("GPUAddSubmit")
        self.AdminTabWidget.addTab(self.GPUAddTab, "")
        self.stackedWidget.addWidget(self.Admin)

        # Adding all the required values from the JSON file to the comboboxes.

        self.GameAddCPUMin.addItem('')
        self.GameAddCPUMin.addItems(list(data['cpus'].keys()))
        self.GameAddCPURec.addItem('')
        self.GameAddCPURec.addItems(list(data['cpus'].keys()))
        self.GameAddGPUMin.addItem('')
        self.GameAddGPUMin.addItems(list(data['gpus'].keys()))
        self.GameAddGPURec.addItem('')
        self.GameAddGPURec.addItems(list(data['gpus'].keys()))

        def AddGame():  # The function for adding a new game to the database.
            try:
                # Here all of the inputs are captured, and typecasting is applied if necessary.
                AddGameName = self.GameEnter2.text()
                AddGameStorage = int(self.StorageEnter2.text())
                AddGameCPUMin = data['cpus'].get(self.GameAddCPUMin.currentText())
                AddGameGPUMin = data['gpus'].get(self.GameAddGPUMin.currentText())
                AddGameRAMMin = int(self.GameAddRAMMin.text())
                AddGameCPURec = data['cpus'].get(self.GameAddCPURec.currentText())
                AddGameGPURec = data['gpus'].get(self.GameAddGPURec.currentText())
                AddGameRAMRec = int(self.GameAddRAMRec.text())
                # These inputs are put into a list which is then used as the value for the key (the game's name) when loaded
                # into the JSON file.
                temp_game_list = [AddGameCPUMin[0], AddGameGPUMin[0], AddGameRAMMin,
                                  AddGameCPURec[0], AddGameGPURec[0], AddGameRAMRec, AddGameStorage]
                games = data['games']
                games[AddGameName] = temp_game_list
                # Opening the JSON file and dumping the new data into it.
                a_file = open("database2.json", "w")
                json.dump(data, a_file, indent=4)
                a_file.close()
                # A message letting the admin know their addition was a success.
                message("Success!", "The game has been added.")
            except:
                # A popup letting the admin know they've left a field blank.
                popup("Fields Blank", "You have left fields blank.")

        def DeleteGame():  # A function for removing a game from the database.
            try:
                # Fetching the name of the game to be deleted.
                RemoveGameName = self.GameEnter2.text()
                # Using the bult in pop method to remove the key and value from the dictionary.
                data['games'].pop(RemoveGameName)
                # Opening the JSON file and dumping the updated information into it.
                a_file = open("database2.json", "w")
                json.dump(data, a_file, indent=4)
                a_file.close()
                # A message letting the admin know their removal of the game successful.
                message("Success!", "The game has been deleted.")
            except:
                # Popup called to warn the admin of the function not working.
                popup("Failure.", "Your input was invalid, you must select a valid game.")

        def AddCPU():  # A function for adding a CPU to the database.
            try:
                # The inputs are collected and typecasted accordingly.
                AddCPUName = self.NewNameCPUEnter.text()
                AddCPUPerf = int(self.NewPerfCPUEnter.text())
                AddCPUBrand = self.NewBrandCPUCombo.currentText()
                AddCPUPrice = int((self.NewPriceCPUEnter.text()))
                # A temporary list is created containing the correct information.
                temp_cpu_list = [AddCPUPerf, AddCPUPrice, AddCPUBrand]
                cpus = data['cpus']
                cpus[AddCPUName] = temp_cpu_list
                a_file = open("database2.json", "w")  # The JSON file is updated.
                json.dump(data, a_file, indent=4)
                a_file.close()
                # A message letting the admin know their addition was successful.
                message("Success!", "The CPU has been added.")
            except:
                popup("Fields Blank", "You have left fields blank.")

        def AddGPU():  # A function for adding a GPU to the database.
            try:
                # The inputs are collected and typecasted accordingly.
                AddGPUName = self.NewNameGPUEnter.text()
                AddGPUPerf = int(self.NewPerfGPUEnter.text())
                AddGPUBrand = self.NewBrandGPUCombo.currentText()
                AddGPUPrice = int((self.NewPriceGPUEnter.text()))
                temp_gpu_list = [AddGPUPerf, AddGPUPrice, AddGPUBrand]
                # A temporary list is created containing the correct information.
                gpus = data['gpus']
                gpus[AddGPUName] = temp_gpu_list
                a_file = open("database2.json", "w")  # The JSON file is updated.
                json.dump(data, a_file, indent=4)
                a_file.close()
                message("Success!", "The GPU has been added.")
            except:
                # Popup called to warn the admin of the function not working.
                popup("Fields Blank", "You have left fields blank.")

        self.GameCombo3.addItem('')
        self.GameCombo3.addItems(list(data['games'].keys()))

        self.CPUCombo4.addItem('')
        self.CPUCombo4.addItems(list(data['cpus'].keys()))

        self.GPUCombo5.addItem('')
        self.GPUCombo5.addItems(list(data['gpus'].keys()))

        def GameModifyAdmin():  # The function for the developers to modify the attributes of a game.
            try:

                game_input4 = str(self.GameCombo3.currentText())
                if game_input4 in list(data['games'].keys()):
                    game_4 = data['games'].get(game_input4)

                cpu_input5 = str(self.CPUCombo4.currentText())
                if cpu_input5 in list(data['cpus'].keys()):
                    cpu_5 = data['cpus'].get(cpu_input5)

                gpu_input5 = str(self.GPUCombo5.currentText())
                if gpu_input5 in list(data['gpus'].keys()):
                    gpu_5 = data['gpus'].get(gpu_input5)

                ram_input3 = self.RamEnter2.text()

                sto_input3 = self.StorageEnter3.text()

                if self.MinCheck.isChecked():
                    game_4[0] = int(cpu_5[0])
                    game_4[1] = int(gpu_5[0])
                    game_4[2] = int(ram_input3)
                    game_4[6] = int(sto_input3)
                    a_file = open("database2.json", "w")
                    json.dump(data, a_file, indent=4)
                    a_file.close()
                    message("Success!", "The minimum requirements have been updated.")
                else:
                    game_4[3] = int(cpu_5[0])
                    game_4[4] = int(gpu_5[0])
                    game_4[5] = int(ram_input3)
                    game_4[6] = int(sto_input3)
                    a_file = open("database2.json", "w")
                    json.dump(data, a_file, indent=4)
                    a_file.close()
                    message("Success!", "The recommended requirements have been updated.")

            except:
                popup("Fields Blank", "You have left fields blank.")

        self.BackButton5.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
        self.BackButton6.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
        self.BackButton12.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
        self.BackButton11.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
        self.EditSubmit.clicked.connect(lambda: GameModifyAdmin())
        self.CPUAddSubmit.clicked.connect(lambda: AddCPU())
        self.GPUAddSubmit.clicked.connect(lambda: AddGPU())
        self.AddGameSubmit.clicked.connect(lambda: AddGame())
        self.DeleteGame.clicked.connect(lambda: DeleteGame())

        # Developer screen.

        self.Developer = QtWidgets.QWidget()

        # Creating developer tabs, buttons and entry fields.

        self.Developer.setObjectName("Developer")
        self.DeveloperTabWidget = QtWidgets.QTabWidget(self.Developer)
        self.DeveloperTabWidget.setGeometry(QtCore.QRect(0, 0, 941, 501))
        self.DeveloperTabWidget.setObjectName("DeveloperTabWidget")

        self.DevModify = QtWidgets.QWidget()
        self.DevModify.setObjectName("DevModify")

        self.BackButton7 = QtWidgets.QPushButton(self.DevModify)
        self.BackButton7.setGeometry(QtCore.QRect(10, 390, 121, 41))
        self.BackButton7.setObjectName("BackButton7")

        self.Line6 = QtWidgets.QFrame(self.DevModify)
        self.Line6.setGeometry(QtCore.QRect(-10, 370, 961, 20))
        self.Line6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line6.setObjectName("Line6")
        self.Line6.setStyleSheet("color: white;")

        self.DevModSubmit = QtWidgets.QPushButton(self.DevModify)
        self.DevModSubmit.setGeometry(QtCore.QRect(800, 390, 121, 41))
        self.DevModSubmit.setObjectName("DevModSubmit")

        self.GPULabel5 = QtWidgets.QLabel(self.DevModify)
        self.GPULabel5.setGeometry(QtCore.QRect(230, 200, 151, 41))
        self.GPULabel5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GPULabel5.setObjectName("GPULabel5")

        self.RecCheck_2 = QtWidgets.QCheckBox(self.DevModify)
        self.RecCheck_2.setGeometry(QtCore.QRect(420, 340, 151, 20))
        self.RecCheck_2.setObjectName("RecCheck_2")

        self.GameCombo5 = QtWidgets.QComboBox(self.DevModify)
        self.GameCombo5.setGeometry(QtCore.QRect(420, 20, 171, 41))
        self.GameCombo5.setObjectName("GameCombo5")

        self.CPUCombo6 = QtWidgets.QComboBox(self.DevModify)
        self.CPUCombo6.setGeometry(QtCore.QRect(420, 140, 171, 41))
        self.CPUCombo6.setObjectName("CPUCombo6")

        self.MinCheck_2 = QtWidgets.QCheckBox(self.DevModify)
        self.MinCheck_2.setGeometry(QtCore.QRect(420, 310, 121, 20))
        self.MinCheck_2.setObjectName("MinCheck_2")

        self.StorageEnter4 = QtWidgets.QLineEdit(self.DevModify)
        self.StorageEnter4.setGeometry(QtCore.QRect(420, 80, 171, 41))
        self.StorageEnter4.setObjectName("StorageEnter4")

        self.CPULabel5 = QtWidgets.QLabel(self.DevModify)
        self.CPULabel5.setGeometry(QtCore.QRect(230, 140, 151, 41))
        self.CPULabel5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CPULabel5.setObjectName("CPULabel5")

        self.RamEnter4 = QtWidgets.QLineEdit(self.DevModify)
        self.RamEnter4.setGeometry(QtCore.QRect(420, 260, 171, 41))
        self.RamEnter4.setObjectName("RamEnter4")

        self.GPUCombo6 = QtWidgets.QComboBox(self.DevModify)
        self.GPUCombo6.setGeometry(QtCore.QRect(420, 200, 171, 41))
        self.GPUCombo6.setObjectName("GPUCombo6")

        self.GameLabel5 = QtWidgets.QLabel(self.DevModify)
        self.GameLabel5.setGeometry(QtCore.QRect(270, 20, 131, 41))
        self.GameLabel5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GameLabel5.setObjectName("GameLabel5")

        self.DeveloperTabWidget.addTab(self.DevModify, "")

        self.stackedWidget.addWidget(self.Developer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Developer functions.

        self.GameCombo5.addItem('')
        self.GameCombo5.addItems(list(data['games'].keys()))

        self.CPUCombo6.addItem('')
        self.CPUCombo6.addItems(list(data['cpus'].keys()))

        self.GPUCombo6.addItem('')
        self.GPUCombo6.addItems(list(data['gpus'].keys()))

        def GameModify():  # The function called to modify the requirements of a game.
            try:

                game_input5 = str(self.GameCombo5.currentText())  # Selecting the game to modify.
                if game_input5 in list(data['games'].keys()):
                    game_5 = data['games'].get(game_input5)

                # Selecting the recommended/minimum CPU.
                cpu_input6 = str(self.CPUCombo6.currentText())
                if cpu_input6 in list(data['cpus'].keys()):
                    cpu_6 = data['cpus'].get(cpu_input6)

                # Selecting the recommended/minimum GPU.
                gpu_input6 = str(self.GPUCombo6.currentText())
                if gpu_input6 in list(data['gpus'].keys()):
                    gpu_6 = data['gpus'].get(gpu_input6)

                ram_input4 = self.RamEnter4.text()  # Entering the RAM.

                sto_input4 = self.StorageEnter4.text()  # Entering the amount of storage.

                if self.MinCheck_2.isChecked():  # If the minimum requirement checkbox has been checked.
                    game_5[0] = int(cpu_6[0])  # Setting the array values to the input values.
                    game_5[1] = int(gpu_6[0])
                    game_5[2] = int(ram_input4)
                    game_5[6] = int(sto_input4)
                    # Opening the JSON file and dumping the new data.
                    a_file = open("database2.json", "w")
                    json.dump(data, a_file, indent=4)
                    a_file.close()
                    # Prompt that something happened.
                    message("Success!", "The minimum requirements have been updated.")
                else:
                    game_5[3] = int(cpu_6[0])
                    game_5[4] = int(gpu_6[0])
                    game_5[5] = int(ram_input4)
                    game_5[6] = int(sto_input4)
                    a_file = open("database2.json", "w")
                    json.dump(data, a_file, indent=4)
                    a_file.close()
                    message("Success!", "The recommended requirements have been updated.")

            except:
                popup("Fields Blank", "You have left fields blank.")  # Error message.

        self.BackButton7.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
        self.DevModSubmit.clicked.connect(lambda: GameModify())

        # Setting the default positions for the tab widgets.

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.ToolsTabWidget.setCurrentIndex(0)
        self.AdminTabWidget.setCurrentIndex(0)
        self.DeveloperTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # RetranslateUi function called.

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hardware - Game Comparison Tool"))
        self.AdminButton.setText(_translate("MainWindow", "ADMIN LOGIN"))
        self.UserButton.setText(_translate("MainWindow", "USER TOOLS"))
        self.ExitButton.setText(_translate("MainWindow", "EXIT"))
        self.Username.setPlaceholderText(_translate("MainWindow", " USERNAME:"))
        self.Password.setPlaceholderText(_translate("MainWindow", " PASSWORD:"))
        self.BackButton1.setText(_translate("MainWindow", "BACK"))
        self.LoginSubmitButton.setText(_translate("MainWindow", "SUBMIT"))
        self.BackButton2.setText(_translate("MainWindow", "BACK"))
        self.GameLabel1.setText(_translate("MainWindow", "Select Game:"))
        self.CPULabel1.setText(_translate("MainWindow", "Select CPU:"))
        self.GPULabel1.setText(_translate("MainWindow", "Select GPU:"))
        self.RamEnter1.setPlaceholderText(_translate("MainWindow", " ENTER RAM:"))
        self.StorageEnter1.setPlaceholderText(_translate("MainWindow", " ENTER STORAGE:"))
        self.GameSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.ToolsTabWidget.setTabText(self.ToolsTabWidget.indexOf(
            self.GameTab), _translate("MainWindow", "What Games will my PC Run?"))
        self.BackButton3.setText(_translate("MainWindow", "BACK"))
        self.CPUSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.CPULabel2.setText(_translate("MainWindow", "Select CPU #1:"))
        self.CPULabel3.setText(_translate("MainWindow", "Select CPU #2:"))
        self.ToolsTabWidget.setTabText(self.ToolsTabWidget.indexOf(
            self.CPUTab), _translate("MainWindow", "Compare two CPUs"))
        self.GPUSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.BackButton4.setText(_translate("MainWindow", "BACK"))
        self.GPULabel2.setText(_translate("MainWindow", "Select GPU #1:"))
        self.GPULabel3.setText(_translate("MainWindow", "Select GPU #2:"))
        self.ToolsTabWidget.setTabText(self.ToolsTabWidget.indexOf(
            self.GPUTab), _translate("MainWindow", "Compare two GPUs"))
        self.DeleteGame.setText(_translate("MainWindow", "DELETE GAME"))
        self.AddGameSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.BackButton5.setText(_translate("MainWindow", "BACK"))
        self.AdminTabWidget.setTabText(self.AdminTabWidget.indexOf(
            self.AddGameTab), _translate("MainWindow", "Add or Remove a Game"))
        self.EditSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.BackButton6.setText(_translate("MainWindow", "BACK"))
        self.GameLabel4.setText(_translate("MainWindow", "Select Game:"))
        self.StorageEnter3.setPlaceholderText(_translate("MainWindow", " Enter new Storage:"))
        self.CpuLabel4.setText(_translate("MainWindow", "Select New CPU:"))
        self.GPULabel4.setText(_translate("MainWindow", "Select New GPU:"))
        self.RamEnter2.setPlaceholderText(_translate("MainWindow", " Enter New RAM:"))
        self.MinCheck.setText(_translate("MainWindow", "Minimum"))
        self.RecCheck.setText(_translate("MainWindow", "Recommended"))
        self.AdminTabWidget.setTabText(self.AdminTabWidget.indexOf(
            self.EditTab), _translate("MainWindow", "Edit Game Requirements"))
        self.AdminTabWidget.setTabText(self.AdminTabWidget.indexOf(
            self.CPUAddTab), _translate("MainWindow", "Add a CPU"))
        self.AdminTabWidget.setTabText(self.AdminTabWidget.indexOf(
            self.GPUAddTab), _translate("MainWindow", "Add a GPU"))
        self.BackButton7.setText(_translate("MainWindow", "BACK"))
        self.DevModSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.CPUAddSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.GPUAddSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.GPULabel5.setText(_translate("MainWindow", "Select New GPU:"))
        self.RecCheck_2.setText(_translate("MainWindow", "Recommended"))
        self.MinCheck_2.setText(_translate("MainWindow", "Minimum"))
        self.StorageEnter4.setPlaceholderText(_translate("MainWindow", " Enter new Storage:"))
        self.CPULabel5.setText(_translate("MainWindow", "Select New CPU:"))
        self.RamEnter4.setPlaceholderText(_translate("MainWindow", " Enter New RAM:"))
        self.GameLabel5.setText(_translate("MainWindow", "Select Game:"))
        self.DeveloperTabWidget.setTabText(self.DeveloperTabWidget.indexOf(
            self.DevModify), _translate("MainWindow", "Modify a Game\'s Requirements"))
        self.BackButton8.setText(_translate("MainWindow", "BACK"))
        self.BackButton9.setText(_translate("MainWindow", "BACK"))
        self.BackButton10.setText(_translate("MainWindow", "BACK"))
        self.BackButton11.setText(_translate("MainWindow", "BACK"))
        self.BackButton12.setText(_translate("MainWindow", "BACK"))
        self.NewNameCPUEnter.setPlaceholderText(_translate("MainWindow", "Enter CPU Name:"))
        self.NewPerfCPUEnter.setPlaceholderText(_translate("MainWindow", "Enter CPU Performance:"))
        self.NewNameGPUEnter.setPlaceholderText(_translate("MainWindow", "Enter GPU Name:"))
        self.NewPerfGPUEnter.setPlaceholderText(_translate("MainWindow", "Enter GPU Performance:"))
        self.NewBrandCPUComboLabel.setText(_translate("MainWindow", "Select the CPU Brand ID:"))
        self.NewBrandGPUComboLabel.setText(_translate("MainWindow", "Select the GPU Brand ID:"))
        self.NewPriceCPUEnter.setPlaceholderText(_translate("MainWindow", "Enter CPU Price:"))
        self.NewPriceGPUEnter.setPlaceholderText(_translate("MainWindow", "Enter GPU Price:"))
        self.StorageEnter2.setPlaceholderText(_translate("MainWindow", "Enter Storage:"))
        self.GameAddCPUMinLabel.setText(_translate("MainWindow", "Select Min CPU:"))
        self.GameAddGPUMinLabel.setText(_translate("MainWindow", "Select Min GPU:"))
        self.GameAddRAMMin.setPlaceholderText(_translate("MainWindow", "Enter Min RAM:"))
        self.GameAddCPURecLabel.setText(_translate("MainWindow", "Enter Rec CPU:"))
        self.GameAddGPURecLabel.setText(_translate("MainWindow", "Enter Rec GPU:"))
        self.GameAddRAMRec.setPlaceholderText(_translate("MainWindow", "Enter Rec RAM:"))
        self.GameEnter2.setPlaceholderText(_translate("MainWindow", "Enter Game:"))


if __name__ == "__main__":  # Makes sure this is the main file.
    app = QtWidgets.QApplication(sys.argv)  # Creating an application object.
    MainWindow = QtWidgets.QMainWindow()  # Defining the mainwindow.
    ui = Ui_MainWindow()  # Defining the UI.
    ui.setupUi(MainWindow)
    MainWindow.show()  # Shows the mainwindow.
    sys.exit(app.exec_())
