# 🎮 Tic-Tac-Toe AI

A Python implementation of Tic-Tac-Toe with an AI opponent powered by the **Minimax algorithm**. Challenge yourself against three difficulty levels, from random moves to mathematically perfect play.

## ✨ Features

- **Three AI Difficulty Levels:**
  - **Easy:** Completely random moves
  - **Intermediate:** Minimax with depth limit (beatable)
  - **Impossible:** Full minimax recursion (unbeatable)
- **Interactive CLI:** Clean command-line interface with real-time board rendering
- **Modular Design:** Separated game logic, display, and input handling

## 🚀 Getting Started

### Prerequisites

- Python 3.x

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

1. **Select Difficulty:** Type `1`/`Easy`, `2`/`Inter`, or `3`/`Impossible`

2. **Make Your Move:** Enter x and y coordinates (1-3)

3. **Win:** Get three in a row horizontally, vertically, or diagonally

**Board Layout:**
```
    1   2   3
   -----------
 1 | x |   |   |
   -----------
 2 |   | o |   |
   -----------
 3 |   |   |   |
   -----------
```
- **x:** Your moves
- **o:** AI's moves

## 🧠 Technical Overview

The **Minimax algorithm** recursively evaluates all possible game states:
- `+1` for AI win
- `-1` for player win  
- `0` for draw

**Difficulty Implementation:**
- **Easy (level = 0):** Random moves only
- **Intermediate (level = 1):** Minimax with 1-move lookahead
- **Impossible (level = 100):** Complete game tree exploration

## 📂 Project Structure

- [main.py](main.py): Game loop and user input
- [Game.py](Game.py): Game logic and minimax AI
- [Displaying.py](Displaying.py): Board rendering and results
