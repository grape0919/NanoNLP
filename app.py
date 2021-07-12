from tkinter import *
# from tkmacosx import Button
from tkinter import Frame
from tkinter import filedialog, messagebox
from tkinter import font
from tkinter.ttk import Progressbar

import os
from tkinter.font import BOLD, families

import time
from mainProcess import MainProcess
import fileWriter.report as Reporter
import threading

from nlp.data.morph import Morph

DEFAULT_BGCOLOR = "white"
DEFAULT_BUTTON_COLOR = "ghost white"
POINT_BUTTON_COLOR = "#0f4c81"

TEMP_DIR = os.path.join(os.getcwd(), 'temp')

GRID_MAX_ROW = 4
GRID_MAX_COL = 2

CHECKBOX_INDEX = Morph.CHECKBOX_INDEX

CHECKBOX_CORDINATE = [(0, 0), (0, 2), (0, 4),
                      (1, 0), (1, 2),
                      (2, 0), (2, 3),
                      (3, 4),
                      (4, 5),
                      (5, 6),
                      (6, 6),
                      (7, 0), (7, 2), (7, 4)]  # row, col

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 760

TITLE = "국어교육용 형태소 분석기 1.0v"

class MainWindow(Frame):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.initUI()
        self.nlp = MainProcess()

    def initUI(self):
        self.master.title(TITLE)
        self.pack(fill=BOTH, expand=1)
        self.configure(bg=DEFAULT_BGCOLOR)
        self.centerWindow(self.master, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.title = Label(self, text=TITLE, background=DEFAULT_BGCOLOR, font=font.Font(size=20))
        self.title.grid(row=0, column=0, columnspan=GRID_MAX_COL, sticky="n")

        ## 텍스트 필드
        textFieldFrame = Frame(self, background=DEFAULT_BGCOLOR,
                              highlightbackground=DEFAULT_BGCOLOR, pady=20)
        textFieldScrollbar = Scrollbar(textFieldFrame)
        textFieldScrollbar.grid(row=0, column=1, sticky="sn")

        self.textField = Text(textFieldFrame, width=70, height=50, yscrollcommand=textFieldScrollbar.set)
        textFieldScrollbar.config(command=self.textField.yview)
        self.textField.grid(row=0, column=0)

        textFieldFrame.grid(row=1, column=0, rowspan=GRID_MAX_ROW-1)
        
        ## 체크박스UI
        self.optionCheck_var = [None]*len(CHECKBOX_INDEX)

        checkBoxFrame = Frame(self, padx=40, background=DEFAULT_BGCOLOR,
                              highlightbackground=DEFAULT_BGCOLOR)
        for i in range(len(CHECKBOX_INDEX)):
            self.optionCheck_var[i] = BooleanVar()
            self.optionCheck_var[i].set(False)
            if i == 6:
                Button(checkBoxFrame, text=CHECKBOX_INDEX[i], command=self.checkTail)\
                        .grid(row=CHECKBOX_CORDINATE[i][0], column=CHECKBOX_CORDINATE[i][1])
            elif i == 8:
                Button(checkBoxFrame, text=CHECKBOX_INDEX[i], command=self.checkTailSub)\
                        .grid(row=CHECKBOX_CORDINATE[i][0], column=CHECKBOX_CORDINATE[i][1])
            else:
                Checkbutton(checkBoxFrame, variable=self.optionCheck_var[i],
                                            highlightbackground=DEFAULT_BGCOLOR, background=DEFAULT_BGCOLOR).grid(row=CHECKBOX_CORDINATE[i][0],
                                    column=CHECKBOX_CORDINATE[i][1], sticky="e")

                Label(checkBoxFrame, text=CHECKBOX_INDEX[i],
                                    background=DEFAULT_BGCOLOR).grid(row=CHECKBOX_CORDINATE[i][0],
                                    column=CHECKBOX_CORDINATE[i][1]+1, sticky="w")

        Label(checkBoxFrame, text='└──',
                                    background=DEFAULT_BGCOLOR).grid(row=3,
                                    column=3, sticky="w")
        Label(checkBoxFrame, text='└──',
                                    background=DEFAULT_BGCOLOR).grid(row=5,
                                    column=5, sticky="w")

        checkBoxFrame.grid(row=1, column=1)

        checkAllBtnFrame = Frame(self, padx=40, background=DEFAULT_BGCOLOR,
                            highlightbackground=DEFAULT_BGCOLOR)
        self.checkAllBtnText = StringVar()
        self.checkAllBtnText.set("전체 선택")
        checkAllBtn = Button(checkAllBtnFrame, textvariable=self.checkAllBtnText, command=self.checkAll)
        checkAllBtn.grid(row=0, column=0)
        checkAllBtnFrame.grid(row=2, column=1, sticky="wn")

        processFrame = Frame(self, background=DEFAULT_BGCOLOR,
                            highlightbackground=DEFAULT_BGCOLOR)
        runBtn = Button(processFrame, text="실행", command=self.runProcess, width=10, 
                             background=POINT_BUTTON_COLOR, fg=DEFAULT_BGCOLOR, highlightbackground=DEFAULT_BGCOLOR)
        runBtn.grid(row = 0, column=0)

        processFrame.grid(row = 3, column=1, sticky="n")

        canvas = Canvas(self)
        canvas.create_line(150, 20, 170, 20)


        self.place(x=40, y=20)

    def centerWindow(self, view, w, h):

        sw = view.winfo_screenwidth()
        sh = view.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        view.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def openDlg(self):
        print("click openDlg")

        filename = filedialog.askdirectory(
            initialdir=os.getcwd(), title="Select directory")

        self.dirPath.set(filename)


    def runProcess(self):
        self.master.grab_set()
        popup = Toplevel(self.root)
        popup.overrideredirect(1)
        self.root.eval(f'tk::PlaceWindow {str(popup)} center')
        # print(self.textField.get("1.0", "end"))

        Label(popup, text="형태소 분석중...", width=50, height=2).grid(row=0,column=0)
        progress_bar = Progressbar(popup, orient='horizontal', mode='indeterminate', length=300)
        progress_bar.grid(row=1, column=0)#.pack(fill=tk.X, expand=1, side=tk.BOTTOM)
        progress_bar.start()
        th = threading.Thread(target=self.nlp.analyze, args=(self.textField.get("1.0", "end"),))
        th.start()
        while self.nlp.is_running:
            popup.update()
        progress_bar.stop()
        # popup.pack_slaves()
        popup.destroy()
        messagebox.showinfo("메세지", "분석이 완료되었습니다.")

        wb = Reporter.write_report(self.nlp.inputData, self.optionCheck_var)

        filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save file",
                                          filetypes=(("Excel files", "*.xlsx"),("all files", "*.*")), defaultextension=".xlsx")
        if filename:
            wb.save(filename)

    def checkAll(self):
        if self.checkAllBtnText.get() == "전체 선택":
            self.checkAllBtnText.set("전체 해제")
            for i in range(len(CHECKBOX_INDEX)):
                if i == 6 or i == 8:
                    continue
                self.optionCheck_var[i].set(True)
        else:
            self.checkAllBtnText.set("전체 선택")
            for i in range(len(CHECKBOX_INDEX)):
                self.optionCheck_var[i].set(False)

    def checkTail(self):
        if self.optionCheck_var[7].get() and self.optionCheck_var[9].get() and self.optionCheck_var[10].get():
            self.optionCheck_var[7].set(False)
            self.optionCheck_var[9].set(False)
            self.optionCheck_var[10].set(False)
        else:
            self.optionCheck_var[7].set(True)
            self.optionCheck_var[9].set(True)
            self.optionCheck_var[10].set(True)

    def checkTailSub(self):
        if self.optionCheck_var[9].get() and self.optionCheck_var[10].get():
            self.optionCheck_var[9].set(False)
            self.optionCheck_var[10].set(False)
        else:
            self.optionCheck_var[9].set(True)
            self.optionCheck_var[10].set(True)
        

def main():
    root = Tk()
    root.resizable(False, False)
    root.configure(bg=DEFAULT_BGCOLOR)
    ex = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()


# root = Tk()
# root.title('Unziper')
# root.geometry('300x300+100+100')
# root.mainloop()
