import curses

from commands import list_directory

def execute_command(stdscr, command, *args):
    stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    try:
        if command == "list":
            if len(args) != 1:
                raise ValueError("Invalid number of arguments for 'list' command. Expected 1 argument (directory path).")
            contents = list_directory(args[0])
            stdscr.clear()
            stdscr.addstr(f"Contents of directory '{args[0]}':\n", curses.color_pair(1))
            for item in contents:
                stdscr.addstr(f"{item}\n")
            stdscr.refresh()
        else:
            stdscr.addstr(f"Unknown command '{command}'\n", curses.color_pair(2))
            stdscr.refresh()
    except ValueError as ve:
        stdscr.addstr(f"ValueError: {str(ve)}\n", curses.color_pair(2))
        stdscr.refresh()
    except Exception as e:
        stdscr.addstr(f"Error: {str(e)}\n", curses.color_pair(2))
        stdscr.refresh()