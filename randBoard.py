import random
from board import Board
from character import Character
from grid import Grid
from item import create_item
from config import names, items

def generate_random_board(num_characters, num_items, gold_value, team):
    rows = 3
    cols = 7
    board = Board(Grid(rows, cols))
    occupied_positions = set()
    for _ in range(num_characters):
        if (gold_value < 1):
            break
        while True:
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            if (row, col) not in occupied_positions:
                occupied_positions.add((row, col))
                break
        while True:
            name = random.choice(names)
            character = Character.create_character(name, (row, col), team)
            if character.cost <= 3:
                star_lvl = random.randint(1, 3)
            else:
                star_lvl = random.randint(1, 2)
            character.star_lvl = star_lvl
            if star_lvl != 1:
                cost = character.cost * pow(3, star_lvl - 1)
            else:
                cost = character.cost
            if cost <= gold_value:
                gold_value -= cost
                break
        random_item = random.randint(0, min(num_items, 3))
        num_items -= random_item
        for _ in range(random_item):
            item = random.choice(items)
            itemToAdd = create_item(item)
            character.add_item(itemToAdd)
        board.place_character(character, row, col)
    return board
