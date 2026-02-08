# 🎮 Tic-Tac-Toe AI

A modular Python implementation of Tic-Tac-Toe featuring an AI opponent powered by the **Minimax algorithm**. Challenge yourself against three different difficulty levels, from a random-move beginner to an unbeatable expert.

## ✨ Features

- **Three AI Difficulty Levels:**
  - **Easy (Level 1):** AI moves completely at random.
  - **Intermediate (Level 2):** AI uses Minimax with limited depth, making it strategic but still beatable.
  - **Impossible (Level 3):** AI uses full Minimax recursion, making it mathematically impossible to win against.
- **Interactive CLI:** A simple and clean command-line interface with real-time board rendering.
- **Object-Oriented Design:** Logic is cleanly separated between the game engine ([Game.py](Game.py)) and the entry point ([main.py](main.py)).

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/noanjrd/TicTacToeAI.git
   cd TicTacToeAI
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## 🎯 How to Play

1. **Select Difficulty:** When prompted, type the name or number of the level (e.g., `1`, `Easy`, or `impossible`).
2. **Make Your Move:** Enter the coordinates for your move when prompted:
   - **x:** Horizontal position (1, 2, or 3)
   - **y:** Vertical position (1, 2, or 3)
3. **The Board:**
   ```
       1   2   3
      -----------
    1 |   |   |   |
      -----------
    2 |   |   |   |
      -----------
    3 |   |   |   |
      -----------
   ```

## 🧠 Technical Overview

The project uses the **Minimax algorithm**, a decision-making algorithm used in game theory for finding the optimal move in two-player zero-sum games.

- **`Game.minimax()`:** Recursively evaluates the board. It assigns a score of `+1` for an AI win, `-1` for a player win, and `0` for a draw.
- **`Game.level`:** Controls the search depth of the algorithm. In "Intermediate" mode, the AI's foresight is restricted, while in "Impossible" mode, it explores all possible future outcomes.

## 📂 Project Structure

- [main.py](main.py): Entry point of the application. Handles the game loop and user input.
- [Game.py](Game.py): Core game logic, including victory checks and the Minimax AI implementation.
- [README.md](README.md): Project documentation.