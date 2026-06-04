import tkinter as tk
import random

# ==========================
# Configuration
# ==========================
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

BACKGROUND_COLOR = "#111111"
SNAKE_COLOR = "#00ff66"
FOOD_COLOR = "#ff3333"
TEXT_COLOR = "#ffffff"

INITIAL_SPEED = 120


# ==========================
# Snake Class
# ==========================
class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = "Right"

    def move(self):
        x, y = self.body[0]

        if self.direction == "Up":
            y -= CELL_SIZE
        elif self.direction == "Down":
            y += CELL_SIZE
        elif self.direction == "Left":
            x -= CELL_SIZE
        elif self.direction == "Right":
            x += CELL_SIZE

        new_head = (x, y)

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def get_head(self):
        return self.body[0]

    def change_direction(self, new_direction):
        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        if opposite[self.direction] != new_direction:
            self.direction = new_direction


# ==========================
# Food Class
# ==========================
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE

            if (x, y) not in snake_body:
                return (x, y)


# ==========================
# Game Class
# ==========================
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.score = 0
        self.speed = INITIAL_SPEED

        self.canvas = tk.Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg=BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.canvas.pack()

        self.score_label = tk.Label(
            root,
            text="Score: 0",
            font=("Arial", 16, "bold")
        )
        self.score_label.pack()

        self.snake = Snake()
        self.food = Food(self.snake.body)

        self.root.bind("<Key>", self.on_key_press)

        self.running = True

        self.draw()
        self.game_loop()

    # ------------------
    # Drawing
    # ------------------
    def draw(self):
        self.canvas.delete("all")

        # Draw Snake
        for x, y in self.snake.body:
            self.canvas.create_rectangle(
                x,
                y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill=SNAKE_COLOR,
                outline=""
            )

        # Draw Food
        fx, fy = self.food.position

        self.canvas.create_oval(
            fx,
            fy,
            fx + CELL_SIZE,
            fy + CELL_SIZE,
            fill=FOOD_COLOR,
            outline=""
        )

    # ------------------
    # Input Handling
    # ------------------
    def on_key_press(self, event):
        key = event.keysym

        mapping = {
            "Up": "Up",
            "Down": "Down",
            "Left": "Left",
            "Right": "Right",
            "w": "Up",
            "s": "Down",
            "a": "Left",
            "d": "Right"
        }

        if key in mapping:
            self.snake.change_direction(mapping[key])

    # ------------------
    # Collision Checks
    # ------------------
    def wall_collision(self):
        x, y = self.snake.get_head()

        return (
            x < 0 or
            x >= WIDTH or
            y < 0 or
            y >= HEIGHT
        )

    def self_collision(self):
        head = self.snake.get_head()

        return head in self.snake.body[1:]

    # ------------------
    # Food Handling
    # ------------------
    def check_food(self):
        if self.snake.get_head() == self.food.position:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

            self.snake.grow()
            self.food = Food(self.snake.body)

    # ------------------
    # Game Over
    # ------------------
    def game_over(self):
        self.running = False

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 - 20,
            text="GAME OVER",
            fill="red",
            font=("Arial", 32, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + 30,
            text="Press R to Restart",
            fill="white",
            font=("Arial", 18)
        )

        self.root.bind("r", self.restart)
        self.root.bind("R", self.restart)

    def restart(self, event=None):
        self.score = 0
        self.score_label.config(text="Score: 0")

        self.snake = Snake()
        self.food = Food(self.snake.body)

        self.running = True

        self.root.bind("<Key>", self.on_key_press)

        self.draw()
        self.game_loop()

    # ------------------
    # Main Loop
    # ------------------
    def game_loop(self):
        if not self.running:
            return

        self.snake.move()

        if self.wall_collision() or self.self_collision():
            self.game_over()
            return

        self.check_food()
        self.draw()

        self.root.after(self.speed, self.game_loop)


# ==========================
# Main
# ==========================
if __name__ == "__main__":
    root = tk.Tk()

    game = SnakeGame(root)

    root.mainloop()