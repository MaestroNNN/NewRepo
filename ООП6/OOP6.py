import tkinter as tk
import threading
import random
import time

class MovingObject:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.x = random.randint(10, 390)
        self.y = random.randint(10, 390)
        self.radius = 20
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    def move(self):
        while True:
            self.canvas.move(self.shape, self.dx, self.dy)
            self.canvas.update()
            x1, y1, x2, y2 = self.canvas.coords(self.shape)
            if x1 <= 0 or x2 >= 400:
                self.dx *= -1
            if y1 <= 0 or y2 >= 400:
                self.dy *= -1
            time.sleep(0.01)

def create_moving_object(canvas, color):
    obj = MovingObject(canvas, color)
    obj.shape = canvas.create_oval(
        obj.x - obj.radius, obj.y - obj.radius,
        obj.x + obj.radius, obj.y + obj.radius,
        fill=color
    )
    thread = threading.Thread(target=obj.move)
    thread.daemon = True
    thread.start()

def main():
    root = tk.Tk()
    root.title("Движущиеся объекты")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    colors = ['red', 'green', 'blue']

    for color in colors:
        create_moving_object(canvas, color)

    root.mainloop()

if __name__ == "__main__":
    main()