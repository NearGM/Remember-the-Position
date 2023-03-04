Remember the Position
=====================

This program generates a random chess position from a PGN file, displays the position on the screen for 10 seconds, and then prompts the user to enter the positions of the pieces on the board. The goal is to correctly identify the positions of all pieces on the board..

![](./ft.gif)

Requirements
------------

The script requires the [Python Chess library](https://github.com/niklasf/python-chess) to be installed. You can install it using pip:

    pip install chess

Usage
-----

1.  Clone the repository and navigate to the directory:

    `git clone https://github.com/NearGM/Remember-the-Position`
    
2.  Navigate to the cloned repository folder using the command line.
3.  Place your PGN files with chess games in the `Games` folder or use the one already there.
4.  Run the script:

    `python remember_the_position.py`

6.  Look at the chess board and remember the positions of the pieces. You will have 10 seconds.
7.  After 10 seconds, the board will disappear, and you will be prompted to enter the positions of the pieces.
8.  Enter the positions of the pieces in the format "piece name + square name" (e.g., "Kg1", "nd4").
9.  If you correctly identify all the positions, the script will print "You got all positions correct!"

Contributing
------------

If you have any suggestions for improvements or find any bugs, feel free to open an issue or a pull request on the [GitHub repository](https://github.com/NearGM/Remember-the-Position).
