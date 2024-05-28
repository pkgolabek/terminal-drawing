class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_ascii_box(self):
        top_border = "-" * self.width
        bottom_border = "_" * self.width

        middle_part = "|" + " " * (self.width - 2) + "|"

        box = [top_border]
        for _ in range(self.height - 2):
            box.append(middle_part)
        box.append(bottom_border)
        box.append("\n")

        return "\n".join(box)

class CommandPrompt:
    def __init__(self, position, width, height, command):
        self.position = position
        self.width = width
        self.height = height
        self.command = command
    
    def render_command(self):
        box = self.empty_box(self.width, self.height)
        if self.position == "top-left":
            box[0] = self.command
        if self.position == "top-right":
            box[0] = box[0][:len(box) - len(self.command)] + self.command
        if self.position == "bottom-left":
            box[-1] = self.command
        if self.position == "bottom-right":
            box[-1] = box[-1][:len(box) - len(self.command)] + self.command
        return "\n".join(box)

    def empty_box(self, width, height):
        box = []
        for _ in range(height):
            box.append(" " * width)
        return box

if __name__ == "__main__":
    canvas = Canvas(10, 10)
    print(canvas.generate_ascii_box())
    prompt = CommandPrompt("bottom-left", 30, 30, "Your command here:")
    print(prompt.render_command())