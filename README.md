## Connect Four Game using NumPy and Pygame

Connect Four is also known as Four Up, Plot Four, Four in a Row, and Drop Four. It is a two-player connection board game, where each player takes turns dropping their respective colored discs into a seven-column, six-row vertically suspended grid. The objective of the game is to be the first one to form a horizontal, vertical, or diagonal line of four in one's disc colors.

### Step 1: Creating the Board
Pygame is a free and open-source cross-platform library for multimedia applications using Python.

### Step 2: Tracking the end of the game
Through alternating between the two players, we also need to be tracking when there is a possible `win` being made within the game in order to stop the program. At the end of the game, we can decide whether we want to implement a restart button or simply have the program close.

### Step 3: Allowing players to make moves
Since not all moves are valid within the game, there has to be a method of making sure each player is playing by the rules. This also means making sure the program doesn't mistakenly replaces one player's pieces for another.