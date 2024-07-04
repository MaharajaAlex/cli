import os
import customtkinter as ctk
from commands import list_directory, cd, mkdir, rmdir, signout, shutdown, echo, cls, ipconfig, ping_func, help

class TerminalApp(ctk.CTk):
    """A custom CLI application using customtkinter."""

    def __init__(self):
        """Initialize the CLI application."""
        super().__init__()
        self.title("CLI")
        self.geometry("800x600")
        self.current_directory = os.getcwd()
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create and pack the widgets for the application."""
        self.output_textbox = ctk.CTkTextbox(self, wrap=ctk.WORD)
        self.output_textbox.pack(padx=20, pady=20, fill="both", expand=True)

        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(padx=20, pady=10, fill="x")

        self.command_label = ctk.CTkLabel(self.input_frame, text=f"{self.current_directory}>")
        self.command_label.pack(side=ctk.LEFT)

        self.command_entry = ctk.CTkEntry(self.input_frame, width=600)
        self.command_entry.pack(side=ctk.LEFT, padx=10, fill="x", expand=True)
        self.command_entry.bind("<Return>", self.execute_command)

    def execute_command(self, event=None) -> None:
        """Execute the command entered by the user."""
        command = self.command_entry.get()
        self.command_entry.delete(0, ctk.END)
        self.output_textbox.insert(ctk.END, f"{self.current_directory}> {command}\n")
        
        try:
            if command.startswith('list'):
                self.handle_list(command)
            elif command.startswith('cd'):
                self.handle_cd(command)
            elif command.startswith('mkdir'):
                self.handle_mkdir(command)
            elif command.startswith('rmdir'):
                self.handle_rmdir(command)
            elif command.startswith('signout'):
                self.handle_signout()
            elif command.startswith('shutdown'):
                self.handle_shutdown()
            elif command.startswith('echo'):
                self.handle_echo(command)
            elif command.startswith('cls'):
                self.handle_cls()
            elif command.startswith('exit'):
                self.handle_exit()
            elif command.startswith('ipconfig'):
                self.handle_ipconfig()
            elif command.startswith('ping'):
                self.handle_ping(command)
            elif command.startswith('help'):
                self.handle_help(r'C:\Users\chirbhat.ORADEV\Desktop\Python\cli\src\help.txt')
            else:
                self.output_textbox.insert(ctk.END, f"\nUnknown command: {command}\n")
        except Exception as e:
            self.output_textbox.insert(ctk.END, f"Error: {e}\n")
        
        self.output_textbox.see(ctk.END)

    def handle_list(self, command: str) -> None:
        """Handle the 'list' command."""
        _, path = command.split(' ', 1)
        contents = list_directory(path)
        for item in contents:
            self.output_textbox.insert(ctk.END, item + '\n')

    def handle_cd(self, command: str) -> None:
        """Handle the 'cd' command."""
        _, path = command.split(' ', 1)
        cd(path)
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")

    def handle_mkdir(self, command: str) -> None:
        """Handle the 'mkdir' command."""
        _, path = command.split(' ', 1)
        mkdir(path)
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")

    def handle_rmdir(self, command: str) -> None:
        """Handle the 'rmdir' command."""
        _, path = command.split(' ', 1)
        rmdir(path)
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")

    def handle_signout(self) -> None:
        """Handle the 'signout' command."""
        signout()
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")

    def handle_shutdown(self) -> None:
        """Handle the 'shutdown' command."""
        shutdown()
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")

    def handle_echo(self, command: str) -> None:
        """Handle the 'echo' command."""
        _, text = command.split(' ', 1)
        echo(text)
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")
        self.output_textbox.insert(ctk.END, text + "\n")

    def handle_cls(self) -> None:
        """Handle the 'cls' command."""
        cls()
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")
        self.output_textbox.delete("0.0", ctk.END)

    def handle_exit(self) -> None:
        """Handle the 'exit' command."""
        self.destroy()
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")
        self.output_textbox.delete("0.0", ctk.END)

    def handle_ipconfig(self) -> None:
        """Handle the 'ipconfig' command."""
        stuff = ipconfig()
        if stuff:
            self.output_textbox.delete("0.0", ctk.END)
        for text in stuff:
            self.output_textbox.insert(ctk.END, f"{text}\n")
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")

    def handle_ping(self, command: str) -> None:
        """Handle the 'ping' command."""
        try:
            _, host = command.split(' ', 1)
            response = ping_func(host)
            self.output_textbox.insert(ctk.END, response)
        except ValueError:
            self.output_textbox.insert(ctk.END, "No host provided.\n")
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")

    def handle_help(self, filepath: str) -> None:
        """Handle the 'help' command."""
        help_command = help(filepath)
        self.current_directory = os.getcwd()
        self.command_label.configure(text=f"{self.current_directory}>")
        self.output_textbox.insert(ctk.END, help_command)
