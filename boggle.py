def make_grid(width, height):
    """
    create a grid that holds all of the tiles
    for a boggle game.
    """
    return {(row, col): ' ' for row in range(height)
        for col in range(width)
    }