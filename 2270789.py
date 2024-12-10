from graphix import Window, Rectangle, Point, Circle, Polygon, Line

def draw_rectangle( win,p1, p2, colour):
    rectangle = Rectangle(p1, p2)
    rectangle.fill_colour = colour
    rectangle.draw(win)

def draw_polygon(win, points, colour):
    polygon = Polygon(points)
    polygon.fill_colour = colour
    polygon.draw(win)

def draw_circle(win, centre, radius, colour,):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.draw(win)


def draw_triangles_up(win, x, y, colour):
    top_triangle_top = Point(x + 10, y)
    top_triangle_left = Point(x, y + 10)
    top_triangle_right = Point(x + 20, y + 10)

    bottom_triangle_top = Point(x + 10, y + 10)
    bottom_triangle_left = Point(x, y + 20)
    bottom_triangle_right = Point(x + 20, y + 20)

    draw_polygon(win, [top_triangle_top, top_triangle_left, top_triangle_right], colour)
    draw_polygon(
        win, [bottom_triangle_top, bottom_triangle_left, bottom_triangle_right], colour
    )


def draw_triangles_down(win, x, y, colour):
    top_triangle_top = Point(x + 20, y + 10)
    top_triangle_left = Point(x + 10, y)
    top_triangle_right = Point(x + 10, y + 20)

    bottom_triangle_top = Point(x + 10, y + 10)
    bottom_triangle_left = Point(x, y)
    bottom_triangle_right = Point(x, y + 20)

    draw_polygon(win, [top_triangle_top, top_triangle_left, top_triangle_right], colour)
    draw_polygon(
        win, [bottom_triangle_top, bottom_triangle_left, bottom_triangle_right], colour
    )



def draw_triangles_patch(win, tl_x, tl_y, colour):
    gap = 20
    for  y in range(5):
        for  x in range(5):
            if (x + y) % 2 == 0:
                draw_circle(
                    win=win,
                    centre=Point(tl_x + x*gap + 10, tl_y + y * gap + 10),
                    radius=10,
                    colour=colour,
                )
            else:
                if  y % 2 == 0:
                    draw_triangles_up(
                        win,
                        tl_x+x*gap,tl_y+y*gap,colour
                    )
                else:
                    draw_triangles_down(
                        win,
                        tl_x+x*gap,tl_y+y*gap,colour
                    )
              

def draw_final_patch(win, tl_x, tl_y, colour):
    step = 10

    for i in range(0, 100 + step, step):
        line1 = Line(
            Point(tl_x + i, tl_y),
            Point(tl_x + 100, tl_y + i),
        )
        line1.fill_colour = colour
        line1.draw(win)

        line2 = Line(
            Point(tl_x, tl_y + i),
            Point(tl_x + i, tl_y + 100),)
        line2.fill_colour = colour
        line2.draw(win)


def draw_grid(win, window_size, colour_1, colour_2, colour_3):
    for y in range(0, window_size, 100):
        for x in range(0, window_size, 100):
            if x < y and x+y < window_size - 100:
                if y <= window_size // 2:
                    draw_triangles_patch(win, x, y, colour=colour_2)
                else:
                    draw_rectangle(
                        win,
                        Point(x, y),
                        Point(x+100, y+100),
                        colour=colour_2,
                    )
            elif x > y and x+y > window_size - 100:
                if y <= window_size // 2:
                    draw_triangles_patch(win, x, y, colour=colour_3)
                else:
                    draw_rectangle(
                        win,
                        Point(x, y),
                        Point(x+100, y+100),
                        colour=colour_3,
                    )
            else:
                if y > window_size // 2 - 100:
                    draw_final_patch(win, x, y, colour_1)
                else:
                    draw_rectangle(win, Point(x, y), Point(x+100, y+100),colour=colour_1)

def test():
    window_size = 900
    win = Window("Testing", window_size, window_size)
    colour_1 = "blue"
    colour_2 = "orange"
    colour_3 = "red"

    draw_grid(win, window_size, colour_1, colour_2, colour_3)
    win.get_mouse()


test()
