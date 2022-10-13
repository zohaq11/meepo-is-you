from game import *
from actor import *
import pytest
import pygame
import os

# USE PYGAME VARIABLES INSTEAD
keys_pressed = [0] * 512

# Setting key constants because of issue on devices
pygame.K_RIGHT = 1
pygame.K_DOWN = 2
pygame.K_LEFT = 3
pygame.K_UP = 4
pygame.K_LCTRL = 5
pygame.K_z = 6
RIGHT = pygame.K_RIGHT
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
UP = pygame.K_UP
CTRL = pygame.K_LCTRL
Z = pygame.K_z


def setup_map(map: str) -> 'Game':
    """Returns a game with map1"""
    game = Game()
    game.new()
    game.load_map(os.path.abspath(os.getcwd()) + '/maps/' + map)
    game.new()
    game._update()
    game.keys_pressed = keys_pressed
    return game


def set_keys(up, down, left, right, CTRL=0, Z=0):
    keys_pressed[pygame.K_UP] = up
    keys_pressed[pygame.K_DOWN] = down
    keys_pressed[pygame.K_LEFT] = left
    keys_pressed[pygame.K_RIGHT] = right
    keys_pressed[pygame.K_LCTRL] = CTRL
    keys_pressed[pygame.K_z] = Z


def test1_move_player_up():
    """
    Check if player is moved up correctly
    """
    game = setup_map("student_map1.txt")
    set_keys(1, 0, 0, 0)
    result = game.player.player_move(game)
    assert result == True
    assert game.player.y == 1


def test2_push_block():
    """
    Check if player pushes block correctly
    """
    game = setup_map("student_map2.txt")
    set_keys(0, 0, 0, 1)
    wall = \
        [i for i in game._actors if isinstance(i, Block) and i.word == "Wall"][0]
    result = game.player.player_move(game)
    assert result == True
    assert game.player.x == 3
    assert wall.x == 4


# def test3_create_rule_wall_is_push():
#    """
#    Check if player creates wall is push rule correctly
#    """
#    game = setup_map("student_map2.txt")
#    set_keys(0, 0, 0, 1)
#    wall = \
#    [i for i in game._actors if isinstance(i, Block) and i.word == "Wall"][0]
#    result = game.player.player_move(game)
#    game._update()
#    # only works : game._rules[1] == Wall  isPush
#    assert game._rules[0] == "Wall isPush"
#    assert game.player.x == 3
#    assert wall.x == 4


def test_4_follow_rule_wall_is_push():
    """
    Check if player follows rules correctly
    """
    game = setup_map("student_map3.txt")
    set_keys(0, 0, 0, 1)
    wall_object = game._actors[game._actors.index(game.player) + 1]
    result = game.player.player_move(game)
    assert game.player.x == 2
    assert wall_object.x == 3


def test_5_no_push():
    """
    Check if player is not able to push because of rule not existing
    """
    game = setup_map("student_map4.txt")
    set_keys(0, 0, 0, 1)
    wall_object = game._actors[game._actors.index(game.player) + 1]
    result = game.player.player_move(game)
    assert game.player.x == 2
    assert wall_object.x == 2

# All of my tests


def test_6_push_wall_rule():
    """
    this tests for whether the push wall is active or not
    """
    game = setup_map("student_map5.txt")
    game.player.x = 11
    game.player.y = 5
    for x in range(0, 4):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 7
    game.player.y = 9
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()

    assert game.player.x == 8
    assert game.player.y == 9


def test_7_push_flag_rule():
    """
    this tests for whether the push flag is active or not
    """
    game = setup_map("student_map5.txt")
    game.player.x = 20
    game.player.y = 5
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 9):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 2, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 7):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 5):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()

    game.player.x = 19
    game.player.y = 5
    game._update()

    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()

    assert game.player.x == 20
    assert game.player.y == 5


def test_8_test_wall_lose():
    """
    test if wall isLose works
    """
    game = setup_map("student_map5.txt")
    game.player.x = 9
    game.player.y = 5
    game._update()

    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.win_or_lose()
    assert game.player == None


def test_9_move_player_down():
    """
    Check if player is moved down correctly
    """
    game = setup_map("student_map5.txt")
    set_keys(0, 1, 0, 0)
    result = game.player.player_move(game)
    assert result == True
    assert game.player.y == 3


def test_10_move_player_left():
    """
    Check if player is moved left correctly
    """
    game = setup_map("student_map5.txt")
    set_keys(0, 0, 1, 0)
    result = game.player.player_move(game)
    assert result == True
    assert game.player.x == 4


