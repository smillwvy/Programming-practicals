from graphix import Window, Point, Line, Circle, Rectangle, Text

def the_sleeper():
    win = Window("The Sleeper", 300, 200)
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    
    left_eye = Circle(Point(190,60), 5)
    left_eye.outline_color = "black"
    left_eye.draw(win)
    
    left_eye_line = Line(185, 195)
    line.draw(win)
    
    right_eye = Circle(Point(210,60), 5)
    right_eye.outline_color = "black"
    right_eye.draw(win)
    
    right_eye_line = Line(205, 215)
    line.draw(win)
    
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    
    arms = Line(Point(160, 90), Point(240, 90))
    arms.draw(win)
    
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)
    
    #duvet
    points = [Point(200, 50), Point(50, 250), Point(350, 250), Point(350, 250)]
    rectangle = Polygon(points)
    rectangle.draw(win)
    rectangle.fill_colour = "blue"
    
#exerxise 2
    message.size = 30
    message.typeface = "times roman"
    message.text_colour = "magenta"
    
    message = Text(Point(50, 50), "Buzz")
    message.draw(win)
    

    p1 = win.get_mouse()
    message.text = "Buzz"
    
    p2 = win.get_mouse()
    message.text = "Buzzz"
    
    p4 = win.get_mouse()
    message.text = "Buzzzz"
    
    p5 = win.get_mouse()
    message.text = "Buzzzzz"
    
    p6 = win.get_mouse()
    message.text = "Buzzzzzz"
    
    p7 = win.get_mouse()
    message.text = "Buzzzzz"
    message.draw(win)
    
    
    win.get_mouse()
    win.close()
    
