# Pong Game 🏓

A clean, object-oriented recreation of the classic arcade game **Pong**, built using Python and the `turtle` graphics module.

This project implements a **dynamic difficulty system**: the ball increases its speed every time it hits a paddle, challenging the players' reflexes as the rally continues.

## 📋 Features

* **Dynamic Physics:** The ball accelerates after every collision with a paddle, making the game progressively harder.
* **Object-Oriented Design:** The code is structured using clean OOP principles (Facade Pattern, Inheritance) for maintainability and scalability.
* **Score Tracking:** Real-time scoreboard updates for both players.
* **Win Condition:** First player to reach **10 points** wins the game.
* **Smooth Controls:** Optimized input handling for responsive paddle movement.

## 🎮 Controls

| Player | Move Up | Move Down |
| :--- | :---: | :---: |
| **Player 1 (Left)** | `W` | `S` |
| **Player 2 (Right)** | `↑` (Arrow Up) | `↓` (Arrow Down) |

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python 3.x installed. The project uses the standard `turtle` library, so no external `pip` installations are required.
2.  **Clone or Download** the repository.
3.  **Navigate** to the project directory in your terminal.
4.  **Run the game** by executing the main script:

```bash
python main.py

```

## 📂 Project Structure

The project is modularized into specific classes to ensure separation of concerns:

* `main.py`: Entry point of the application.
* `PongGame.py`: The **Controller**. Manages the game loop, collision logic, and global states.
* `ball.py`: Handles ball physics, movement vectors, and speed increments.
* `bar.py`: Manages the visual representation and movement logic of the paddles.
* `player.py`: Acts as a **Facade**, grouping the `Bar` and `Scoreboard` into a single entity.
* `scoreboard.py`: Handles text rendering for scores and game-over messages.
* `game_constants.py`: Centralized configuration file for game parameters (screen size, speed, colors).

## ⚙️ Configuration

You can tweak the game settings in `game_constants.py` to adjust the difficulty:

```python
SCORE_TO_WIN = 10          # Points needed to win
BALL_INITIAL_SPEED = 1.2   # Speed multiplier
MAX_SPEED = 8              # Maximum ball speed cap

```

## 👤 Author

**TwoXMaybe(Cristhian Navas)** - Electronic Engineering Student

```

```
