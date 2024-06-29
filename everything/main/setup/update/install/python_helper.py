# This code is taken and modified from loads.py, which is used in conways game of life to load maps
#########################################################################################################
# loading 
import os
# import json
import time
import requests
import tkinter

class Python_helper:
    def __init__(self):
        # unrelated jazz
        self.wDir = os.path.dirname(os.path.abspath(__file__))

        # tkinter stuff
        self.window = tkinter.Tk(className="window~!")
        self.text = tkinter.StringVar()
        self.button_text = tkinter.StringVar()
        self.element_list = []
        self.phase = 0
        self.manual_set = False
        self.manual_phase = 0

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
        if self.manual_phase == True:
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

    def phase_setter(self, text: str, button_text: str):
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
                text=f"Welcome to the Python helper!",
                button_text="Continue"
            )
            self.submit_elements(
                [
                    tkinter.Label(self.window, textvariable=self.text),
                    tkinter.Button(self.window, textvariable=self.button_text, command=self.extender)
                ]
            )
            self.pack_elements()
            self.window.mainloop()

    # CUSTOM FUNCTIONS
    def download(self):
        installer_data = requests.get('https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe')
        if installer_data.status_code == '200':
            tmp_path = self.wDir + '/tmp'
            try:
                os.mkdir(tmp_path)
            except:
                pass
            exec_path = tmp_path + 'python-3.11.9-amd64.exe'
            f = open(exec_path, 'wb')
            f.write(installer_data.content)
            f.close()
            os.system(exec_path)