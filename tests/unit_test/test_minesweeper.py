import random

import pytest

from src import minesweeper


@pytest.fixture
def game():
    # Create a new Minesweeper game with a 3x3 grid and 2 mines
    random.seed(0)
    return minesweeper.Minesweeper(3, 3, 2)


def test_module_exists():
    assert minesweeper


def test_places_mines(game):
    assert len(game.mines) == 2, "There should be 2 mines"


# Bonus : How to put tests in classes to organize better your tests
class Test_reveal:
    def test_content(self, game):
        game.reveal(2, 2)
        assert (2, 2) in game.revealed, "A revealed tile should be visible in revealed"

    def test_bomb(self, game):
        assert (
            game.reveal(1, 1) == "Game Over"
        ), "Revealing a bomb should lead to game over"

    def test_normal(self, game):
        assert (
            game.reveal(2, 2) == "Continue"
        ), "Revealing a bomb should lead to game over"


def test_get_board_output(game):
    assert isinstance(game.get_board(), list), "get_board method should return a list"


def test_get_board_shape(game):
    board = game.get_board()
    assert len(board) == game.rows, "get_board should return same shape"
    assert all(
        len(row) == game.cols for row in board
    ), "get_board should return same shape"


def test_is_winner_false(game):
    for i in range(game.rows):
        for j in range(game.cols):
            if not (i, j) in game.mines:
                game.reveal(i, j)
    assert (
        game.is_winner()
    ), "When all tiles expect bombs are reavealed game should be won"


def test_is_winner_true(game):
    assert (
        not game.is_winner()
    ), "When not all neutral tiles are revealed, game should not be won"


def test_restart(game):
    old_board = game.board
    old_rows, old_cols, old_num_mines = game.rows, game.cols, game.num_mines
    game.restart()
    assert (old_rows, old_cols, old_num_mines) == (
        game.rows,
        game.cols,
        game.num_mines,
    ), "Base parameters shouldn't be modified"
    assert old_board != game.board, "Board should have changed"


def test_fail():
    assert False
