from graphix import Window, Circle, Point


def get_quadrant_color(x, y, center_x, center_y):
    if x < center_x:
        if y < center_y:
            # Top-left quadrant
            return "red", "black"
        else:
            # Bottom-left quadrant
            return "", "yellow"
    else:
        if y < center_y:
            # Top-right quadrant
            return "blue", "black"
        else:
            # Bottom-right quadrant
            return "", "green"


def practice_part1():
    """
    Draw circles at click locations with quadrant-based coloring
    """
    win = Window("Part 1: Click Test", 400, 400)
    center_x, center_y = win.width // 2, win.height // 2

    for _ in range(5):
        click_point = win.get_mouse()
        x, y = click_point.x, click_point.y

        circle = Circle(click_point, 20)
        fill_colour, outline_colour = get_quadrant_color(x, y, center_x, center_y)
        circle.fill_colour = fill_colour
        circle.outline_colour = outline_colour
        circle.draw(win)

    win.get_mouse()
    win.close()


def practice_part2():
    """
    Draw circles in a grid arrangement in the top-left quadrant
    """
    win = Window("Part 2: Grid Arrangement", 400, 400)
    grid_size = 7
    circle_radius = 15
    spacing = 30

    for row in range(grid_size):
        for col in range(grid_size):
            x = col * spacing + circle_radius
            y = row * spacing + circle_radius

            circle = Circle(Point(x, y), circle_radius)
            circle.fill_colour = "red"
            circle.draw(win)

    win.get_mouse()
    win.close()


def practice_part2_1():
    """
    Draw circles in a grid arrangement in the top-left quadrant
    Difference from part 2 is that the circles amount calculated
    based on the window size and radius
    """
    win = Window("Part 2: Grid Arrangement", 400, 400)

    circle_radius = 20
    grid_size = (
        win.width // (circle_radius * 2)
    ) // 2  # Adjust grid size to fit within one quadrant
    spacing = circle_radius * 2

    start_x = circle_radius
    start_y = win.height - (grid_size * spacing) + circle_radius
    """
    Top Left
    start_x = circle_radius
    start_y = circle_radius
    Top Right
    start_x = win.width - (grid_size * spacing) + circle_radius
    start_y = circle_radius
    Bottom Left
    start_x = circle_radius
    start_y = win.height - (grid_size * spacing) + circle_radius
    Bottom Right
    start_x = win.width - (grid_size * spacing) + circle_radius
    """

    for row in range(grid_size):
        for col in range(grid_size):
            x = start_x + col * spacing
            y = start_y + row * spacing

            circle = Circle(Point(x, y), circle_radius)
            circle.fill_colour = "red"
            circle.draw(win)

    win.get_mouse()
    win.close()
    