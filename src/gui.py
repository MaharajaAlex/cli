import subprocess
import customtkinter as ctk
from re import findall
from subprocess import Popen, PIPE
from pythonping import ping
import os
from commands import list_directory, cd, mkdir, rmdir, signout, shutdown, echo, cls

class TerminalApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CLI")
        self.geometry("800x600")

        self.current_directory = os.getcwd()

        self.output_textbox = ctk.CTkTextbox(self, wrap=ctk.WORD)
        self.output_textbox.pack(padx=20, pady=20, fill="both", expand=True)

        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(padx=20, pady=10, fill="x")

        self.command_label = ctk.CTkLabel(self.input_frame, text=f"{self.current_directory}>")
        self.command_label.pack(side=ctk.LEFT)

        self.command_entry = ctk.CTkEntry(self.input_frame, width=600)
        self.command_entry.pack(side=ctk.LEFT, padx=10, fill="x", expand=True)
        self.command_entry.bind("<Return>", self.execute_command)

    def execute_command(self, event=None):
        command = self.command_entry.get()
        self.command_entry.delete(0, ctk.END)
        self.output_textbox.insert(ctk.END, f"{self.current_directory}> {command}\n")
        
        #list   
        if command.startswith('list'):
            _, path = command.split(' ', 1)
            try:
                contents = list_directory(path)
                for item in contents:
                    self.output_textbox.insert(ctk.END, item + '\n')
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #cd
        elif command.startswith('cd'):
            _, path = command.split(' ', 1)
            try:
                cd(path)
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #mkdir
        elif command.startswith('mkdir'):
            _, path = command.split(' ', 1)
            try:
                mkdir(path)
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #rmdir
        elif command.startswith('rmdir'):
            _, path = command.split(' ', 1)
            try:
                rmdir(path)
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #signout
        elif command.startswith('signout'): 
            try:
                signout()
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")
        
        #shutdown
        elif command.startswith('shutdown'): 
            try:
                shutdown()
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #echo
        elif command.startswith('echo'):
            _, text = command.split(' ', 1)
            try:
                echo(text)
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
                self.output_textbox.insert(ctk.END, text + "\n")
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #cls
        elif command.startswith('cls'):
            try:
                cls()
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
                self.output_textbox.delete("0.0", ctk.END)
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #exit
        elif command.startswith('exit'):
            try:
                self.destroy()
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
                self.output_textbox.delete("0.0", ctk.END)
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")

        #ipconfig
        elif command.startswith('ipconfig'):
            try:
                data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8').split('\n')
                for item in data:
                    self.output_textbox.insert(ctk.END, item.split('\r')[:-1])
            except PermissionError:
                print(f"Permission Denied")
            except OSError as e:
                print(f"Error: {e}")
        
        #ping
        elif command.startswith('ping'):
            _, host = command.split(' ', 1) 
            ping_count = 4
            try:
                ping_res = ping(host, verbose=True)
                self.output_textbox.insert(ctk.END, ping_res)
                self.current_directory = os.getcwd()
                self.command_label.configure(text=f"{self.current_directory}>")
            except Exception as e:
                self.output_textbox.insert(ctk.END, f"Error: {e}\n")
        else:
            self.output_textbox.insert(ctk.END, f"\nUnknown command: {command}\n")  

        self.output_textbox.see(ctk.END)

