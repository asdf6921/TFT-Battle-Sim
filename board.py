from grid import Grid, hex_grid
from character import Character

class Board:
    def __init__(self, grid):
        self.rows = grid.rows
        self.cols = grid.cols
        self.board = [['' for _ in range(self.cols)] for _ in range(self.rows)]
        self.character_positions = {}

    def place_character(self, character, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.board[row][col] = character
            self.character_positions[character] = (row, col)
        else:
            raise ValueError("Position out of bounds")

    def get_character_position(self, character):
        return self.character_positions.get(character, None)

    def remove_character(self, character):
        position = self.character_positions.pop(character, None)
        if position:
            row, col = position
            self.board[row][col] = ''
            print(f"{character.name} has been removed from the board.")

    def display_board(self):
        """Displays the board in a hexagonal format with staggered rows."""
        for r in range(self.rows):
            # Add indentation for odd rows
            prefix = " " if r % 2 == 1 else ""
            row_str = prefix + " ".join([cell if cell else '.' for cell in self.board[r]])
            print(row_str)
            
    def get_lowest_percent_health_ally(self, character):
        """Returns the ally with the lowest percentage HP on the same team as the given character."""
        lowest_health_ally = None
        lowest_hp_percent = float('inf')

        for ally in self.character_positions.keys():
            if ally.team == character.team and ally is not character:
                hp_percent = ally.hp / ally.max_hp
                if hp_percent < lowest_hp_percent:
                    lowest_health_ally = ally
                    lowest_hp_percent = hp_percent

        return lowest_health_ally

    def get_second_enemy(self, attacker, primary_target, exclude=set()):
        """Finds a second enemy for Runaan's Hurricane, avoiding primary target and already attacked enemies."""
        enemies = [
            enemy for enemy in self.character_positions.keys()
            if enemy.team != attacker.team and enemy is not primary_target and enemy not in exclude
        ]
        return min(enemies, key=lambda e: hex_grid.calculate_distance(attacker.position, e.position), default=None)
    
    @staticmethod
    def combine_boards(board1, board2):
        combined_row = board1.rows + board2.rows
        combined_col = max(board1.cols, board2.cols)
        combined_grid = Grid(combined_row, combined_col)
        combined_board = Board(combined_grid)

        # Place characters from the first board
        for character, (row, col) in board1.character_positions.items():
            combined_board.place_character(character, row, col)
        # Place characters from the second board, rotated by 180 degrees
        for character, (row, col) in board2.character_positions.items():
            new_row = 3 - row + 2
            new_col = 6 - col
            combined_board.place_character(character, new_row, new_col)
            character.update_position((new_row, new_col))
        return combined_board