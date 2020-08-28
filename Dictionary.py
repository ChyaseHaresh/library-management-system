import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import json
from difflib import get_close_matches



data=json.load(open("data.json"))



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dictionary by @hareshchyase")
        self.setWindowIcon(QIcon("dictionary.ico"))
        self.setGeometry(400, 200, 500, 350)
        self.UI()
        self.show()

    def UI(self):
        self.design()
        self.layouts()


    def design(self):
        self.titleText= QLabel("Word")
        self.textArea= QLineEdit()
        self.textArea.setPlaceholderText("Enter the word")
        self.btn= QPushButton("Search")
        self.btn.clicked.connect(self.return_meaning_clicked)
        self.means= QLabel("Meanings")
        self.meaningList= QListWidget()
        #self.meaningList.setMinimumWidth(self.meaningList.sizeHintForColumn(0))

        # self.meaningList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.meaningList.setFixedSize(self.meaningList.sizeHintForColumn(0) + 2 * self.meaningList.frameWidth(),
        #                   self.meaningList.sizeHintForRow(0) * self.meaningList.count() + 2 * self.meaningList.frameWidth())

    def layouts(self):
        self.mainLayout= QVBoxLayout()
        self.topLayout= QHBoxLayout()
        self.bottomLayout= QVBoxLayout()
        self.groupbocx= QGroupBox("Search")

        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.textArea)
        self.topLayout.addWidget(self.btn)
        self.bottomLayout.addWidget(self.means)
        self.bottomLayout.addWidget(self.meaningList)

        self.groupbocx.setLayout(self.topLayout)
        self.mainLayout.addWidget(self.groupbocx)
        self.mainLayout.addLayout(self.bottomLayout)


        self.setLayout(self.mainLayout)


    def return_meaning_clicked(self):
        self.meaningList.clear()

        word= self.textArea.text()
        word.lower()
        output=self.return_meaning(word)
        #self.textArea.setText(self.sub)

        if type(output) == list:
            for item in output:
                self.meaningList.addItem(item)

        else:
            self.meaningList.addItem(output)

    def return_meaning(self, sabda):
        sabda = sabda.lower()
        if sabda in data:
            return (data[sabda])

        elif len(get_close_matches(sabda, data.keys())) > 0:
            mbox = QMessageBox.question(self, "Warning !!!", "\nDid you mean %s instead ??" % get_close_matches(sabda, data.keys())[0],
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            # yn = input("\nDid you mean %s instead ?? Y for yes n for no: " % get_close_matches(sabda, data.keys())[0])
            # yn = yn.lower()
            if mbox == QMessageBox.Yes:
                self.sub= get_close_matches(sabda, data.keys())[0]
                self.textArea.setText(self.sub)
                return (data[get_close_matches(sabda, data.keys())[0]])
            elif mbox == QMessageBox.No:
                QMessageBox.information(self, "Information", 'Please make sure you type the word correctly')
            else:
                QMessageBox.information(self, "Information", 'What the heck is this ??')

        else:
            QMessageBox.information(self, "Information", sabda + ' doesnt exist')



def main():
    App= QApplication(sys.argv)
    win= Window()
    sys.exit(App.exec_())

if __name__== '__main__':
    main()
