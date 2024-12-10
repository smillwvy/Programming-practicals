from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)
    
#Polygons
def draw_rectangle():
    win = Window()
    points = [Point(200, 50), Point(50, 250), Point(350, 250)]
    triangle = Polygon(points)
    triangle.draw(win)
    triangle.fill_colour = "red"
    
    win.get_mouse()
    win.close()

def message_text():
    message.size = 30
    message.typeface = "times roman"
    message.text_colour = "magenta"
    
    click_point = win.get_mouse()
    message.move(click_point.x, click_point.y) 
    message.draw(win)
    
    win.get_mouse()
    win.close()

def click_point():
    win = Window()
    
    click_point = win.get_mouse()

    message = Text(click_point, "Hello!")
    message.size = 30
    message.typeface = "times roman"
    message.text_color = "magenta"
    message.draw(win)

    win.get_mouse()
    win.close()


#Exercise 1
def draw_stick_figure():
    win = Window()
    
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)

#Exercise 1(1)
def draw_line():
    win = Window()
    
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    
    p1 = win.get_mouse()
    message.text = "click on second point"
    
    p2 = win.get_mouse()
    
    line = Line(p1, p2)
    line.draw(win)
    
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()

#Exercise 1(2)
def create_stick_figure():
    win = Window()
    
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    
    left_arm = Line(Point(160, 180), Point(240, 180))
    left_arm.draw(win)
    
    left_leg = Line(Point(200, 240), Point(160, 300))
    left_leg.draw(win)
    
    right_leg = Line(Point(200, 240), Point(240, 300))
    right_leg.draw(win)
    
    win.get_mouse()
    win.close()
    
#Exercise 2
def draw_circle():
    radius = int(input("Enter the radius of the circle: "))
    
    win = Window()
    
    circle = Circle(Point(200, 200), radius)
    circle.draw(win)
    
    win.get_mouse()
    win.close()

#Exercise 3 (error)
def draw_circle(win, center, radius, color):
    circle = Circle(center, radius)
    circle.fill_color = color
    circle.outline_color = "black"
    circle.draw(win)

def draw_archery_target():
    win = Window()
    
    yellow_radius = 30
    draw_circle(win, Point(200, 200), yellow_radius, "yellow")
    draw_circle(win, Point(200, 200), yellow_radius * 2, "red")
    draw_circle(win, Point(200, 200), yellow_radius * 3, "blue")

    win.get_mouse()
    win.close()
    
#Exercise 4 (error)
def draw_rectangle():
    win = Window()
    
    width = float(input("Enter the width of the rectangle (less than 400): "))
    height = float(input("Enter the height of the rectangle (less than 400): "))
#     
#     top_left_x = (400 - width) / 2
#     top_left_y = (400 - height) / 2
    
#     bottom_right_x = top_left_x + width
#     bottom_right_y = top_left_y + height
    
    top_left = Point(int(200 - width/2), int(200 - height/2))
    bottom_right = Point(int(200 + width/2), int(200 + height/2))
    rect = Rectangle(top_left, bottom_right)
    rect.draw(win)
    
    
    
    
#     rect = Rectangle(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))
#     rect.fill_color = "blue"
#     rect.outline_color = "black"
#     rect.draw(win)
    
    win.get_mouse()
    win.close()

#Exercise 5 (error)
def blue_circle():
    win = Window()
    message = Text(Point(200, 50), "Click to draw a blue circle")
    message.draw(win)

    center = win.get_mouse()
    circle = Circle(center, 100)
    circle.fill_color = "blue"
    circle.outline_color = "black"
    circle.draw(win)

    message.text = "Click anywhere to quit"
    win.get_mouse()
    win.close()

#Exercise 6
def ten_lines():
    win = Window()
    message = Text(Point(200, 50), "Click to draw 10 lines")
    message.draw(win)

    for i in range(10):
        message.text = "Click on the first point for line " + str(i + 1)
        p1 = win.get_mouse()
        
        message.text = "Click on the second point for line " + str(i + 1)
        p2 = win.get_mouse()
        
        line = Line(p1, p2)
        line.draw(win)

    message.text = "Click anywhere to quit"
    
    win.get_mouse()
    win.close()





    
    





