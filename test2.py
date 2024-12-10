from graphix import Window, Circle, Point

def get_colour(x, y, center_x, center_y):
    if x < 150:
            return "red"
    elif x > 150 <300:
            return "black"
    elif x> 300 <450:
            return "blue"
    elif x> 450 <600:
            return "green"
        
def draw_circle1():
    win = Window("Circles", 600, 450)
    center_x, center_y = win.width // 2, win.height // 2

    for _ in range(12):
        click_point = win.get_mouse()
        x, y = click_point.x, click_point.y

        circle = Circle(click_point, 30)
        fill_colour = get_colour(x, y, center_x, center_y)
        circle.fill_colour = fill_colour
        circle.outline_colour = fill_colour
        circle.draw(win)

    win.get_mouse()
    win.close()

def draw_circle2():
    win = Window("Circles", 600, 450)
    circle_radius = 30
    grid_size = (
        win.width // (circle_radius * 2)
    ) // 2
    spacing = circle_radius * 2
    
    start_x = win.width // 2
    start_y = circle_radius
    
    for row in range(grid_size):
        for col in range(grid_size):
            x = start_x + col * spacing
            y = start_y + row * spacing
            
            circle = Circle(Point(x, y), circle_radius)
            
            fill_colour, outline_colour = get_colour(x, y, center_x, center_y)
            circle.fill_colour = fill_colour
            circle.outline_colour = outline_colour
            
            circle.draw(win)

    win.get_mouse()
    win.close()
    
    


    
    
    