"""
Main entry point for the Pong Game application.

This script acts as the entry point, instantiating the game logic
and starting the main execution loop.
"""
from PongGame import PongGame

def main() -> None:
    """
    Initialize the game instance and start the execution.

    Creates a `PongGame` object and calls the `start_game` method
    to activate the screen and the event loop.
    """
    pong = PongGame()
    pong.start_game()

if __name__ == "__main__":
    main()