class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def offset_to_axial(self, row, col):
        """Converts offset (row, col) to axial (q, r) coordinates."""
        q = col - (row // 2)  # Shift columns based on row parity
        r = row
        return (q, r)

    def calculate_distance(self, point1, point2):
        """Computes hex distance between two points given in (row, col)."""
        q1, r1 = self.offset_to_axial(*point1)
        q2, r2 = self.offset_to_axial(*point2)
        
        return (abs(q1 - q2) + abs(r1 - r2) + abs((q1 + r1) - (q2 + r2))) // 2

# Example: Create a hex grid
hex_grid = Grid(3, 7)