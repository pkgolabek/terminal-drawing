from ui.ui import Canvas
from ui.ui import CommandPrompt
from ui.screen import Screen

class Session:
    def __init__(self):
        self.screen = None
        self.canvas = None
        self.width = None
        self.height = None

    def start(self):
        self.screen = Screen().start()
        prompt = CommandPrompt("bottom-left", self.screen.width, self.screen.height, "Pick your Canvas size (max {self.screen.width} {self.screen.height}):".format(self=self))
        self.screen.add_to_ui_buffer(0, 0, prompt.render_command()).render()
        self.width, self.height = self.screen.get_input().split(" ")
    def run():
        pass
        
if __name__ == "__main__":
    session = Session()
    session.start()