def test_11_move_player_right():
    """
    Check if player is moved right correctly

    """
    game = setup_map("student_map5.txt")
    set_keys(0, 0, 0, 1)
    result = game.player.player_move(game)
    assert result == True
    assert game.player.x == 6


def test_12_boundary():
    """
    Check if player is not crossing the boundary
    """
    game = setup_map("student_map5.txt")
    set_keys(0, 0, 1, 0)
    result = game.player.player_move(game)
    set_keys(0, 0, 1, 0)
    result = game.player.player_move(game)
    set_keys(0, 0, 1, 0)
    result = game.player.player_move(game)
    set_keys(0, 0, 1, 0)
    result = game.player.player_move(game)
    set_keys(0, 0, 1, 0)
    result = game.player.player_move(game)
    assert result == False


def test_13_test_flag_lose():
    """
    test if flag isLose works
    """
    game = setup_map("student_map5.txt")
    game.player.x = 9
    game.player.y = 6
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 18
    game.player.y = 5
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()

    game.win_or_lose()
    assert game.player == None


def test_14_test_wall_stop():
    """
    test is wall isStop works
    """
    game = setup_map("student_map5.txt")
    game.player.x = 9
    game.player.y = 5
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 11):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 11
    game.player.y = 15
    game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    assert (game.player.x, game.player.y) == (11, 15)


def test_15_test_wall_victory():
    """
    test if wall isVictory works
    """
    game = setup_map("student_map5.txt")
    game.player.x = 10
    game.player.y = 4
    game._update()

    for x in range(0, 6):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 18
    game.player.y = 7
    game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.win_or_lose()
    assert game.get_running() == False


def test_16_move_through_wall():
    """
    check if you can move through wall when wall is not stop/push
    """
    game = setup_map("student_map5.txt")
    game.player.x = 7
    game.player.y = 8
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    assert (game.player.x, game.player.y) == (8, 8)


def test_17_check_two_rules():
    """
    check precendence when wall is lose then wall is victory
    It should implement the victory rule
    """
    game = setup_map("student_map5.txt")
    game.player.x = 9
    game.player.y = 5
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 4):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 5):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 7):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 5):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 14
    game.player.y = 8
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game.win_or_lose()
    assert game.get_running() == False


def test_18_check_two_rules_again():
    """
    check precendence when rock is push and the rock is victory
    it should implement the victory rule
    """
    game = setup_map("student_map5.txt")
    game.player.x = 7
    game.player.y = 11
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 12
    game.player.y = 10
    game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 9):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 4
    game.player.y = 4
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game.win_or_lose()
    assert game.get_running() == False


def test_19_check_basic_undo():
    """
    test the basic undo
    """
    game = setup_map("student_map5.txt")
    game._history.push(game._copy())
    game.player.x = 5
    game.player.y = 2
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game._undo()
    game._update()
    assert (game.player.x, game.player.y) == (5, 2)


def test_20_check_flag_is_stop():
    """
    check if flag isStop works
    """
    game = setup_map("student_map5.txt")
    game.player.x = 9
    game.player.y = 6
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 10):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 18
    game.player.y = 5
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    assert (game.player.x, game.player.y) == (18, 5)


def test_21_check_wall_is_vict():
    """
    check if wall is victory works
    """
    game = setup_map("student_map5.txt")
    game.player.x = 9
    game.player.y = 6
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 5):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 18
    game.player.y = 5
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    game.win_or_lose()
    assert game.get_running() == False


def test_22_rock_is_stop():
    """
    check if rock isStop correctly works
    """
    game = setup_map("student_map5.txt")
    game.player.x = 15
    game.player.y = 16
    game._update()
    for x in range(0, 8):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 5):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 4
    game.player.y = 4
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    assert (game.player.x, game.player.y) == (4, 4)


def test_23_double_rule():
    """
    check what happens when there are two rules being implemented
    on one iS block.
    Both the rules should work
    """
    game = setup_map("student_map5.txt")
    game.player.x = 7
    game.player.y = 11
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 3):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 11
    game.player.y = 6
    game._update()
    for x in range(0, 8):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 1, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 4):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 1):
        set_keys(1, 0, 0, 0)
        result = game.player.player_move(game)
        game._update()
    for x in range(0, 2):
        set_keys(0, 0, 1, 0)
        result = game.player.player_move(game)
        game._update()
    game.player.x = 4
    game.player.y = 4
    game._update()
    for x in range(0, 1):
        set_keys(0, 0, 0, 1)
        result = game.player.player_move(game)
        game._update()
    assert game.player.x == 5
    assert game.player.y == 4
    game.player.x = 18
    game.player.y = 5
    game._update()
    assert game.player.x == 18
    assert game.player.y == 5


if __name__ == "__main__":

    import pytest
    pytest.main(['student_tests.py'])
