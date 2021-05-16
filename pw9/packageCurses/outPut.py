import curses

def output():
    print("preparing to initialize screen...")
    screen = output.initscr()
    print("Screen initialized.")
    screen.refresh()
    output.napms(2000)
    output.endwin()
    print("window ended.")
    return null
outPut()
