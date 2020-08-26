#! /bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from random import shuffle,choice

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rock = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rock.sizePolicy().hasHeightForWidth())
        self.rock.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(34)
        font.setItalic(False)
        self.rock.setFont(font)
        self.rock.setObjectName("rock")
        self.verticalLayout_2.addWidget(self.rock)
        self.paper = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paper.sizePolicy().hasHeightForWidth())
        self.paper.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(34)
        self.paper.setFont(font)
        self.paper.setObjectName("paper")
        self.verticalLayout_2.addWidget(self.paper)
        self.scissers = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scissers.sizePolicy().hasHeightForWidth())
        self.scissers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(34)
        self.scissers.setFont(font)
        self.scissers.setObjectName("scissers")
        self.verticalLayout_2.addWidget(self.scissers)
        self.gridLayout.addWidget(self.widget, 1, 0, 3, 6)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pcLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(26)
        self.pcLabel.setFont(font)
        self.pcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pcLabel.setObjectName("pcLabel")
        self.gridLayout_3.addWidget(self.pcLabel, 0, 2, 1, 1)
        self.plWinLcd = QtWidgets.QLCDNumber(self.frame)
        self.plWinLcd.setObjectName("plWinLcd")
        self.gridLayout_3.addWidget(self.plWinLcd, 0, 1, 1, 1)
        self.plLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(26)
        self.plLabel.setFont(font)
        self.plLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.plLabel.setObjectName("plLabel")
        self.gridLayout_3.addWidget(self.plLabel, 0, 0, 1, 1)
        self.pcWinLcd = QtWidgets.QLCDNumber(self.frame)
        self.pcWinLcd.setObjectName("pcWinLcd")
        self.gridLayout_3.addWidget(self.pcWinLcd, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 6)
        self.resetBot = QtWidgets.QPushButton(self.centralwidget)
        self.resetBot.setObjectName("resetBot")
        self.gridLayout.addWidget(self.resetBot, 6, 0, 1, 1)
        self.pcChoiceOut = QtWidgets.QLineEdit(self.centralwidget)
        self.pcChoiceOut.setMouseTracking(False)
        self.pcChoiceOut.setAcceptDrops(False)
        self.pcChoiceOut.setReadOnly(True)
        self.pcChoiceOut.setObjectName("pcChoiceOut")
        self.gridLayout.addWidget(self.pcChoiceOut, 6, 3, 1, 1)
        self.pcChoice = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(16)
        self.pcChoice.setFont(font)
        self.pcChoice.setAlignment(QtCore.Qt.AlignCenter)
        self.pcChoice.setObjectName("pcChoice")
        self.gridLayout.addWidget(self.pcChoice, 6, 1, 1, 1)
        self.roundLcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.roundLcd.setObjectName("roundLcd")
        self.gridLayout.addWidget(self.roundLcd, 6, 5, 1, 1)
        self.round = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(21)
        self.round.setFont(font)
        self.round.setObjectName("round")
        self.gridLayout.addWidget(self.round, 6, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.rock.pressed.connect(lambda: self.result("rock"))
        self.scissers.pressed.connect(lambda: self.result("scissers"))
        self.paper.pressed.connect(lambda: self.result("paper"))
        self.resetBot.pressed.connect(self.reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rock.setText(_translate("MainWindow", "Rock"))
        self.paper.setText(_translate("MainWindow", "paper"))
        self.scissers.setText(_translate("MainWindow", "scissers"))
        self.pcLabel.setText(_translate("MainWindow", "computer"))
        self.plLabel.setText(_translate("MainWindow", "player"))
        self.resetBot.setText(_translate("MainWindow", "Reset"))
        self.pcChoice.setText(_translate("MainWindow", "computr choice"))
        self.round.setText(_translate("MainWindow", "round"))


    def pcChoiceMk(self):
        rsp = ["rock","scissers","paper"]
        shuffle(rsp)
        pc = choice(rsp)
        return pc

    def reset(self):
        global playerScore,pcScore,gameRound
        playerScore = 0
        pcScore = 0
        gameRound = 0
        self.roundLcd.display(gameRound)
        self.plWinLcd.display(playerScore)
        self.pcWinLcd.display(pcScore)
        self.pcChoiceOut.clear()

    def result(self,player):
        global playerScore,pcScore,gameRound
        pcMove = self.pcChoiceMk()
        if player[0] == pcMove[0]:
            self.pcChoiceOut.clear()
            self.pcChoiceOut.setText(pcMove)
        elif player[0] == "r" and pcMove[0] == "s":
            self.pcChoiceOut.clear()
            self.pcChoiceOut.setText(pcMove)
            playerScore += 1
            self.plWinLcd.display(playerScore)
        elif player[0] == "r" and pcMove[0] == "p":
            self.pcChoiceOut.clear()
            self.pcChoiceOut.setText(pcMove)
            pcScore += 1
            self.pcWinLcd.display(pcScore)
        elif player[0] == "s" and pcMove[0] == "r":
            self.pcChoiceOut.clear()
            self.pcChoiceOut.setText(pcMove)
            pcScore += 1
            self.pcWinLcd.display(pcScore)
        elif player[0] == "s" and pcMove[0] == "p":
            self.pcChoiceOut.clear()
            self.pcChoiceOut.setText(pcMove)
            playerScore += 1
            self.plWinLcd.display(playerScore)
        elif player[0] == "p" and pcMove[0] == "r":
            self.pcChoiceOut.clear()
            self.pcChoiceOut.setText(pcMove)
            playerScore += 1
            self.plWinLcd.display(playerScore)
        elif player[0] == "p" and pcMove[0] == "s":
            self.pcChoiceOut.clear()
            self.pcChoiceOut.setText(pcMove)
            pcScore += 1
            self.pcWinLcd.display(pcScore)
        gameRound += 1
        self.roundLcd.display(gameRound)

playerScore = 0
pcScore = 0
gameRound = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
