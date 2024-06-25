import os

import curses

from utils import execute_command 

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    stdscr.clear()

    # Display current path
    current_path = os.getcwd()
    stdscr.addstr(f"{current_path}> ", curses.color_pair(1))
    stdscr.refresh()

    # Input handling
    curses.echo()
    command_input = stdscr.getstr().decode('utf-8')
    curses.noecho()

    # Parse command and arguments
    parts = command_input.split(maxsplit=1)
    command = parts[0]
    args = parts[1].split() if len(parts) > 1 else []

    # Execute command
    execute_command(stdscr, command, *args)

    # Wait for user input to exit
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
