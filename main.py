"""Запуск игры «Змейка» из корня проекта."""

import runpy
from pathlib import Path


if __name__ == '__main__':
    game_path = Path(__file__).resolve().parent / 'the_snake-main' / 'the_snake.py'
    runpy.run_path(str(game_path), run_name='__main__')
