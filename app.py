from tkinter import *
# from tkmacosx import Button
from tkinter import Frame
from tkinter import filedialog, messagebox
import os
from tkinter.font import BOLD

DEFAULT_BGCOLOR = "white"
TEMP_DIR = os.path.join(os.getcwd(),'table')

GRID_MAX_COL = 7

CHECKBOX_INDEX = {'채언':1, '조사':2}

class MainWindow(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title('Unziper')
        self.pack(fill=BOTH, expand=1)
        self.configure(bg=DEFAULT_BGCOLOR)
        self.centerWindow()

        self.title = Label(self, text='형태소 분석기', font=("Helvetica 18 bold"), background=DEFAULT_BGCOLOR, pady=20)
        self.title.grid(row=0, column=0, columnspan=2)

        self.textField = Text(self, width=70, height=50)
        self.textField.grid(row = 1, column=0)

        checkBoxFrame = Frame(self, background=DEFAULT_BGCOLOR, highlightbackground=DEFAULT_BGCOLOR)
        self.cheUnLabel = Label(checkBoxFrame, text="채언", background=DEFAULT_BGCOLOR)
        self.cheUnLabel.grid(row = 1, column=2,  sticky  ="w")
        self.cheUnCheck_var = BooleanVar()
        self.cheUnCheck_var.set(False)
        cheUnCheck = Checkbutton(checkBoxFrame, variable=self.cheUnCheck_var, highlightbackground=DEFAULT_BGCOLOR, background=DEFAULT_BGCOLOR)
        cheUnCheck.grid(row = 1, column=1, sticky="e")

        checkBoxFrame.grid(row=1, column=1)

        self.place(x = 40, y = 20)

    def centerWindow(self):

        w = 1200
        h = 800

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.master.geometry('%dx%d+%d+%d' % (w,h,x,y))

    def openDlg(self):
        print("click openDlg")

        filename = filedialog.askdirectory(initialdir=os.getcwd(), title="Select directory")

        self.dirPath.set(filename)
    

def main():
    root = Tk()
    root.resizable(False, False)
    root.configure(bg=DEFAULT_BGCOLOR)
    ex = MainWindow()
    root.mainloop()


if __name__=='__main__':
    main()


# root = Tk()
# root.title('Unziper')
# root.geometry('300x300+100+100')
# root.mainloop()
