#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from Connect4.Connect4Logic import Grid
from Connect4.Connect4Logic import Game


def main():
    game = Game("yellow", "red")
    game.gamingTime()
    print("hello")


if __name__ == '__main__':
    main()
