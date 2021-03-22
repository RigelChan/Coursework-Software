# The full code for my Computer Science 2020 Coursework.

from database_module import CPU_DATA, CPU, CPU_NAMES, GPU_DATA, GPU, GPU_NAMES, GAME_DATA, GAME, GAME_NAMES
from PyQt5 import QtCore, QtGui, QtWidgets  # Importing the necessary PyQt5 modules.
from PyQt5.QtWidgets import QMessageBox
import sys # Importing the sys module.


class Ui_MainWindow(object):  # Class definition for the main window.
    def setupUi(self, MainWindow):  # The main setupUi function, this creates all of the UI elements in the program.
        MainWindow.setObjectName("MainWindow")  # Giving the main window a name.
        MainWindow.resize(960, 540)  # Defining the size of the window.
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))  # These two lines of code make it so the window cannot be resized, 
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
        self.AdminButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
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


        def loginValidation():  # Login validation function.
            if 0 < len(self.Username.text()) <= 12:  # This line works as a range check, and a presence check, as the input cannot be 0 characters long.
                if self.Username.text() in ADMIN_US and self.Password.text() in ADMIN_PW:  # Checks if the inputs are for an admin.
                    self.stackedWidget.setCurrentWidget(self.Admin)  # Switches to the admin screen.
                    self.Username.clear()  # Clears the username field.
                    self.Password.clear()  # Clears the passworld field.
                    print("Taken to admin screen.")  # For debug use only.
                elif self.Username.text() in USER_US and self.Password.text() in USER_PW:  # Checks if the inputs are for a developer.
                    self.stackedWidget.setCurrentWidget(self.Developer)  # Switches to the developer screen.
                    self.Username.clear()  # Clears the username field.
                    self.Password.clear()  # Clears the password field.
                    print("Taken to developer screen.")  # For debug use only.    
            else:
                popup("Invalid Input", "The input is out of range.")  # Calling the popup function.
            
        # Adding functionality to the buttons.

        self.BackButton1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))  # Brings the user back to the main menu screen.
        self.LoginSubmitButton.clicked.connect(lambda: loginValidation())  # Calls the login validation function.

        # Tools screen.
        
        self.Tools = QtWidgets.QWidget()

        # Tools buttons, entry fields and tabs.

        self.Tools.setObjectName("Tools")
        self.ToolsTabWidget = QtWidgets.QTabWidget(self.Tools)
        self.ToolsTabWidget.setGeometry(QtCore.QRect(0, 0, 941, 491))
        self.ToolsTabWidget.setObjectName("ToolsTabWidget")

        self.GameTab = QtWidgets.QWidget()
        self.GameTab.setObjectName("GameTab")

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

        self.CPUTab = QtWidgets.QWidget()
        self.CPUTab.setAutoFillBackground(False)
        self.CPUTab.setObjectName("CPUTab")

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

        self.GPUTab = QtWidgets.QWidget()
        self.GPUTab.setObjectName("GPUTab")

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
        self.TutorialTab = QtWidgets.QWidget()
        self.TutorialTab.setObjectName("TutorialTab")
        self.ToolsTabWidget.addTab(self.TutorialTab, "")
        self.stackedWidget.addWidget(self.Tools)

        # Functionality.

        self.CPUCombo1.addItem('')
        self.CPUCombo1.addItems(CPU_NAMES.keys())
        self.CPUCombo2.addItem('')
        self.CPUCombo2.addItems(CPU_NAMES.keys())
        self.CPUCombo3.addItem('')
        self.CPUCombo3.addItems(CPU_NAMES.keys())

        self.GPUCombo1.addItem('')
        self.GPUCombo1.addItems(GPU_NAMES.keys())
        self.GPUCombo2.addItem('')
        self.GPUCombo2.addItems(GPU_NAMES.keys())
        self.GPUCombo3.addItem('')
        self.GPUCombo3.addItems(GPU_NAMES.keys())

        self.GameCombo1.addItem('')
        self.GameCombo1.addItems(GAME_NAMES.keys())

        def GameCompare():
            try:
                game_input1 = str(self.GameCombo1.currentText())
                if game_input1 in GAME_NAMES.keys():
                    game_1 = GAME_NAMES.get(game_input1.upper())  # Fetches the array containing the game's requirements: CPU_Min, GPU_Min, RAM_Min, CPU_Rec, GPU_Rec, RAM_Rec, Storage

                cpu_input1 = str(self.CPUCombo1.currentText())
                if cpu_input1 in CPU_NAMES.keys():
                    cpu_1 = CPU_NAMES.get(cpu_input1.upper())  # Fetches the information related to the selected CPU.

                gpu_input1 = str(self.GPUCombo1.currentText())
                if gpu_input1 in GPU_NAMES.keys():
                    gpu_1 = GPU_NAMES.get(gpu_input1.upper())  # Fetches the information related to the selected GPU.

                ram_input1 = self.RamEnter1.text()  # Fetches the entered amount of ram.

                sto_input1 = self.StorageEnter1.text()  # Fetches the entered amount of storage capacity.

                if game_1[0][0] <= cpu_1[0]:
                    print("The CPU meets the minimum requirements.")
                else:
                    print("The CPU doesn't meet the minimum requirements.")

                if game_1[1][0] <= gpu_1[0]:
                    print("The GPU meets the minimum requirements.")
                else:
                    print("The GPU doesn't meet the minimum requirements.")

                if game_1[2] <= int(ram_input1):
                    print("The amount of RAM meets the minimum requirements.")
                else:
                    print("The amount of RAM doesn't meet the minimum requirements.")

                if game_1[3][0] <= cpu_1[0]:
                    print("The CPU meets the recommended requirements.")
                else:
                    print("The CPU doesn't meet the recommended requirements.")

                if game_1[4][0] <= gpu_1[0]:
                    print("The GPU meets the minimum requirements.")
                else:
                    print("The GPU doesn't meet the recommended requirements.")

                if game_1[5] <= int(ram_input1):
                    print("The amount of RAM meets the recommended requirements.")
                else:
                    print("The amount of RAM doesn't meet the recommended requirements.")

                if game_1[6] <= int(sto_input1):
                    print("The amount of storage capacity if sufficient.")
                else:
                    print("The amount of storage capacity if insufficient.")
                self.stackedWidget.setCurrentWidget(self.GameResultsScreen)
                
            except:
                popup("Fields Blank", "You have left fields blank.")

        def CPUCompare():
            try:
                cpu_input2 = str(self.CPUCombo2.currentText())
                if cpu_input2 in CPU_NAMES.keys() and len(cpu_input2) != 0:
                    cpu_2 = CPU_NAMES.get(cpu_input2.upper())
                else:
                    popup("Field Blank", "There is no input for CPU #1")

                if cpu_2[2] == 'r5':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/ryzen53600.png"))
                elif cpu_2[2] == 'i7':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/i77700k.png"))
                elif cpu_2[2] == 'tr':
                    self.cpuim1.setPixmap(QtGui.QPixmap("images/thr2990wx.png"))

                cpu_input3 = str(self.CPUCombo3.currentText())
                if cpu_input3 in CPU_NAMES.keys() and len(cpu_input3) != 0:
                    cpu_3 = CPU_NAMES.get(cpu_input3.upper())
                    self.stackedWidget.setCurrentWidget(self.CPUResultsScreen)

                    self.cpunum1label.setText(cpu_input2)
                    self.cpuperf1.setText("This CPU has a performance score of: " + cpu_2[0])
                    self.cpuprice1.setText("This CPU has a price of: £" + cpu_2[1])

                    self.cpunum2label.setText(cpu_input3)
                    self.cpuperf2.setText("This CPU has a performance score of: " + cpu_3[0])
                    self.cpuprice2.setText("This CPU has a price of: £" + cpu_3[1])       
                else:
                    popup("Field Blank", "There is no input for CPU #2")

                if cpu_3[2] == 'r5':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/ryzen53600.png"))
                elif cpu_3[2] == 'i7':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/i77700k.png"))
                elif cpu_3[2] == 'tr':
                    self.cpuim2.setPixmap(QtGui.QPixmap("images/thr2990wx.png"))

            except:
                pass

        def GPUCompare():
            gpu_input2 = str(self.GPUCombo2.currentText())
            if gpu_input2 in GPU_NAMES.keys() and len(gpu_input2) != 0:
                gpu_2 = GPU_NAMES.get(gpu_input2.upper())
            else:
                popup("Field Blank", "There is no input for GPU #1")

            if gpu_2[2] == 'gx':
                self.gpuim1.setPixmap(QtGui.QPixmap("images/gtx1070.png"))
            elif gpu_2[2] == 'rx':
                self.gpuim1.setPixmap(QtGui.QPixmap("images/rx480.png"))
            elif gpu_2[2] == 'rt':
                self.gpuim1.setPixmap(QtGui.QPixmap("images/rtx2060.png"))

            gpu_input3 = str(self.GPUCombo3.currentText())
            if gpu_input3 in GPU_NAMES.keys() and len(gpu_input3) != 0:
                gpu_3 = GPU_NAMES.get(gpu_input3.upper())
                self.stackedWidget.setCurrentWidget(self.GPUResultsScreen)

                self.gpunum1label.setText(gpu_input2)
                self.gpuperf1.setText("This GPU has a performance of: " + gpu_2[0])
                self.gpuprice1.setText("This GPU has a price of: £" + gpu_2[1])

                self.gpunum2label.setText(gpu_input3)
                self.gpuperf2.setText("This GPU has a performance score of: " + gpu_3[0])
                self.gpuprice2.setText("This GPU has a price of: £" + gpu_3[1])

            else:
                popup("Field Blank", "There is no input for GPU #2")

            if gpu_3[2] == 'gx':
                self.gpuim2.setPixmap(QtGui.QPixmap("images/gtx1070.png"))
            elif gpu_3[2] == 'rx':
                self.gpuim2.setPixmap(QtGui.QPixmap("images/rx480.png"))
            elif gpu_3[2] == 'rt':
                self.gpuim2.setPixmap(QtGui.QPixmap("images/rtx2060.png"))

        self.CPUSubmit.clicked.connect(lambda: CPUCompare())
        self.GPUSubmit.clicked.connect(lambda: GPUCompare())
        self.GameSubmit.clicked.connect(lambda: GameCompare())
        self.BackButton2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))
        self.BackButton3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))
        self.BackButton4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainMenuPage))

        # Results Screen for CPUs.

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
        self.cpuim1.setPixmap(QtGui.QPixmap("images/ryzen53600.png"))

        self.cpuim2 = QtWidgets.QLabel(self.CPUResultsScreen)
        self.cpuim2.setGeometry(QtCore.QRect(650, 50, 200, 200))
        self.cpuim2.setObjectName("cpuim2")
        self.cpuim2.setText("")
        self.cpuim2.setPixmap(QtGui.QPixmap("images/i77700k.png"))

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

        self.BackButton8.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Tools))

        # Results Screen for GPUs.

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
        self.BackButton10.setObjectName("BackButton9")

        self.BackButton10.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Tools))

        # Admin screen.

        self.Admin = QtWidgets.QWidget()

        # Creating admin buttons, tabs and entry fields.

        self.Admin.setObjectName("Admin")
        self.AdminTabWidget = QtWidgets.QTabWidget(self.Admin)
        self.AdminTabWidget.setGeometry(QtCore.QRect(0, -10, 941, 501))
        self.AdminTabWidget.setObjectName("AdminTabWidget")

        self.RequirementTab = QtWidgets.QWidget()
        self.RequirementTab.setObjectName("RequirementTab")

        self.GameLabel2 = QtWidgets.QLabel(self.RequirementTab)
        self.GameLabel2.setGeometry(QtCore.QRect(240, 60, 121, 41))
        self.GameLabel2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GameLabel2.setObjectName("GameLabel2")

        self.GameCombo2 = QtWidgets.QComboBox(self.RequirementTab)
        self.GameCombo2.setGeometry(QtCore.QRect(390, 60, 171, 41))
        self.GameCombo2.setObjectName("GameCombo2")

        self.StorageLabel1 = QtWidgets.QLabel(self.RequirementTab)
        self.StorageLabel1.setGeometry(QtCore.QRect(230, 120, 131, 41))
        self.StorageLabel1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StorageLabel1.setObjectName("StorageLabel1")

        self.StorageEnter2 = QtWidgets.QLineEdit(self.RequirementTab)
        self.StorageEnter2.setGeometry(QtCore.QRect(390, 120, 171, 41))
        self.StorageEnter2.setObjectName("StorageEnter2")

        self.RecRequirements = QtWidgets.QPushButton(self.RequirementTab)
        self.RecRequirements.setGeometry(QtCore.QRect(390, 180, 171, 41))
        self.RecRequirements.setObjectName("RecRequirements")

        self.MinRequirements = QtWidgets.QPushButton(self.RequirementTab)
        self.MinRequirements.setGeometry(QtCore.QRect(390, 240, 171, 41))
        self.MinRequirements.setObjectName("MinRequirements")

        self.SaveButton1 = QtWidgets.QPushButton(self.RequirementTab)
        self.SaveButton1.setGeometry(QtCore.QRect(390, 300, 171, 41))
        self.SaveButton1.setObjectName("SaveButton1")

        self.Delete1 = QtWidgets.QPushButton(self.RequirementTab)
        self.Delete1.setGeometry(QtCore.QRect(390, 400, 171, 41))
        self.Delete1.setObjectName("Delete1")

        self.RequirementSubmit = QtWidgets.QPushButton(self.RequirementTab)
        self.RequirementSubmit.setGeometry(QtCore.QRect(810, 400, 121, 41))
        self.RequirementSubmit.setObjectName("RequirementSubmit")

        self.Line4 = QtWidgets.QFrame(self.RequirementTab)
        self.Line4.setGeometry(QtCore.QRect(0, 380, 961, 20))
        self.Line4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line4.setObjectName("Line4")
        self.Line4.setStyleSheet("color: white;")

        self.BackButton5 = QtWidgets.QPushButton(self.RequirementTab)
        self.BackButton5.setGeometry(QtCore.QRect(10, 400, 121, 41))
        self.BackButton5.setObjectName("BackButton5")

        self.AdminTabWidget.addTab(self.RequirementTab, "")

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
        self.AdminTutorial = QtWidgets.QWidget()
        self.AdminTutorial.setObjectName("AdminTutorial")

        self.AdminTabWidget.addTab(self.AdminTutorial, "")
        self.stackedWidget.addWidget(self.Admin)

        self.OutputScreen = QtWidgets.QWidget()
        self.OutputScreen.setObjectName("OutputScreen")
        self.stackedWidget.addWidget(self.OutputScreen)

        # Functionality.

        self.BackButton5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))
        self.BackButton6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))

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
        
        self.DeveloperTutorial = QtWidgets.QWidget()
        self.DeveloperTutorial.setObjectName("DeveloperTutorial")
        self.DeveloperTabWidget.addTab(self.DeveloperTutorial, "")
        self.stackedWidget.addWidget(self.Developer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Developer functions.

        self.BackButton7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.LoginScreen))

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Coursework App - Beta"))
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
        self.ToolsTabWidget.setTabText(self.ToolsTabWidget.indexOf(self.GameTab), _translate("MainWindow", "What Games will my PC Run?"))
        self.BackButton3.setText(_translate("MainWindow", "BACK"))
        self.CPUSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.CPULabel2.setText(_translate("MainWindow", "Select CPU #1:"))
        self.CPULabel3.setText(_translate("MainWindow", "Select CPU #2:"))
        self.ToolsTabWidget.setTabText(self.ToolsTabWidget.indexOf(self.CPUTab), _translate("MainWindow", "Compare two CPUs"))
        self.GPUSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.BackButton4.setText(_translate("MainWindow", "BACK"))
        self.GPULabel2.setText(_translate("MainWindow", "Select GPU #1:"))
        self.GPULabel3.setText(_translate("MainWindow", "Select GPU #2:"))
        self.ToolsTabWidget.setTabText(self.ToolsTabWidget.indexOf(self.GPUTab), _translate("MainWindow", "Compare two GPUs"))
        self.ToolsTabWidget.setTabText(self.ToolsTabWidget.indexOf(self.TutorialTab), _translate("MainWindow", "User Tutorial"))
        self.GameLabel2.setText(_translate("MainWindow", "Select Game:"))
        self.StorageLabel1.setText(_translate("MainWindow", "Enter Storage:"))
        self.RecRequirements.setText(_translate("MainWindow", "Set Rec Reqs"))
        self.MinRequirements.setText(_translate("MainWindow", "Set Min Reqs"))
        self.SaveButton1.setText(_translate("MainWindow", "SAVE"))
        self.Delete1.setText(_translate("MainWindow", "DELETE GAME"))
        self.RequirementSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.BackButton5.setText(_translate("MainWindow", "BACK"))
        self.AdminTabWidget.setTabText(self.AdminTabWidget.indexOf(self.RequirementTab), _translate("MainWindow", "Add or Remove a Game"))
        self.EditSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.BackButton6.setText(_translate("MainWindow", "BACK"))
        self.GameLabel4.setText(_translate("MainWindow", "Select Game:"))
        self.StorageEnter3.setPlaceholderText(_translate("MainWindow", " Enter new Storage:"))
        self.CpuLabel4.setText(_translate("MainWindow", "Select New CPU:"))
        self.GPULabel4.setText(_translate("MainWindow", "Select New GPU:"))
        self.RamEnter2.setPlaceholderText(_translate("MainWindow", " Enter New RAM:"))
        self.MinCheck.setText(_translate("MainWindow", "Minimum"))
        self.RecCheck.setText(_translate("MainWindow", "Recommended"))
        self.AdminTabWidget.setTabText(self.AdminTabWidget.indexOf(self.EditTab), _translate("MainWindow", "Edit Game Requirements"))
        self.AdminTabWidget.setTabText(self.AdminTabWidget.indexOf(self.AdminTutorial), _translate("MainWindow", "Admin Tutorial"))
        self.BackButton7.setText(_translate("MainWindow", "BACK"))
        self.DevModSubmit.setText(_translate("MainWindow", "SUBMIT"))
        self.GPULabel5.setText(_translate("MainWindow", "Select New GPU:"))
        self.RecCheck_2.setText(_translate("MainWindow", "Recommended"))
        self.MinCheck_2.setText(_translate("MainWindow", "Minimum"))
        self.StorageEnter4.setPlaceholderText(_translate("MainWindow", " Enter new Storage:"))
        self.CPULabel5.setText(_translate("MainWindow", "Select New CPU:"))
        self.RamEnter4.setPlaceholderText(_translate("MainWindow", " Enter New RAM:"))
        self.GameLabel5.setText(_translate("MainWindow", "Select Game:"))
        self.DeveloperTabWidget.setTabText(self.DeveloperTabWidget.indexOf(self.DevModify), _translate("MainWindow", "Modify a Game\'s Requirements"))
        self.DeveloperTabWidget.setTabText(self.DeveloperTabWidget.indexOf(self.DeveloperTutorial), _translate("MainWindow", "Developer Tutorial"))
        self.BackButton8.setText(_translate("MainWindow", "BACK"))
        self.BackButton9.setText(_translate("MainWindow", "BACK"))
        self.BackButton10.setText(_translate("MainWindow", "BACK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
