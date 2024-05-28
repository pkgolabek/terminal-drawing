import curses

class Screen:
    def __init__(self):
        self.screen = None
        self.height = None
        self.width = None
        self.input_buffer = ""

    def start(self):
        curses.wrapper(self._main)
        return self

    def _main(self, stdscr):
        self.screen = stdscr
        curses.curs_set(0)
        self.screen.clear()
        self.height, self.width = self.screen.getmaxyx()
        curses.echo()
        
    def clear(self):
        self.screen.clear()
        return self
    
    def add_to_ui_buffer(self, y, x, string):
        for line in string.split('\n'):
            self.screen.addstr(y, x, line)
            y += 1
        return self

    def render(self):
        self.screen.refresh()
        return self
    
    def wait_for_input(self):
        self.screen.getch()
        return self

    def get_input(self):
        return self.screen.getstr().decode("utf-8")

if __name__ == "__main__":
    tr = Screen()
    tr.start().add_to_ui_buffer(10, 10, "Hello, world!\nit's me").render().wait_for_input().clear()
