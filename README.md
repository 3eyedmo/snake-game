# 🐍 Snake Game - Python Tkinter

A modern implementation of the classic Snake Game built with Python and Tkinter.

The game features smooth controls, score tracking, food spawning, collision detection, and a clean object-oriented architecture, making it both fun to play and easy to extend.

---

## 📸 Preview

![Snake Game Screenshot](screenshot.png)

---

## ✨ Features

* Classic Snake gameplay
* Smooth keyboard controls
* Score tracking
* Random food generation
* Wall collision detection
* Self-collision detection
* Game Over screen
* Restart functionality
* Object-Oriented Design (OOP)
* Easy to customize and extend

---

## 🛠 Requirements

* Python 3.8+
* Tkinter (usually included with Python)

Verify Tkinter installation:

```bash
python -m tkinter
```

If a small window opens, Tkinter is installed correctly.

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/snake-game.git
cd snake-game
```

### Run the game

```bash
python snake.py
```

---

## 🎮 Controls

| Key | Action                  |
| --- | ----------------------- |
| ↑   | Move Up                 |
| ↓   | Move Down               |
| ←   | Move Left               |
| →   | Move Right              |
| W   | Move Up                 |
| S   | Move Down               |
| A   | Move Left               |
| D   | Move Right              |
| R   | Restart after Game Over |

---

## 📂 Project Structure

```text
snake-game/
│
├── snake.py
├── README.md
└── screenshot.png
```

---

## 🏗 Architecture

The project follows an object-oriented design:

### Snake

Responsible for:

* Snake movement
* Growth mechanics
* Direction handling

### Food

Responsible for:

* Random food generation
* Preventing food from spawning inside the snake

### SnakeGame

Responsible for:

* Rendering
* Game loop
* Input handling
* Collision detection
* Score management

---

## 🔧 Customization

### Change Game Speed

```python
INITIAL_SPEED = 120
```

Lower values make the snake move faster.

---

### Change Window Size

```python
WIDTH = 600
HEIGHT = 600
```

---

### Change Colors

```python
BACKGROUND_COLOR = "#111111"
SNAKE_COLOR = "#00ff66"
FOOD_COLOR = "#ff3333"
```

---

## 📈 Future Improvements

Potential enhancements include:

* High score system
* Difficulty levels
* Pause functionality
* Sound effects
* Animated graphics
* Obstacles
* Multiplayer mode
* Power-ups
* AI-controlled snake
* Save/load game state

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## ❤️ Acknowledgments

Inspired by the classic Snake game that has entertained generations of players and programmers.
