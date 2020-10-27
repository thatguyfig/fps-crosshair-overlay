import win32.win32gui as win32gui
import win32.win32api as win32api

class Screen:
    width = 1920
    height = 1080

class Crosshair:

    ## sets length of lines
    length = 30
    thickness = 1

    ## sets colour of the lines
    colour = {
        "red": 255,
        "green": 0,
        "blue": 0
    }

    # offset from the center point 
    X_offset = 0 
    Y_offset = 0


def get_screen_centre(width, height) -> dict:
    center = {"x":width/2, "y": height/2}
    return center

def build_rgb_colour(red: int, green: int, blue: int):
    colour = win32api.RGB(red, green, blue)
    return colour



def draw_on_screen(location: dict, colour):

    # iterate forever
    while True:

        # always try to draw
        try:

            # if the length is 0
            if Crosshair.length <= 1:
                
                # just draw center
                win32gui.SetPixel(dc, int(location['x']), int(location['y']), colour) # center

            # otherwise draw multiple lines
            else:

                # iterate for the length drawing a line
                for x in range(Crosshair.length):
                    win32gui.SetPixel(dc, int(location['x'])+x, int(location['y']), colour) # right
                    win32gui.SetPixel(dc, int(location['x'])-x, int(location['y']), colour) # left
                    win32gui.SetPixel(dc, int(location['x']), int(location['y'])-x, colour) # bottom
                    win32gui.SetPixel(dc, int(location['x']), int(location['y'])+x, colour) # top



        # if we try to stop the process, kill it
        except KeyboardInterrupt as e:
            raise(e)

        # otherwise ignore errors
        except:
            pass


# get device context
dc = win32gui.GetDC(0)

# calculate location to draw the crosshair
location = get_screen_centre(Screen.width, Screen.height)
location['x'] = location['x'] + Crosshair.X_offset
location['y'] = location['y'] + Crosshair.Y_offset

# build the cross hair colour
colour = build_rgb_colour(
    red=Crosshair.colour['red'],
    green=Crosshair.colour['green'],
    blue=Crosshair.colour['blue']
)

# draw the crosshair
draw_on_screen(
    location=location,
    colour=colour
)