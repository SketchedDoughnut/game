# This code is taken and modified from loads.py, which is used in conways game of life to load maps
#########################################################################################################
# loading 
import os
# import json
import time
import requests
import tkinter

TEXT_DATA = [
    """Welcome to the Python Helper! This guide will help you through the process of installing Python. Click "Continue" to get started.""",
    """This project requires an installation of Python. It was specifically made on Python 3.11.""",
    """To check if you have Python installed, open command prompt and enter "python --version". You should get a version number back. This project can not guarantee proper functionality on versions other then Python 3.11.""",
    """If you have Python installed, click "Yes, I have Python" below. Otherwise, click "No, I do not have Python" below."""
]

class Python_helper:
    def __init__(self):
        # unrelated jazz
        self.wDir = os.path.dirname(os.path.abspath(__file__))

        # tkinter stuff
        self.window = tkinter.Tk(className="window~!")
        self.window.geometry('500x480')
        self.text = tkinter.StringVar()
        # self.text = tkinter.Text(wrap=tkinter.WORD)
        self.button_text = tkinter.StringVar()
        self.element_list = []
        self.phase = 0
        self.manual_set = False
        self.manual_phase = 0

        # CUSTOM VARIABLES
        self.has_python_installed = False
        self.run_install = False
        self.microsoft_install = False

    def reset_element_list(self):
        self.element_list = []

    def clear_screen(self):
        for element in self.window.winfo_children():
            element.destroy()

    def submit_elements(self, new_elements: list):
        self.element_list.extend(new_elements)

    def set_phase(self, prep_num: int):
        self.manual_set = True
        self.manual_phase = prep_num

    def extender(self):
        if self.manual_set == True:
            self.phase = self.manual_phase
        else:
            self.phase += 1
        # self.clear_screen()
        self.reset_element_list()
        self.main()

    def reverser(self):
        if self.manual_set == True:
            self.phase = self.manual_phase
        else:
            self.phase -= 1
        # self.clear_screen()
        self.reset_element_list()
        self.main()

    def end(self):
        self.window.destroy()
        self.main('return')

    def pack_elements(self):
        for element in self.element_list:
            element.pack()

    def phase_setter(self, text: str = 'default', button_text: str = 'default'):
        self.text.set(text)
        self.button_text.set(button_text)

    def main(self, mode: str = 'op'):
        # return data
        if mode != 'op':
            return # any returns go here

        # introductions
        if self.phase == 0:
            self.clear_screen()
            self.reset_element_list()
            self.phase_setter(
                button_text="Continue"
            )
            label = self.label_wrapped(text_data=TEXT_DATA[0])
            self.submit_elements(
                [
                    label,
                    tkinter.Button(self.window, textvariable=self.button_text, command=self.extender)
                ]
            )
            self.pack_elements()
            self.window.mainloop()

        elif self.phase == 1:
            self.clear_screen()
            self.reset_element_list()
            label1 = self.label_wrapped(text_data=TEXT_DATA[2])
            label2 = self.label_wrapped(text_data=TEXT_DATA[3])
            self.submit_elements(
                [
                    label1,
                    label2
                ]
            )
            self.pack_elements()
            





    # CUSTOM FUNCTIONS
    def label_wrapped(self, text_data: str = 'autofill', justifyer: str = 'center', wraplengther = 490, padding_x = 10, padding_y = 10) -> tkinter.Label:
        # justify can be center, left, or right
        if text_data == 'autofill':
            text_data = self.text
        text_obj = tkinter.StringVar()
        text_obj.set(text_data)
        return tkinter.Label(self.window, textvariable=text_obj, justify=justifyer, wraplength=wraplengther, padx = padding_x, pady=padding_y)

    def run_installer(self):
        installer_data = requests.get('https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe')
        if installer_data.status_code == 200:
            tmp_path = self.wDir + '/tmp'
            try:
                os.mkdir(tmp_path)
            except:
                pass
            exec_path = tmp_path + '/python-3.11.9-amd64.exe'
            f = open(exec_path, 'wb')
            f.write(installer_data.content)
            f.close()
            os.system(exec_path)

Python_helper().main()