# PyGame Learning

Small PyGame practice project with two scripts:

- `01_basic.py` creates a window and prints a message when the right arrow key is pressed.
- `snakes_game.py` runs a basic Snake game with score and high score tracking.

## Folder Contents

- `01_basic.py` - starter PyGame window and keyboard input example.
- `snakes_game.py` - playable Snake game.
- `highScore.txt` - stores the best score for the Snake game.

## Requirements

- Python 3
- `pygame`

Install PyGame with:

```bash
pip3 install pygame
```

## How To Run

Open a terminal in this folder and run either script.

Basic PyGame demo:

```bash
python3 01_basic.py
```

Snake game:

```bash
python3 snakes_game.py
```

## Snake Game Controls

- Up Arrow: move up
- Down Arrow: move down
- Left Arrow: move left
- Right Arrow: move right
- Enter: restart after game over
- Close window: quit the game

## Notes

- Keep `highScore.txt` in the same folder as `snakes_game.py`, because the game reads and writes it directly.
- Run the scripts from this folder so file paths resolve correctly.
- This project is intended for learning the basics of PyGame window creation, input handling, movement, collision, and simple score persistence.

## Learning Areas Covered

- Initializing PyGame
- Creating a game window
- Handling keyboard events
- Drawing shapes on screen
- Managing a game loop
- Tracking score and high score
- Detecting collisions and game over state