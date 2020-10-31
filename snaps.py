# Some pygame helper functions for simple image display
# and sound effect playback
# Rob Miles July 2017
# Version 1.0

import time
import random
import sys
import urllib.request
import pygame

pygame_available = True
surface = None
sound_available = False

def install_pygame():
    print("Installing pygame")

    version = sys.version_info
    if version[0] != 3:
        print("Must have version 3 of Python")
        return False

    try:
        import pip
        pip.main(['install', 'pygame'])
        
    except ImportError:
        print("pip is not installed on this machine")
        print("Check your Python installation")
        return False

    print("Pygame installed")
    return True

def setup_pygame():
    global pygame_available

    if pygame_available:
        return
    try:
        import pygame
        pygame_available = True
        print("setup pygame")
    except ImportError:
        if not install_pygame():
            print("pygame installation failed")
        try:
            import pygame
            pygame_available = True    
        except ImportError:
            print("The installation of pygame didn't work.")
            print("Remove and re-install Python and try again")

def setup(width=800, height=600, title=''):
    '''
    Sets up the pygame environment
    '''
    global window_size
    global back_color
    global text_color
    global image
    global surface
    global pygame_available

    setup_pygame()
    
    # Don't initialise if we don't have pygame
    if not pygame_available:
        print("Pygame is not installed on this machine")
        return
    
    # Don't initialise if we already have

    if surface is not None:
        return

    window_size = (width, height)
    back_color = (255, 255, 255)
    text_color = (255, 0, 0)
    image = None

    pygame.init()

    # Create the game surface
    surface = pygame.display.set_mode(window_size)

    clear_display()

    pygame.display.set_caption(title)

def handle_events():
    '''
    Consume events that are generated by the pygame window
    Captures key pressed events and sets the key_pressed value 
    '''
    global key_pressed
    setup()
    for event in pygame.event.get():
        pass

def play_sound(filepath):
    '''
    Plays the specified sound file
    '''
    global sound_available
    
    setup_pygame()
    
    # Don't initialise if we don't have pygame
    if not pygame_available:
        print("Pygame is not installed on this machine")
        return

    try:
    # pre initialise pyGame's audio engine to avoid sound latency issues
        pygame.mixer.pre_init(frequency=44100)
        pygame.mixer.init()
    except:
        print("There is no sound provision on this computer.")
        print("Sound commands will not produce any output")
        return

    sound = pygame.mixer.Sound(filepath)
    sound.play()

def display_image(filepath):
    '''
    Displays the image from the given filepath
    Starts pygame if required
    May throw exceptions
    '''
    global surface
    global window_size
    global image

    handle_events()
    image = pygame.image.load(filepath)
    image = pygame.transform.smoothscale(image, window_size)
    surface.blit(image, (0, 0))
    pygame.display.flip()


def clear_display():
    '''
    Clears the display to the background colour
    and the image (if any) on top of it
    '''

    global surface
    global image
    global back_color

    handle_events()

    surface.fill(back_color)
    if image is not None:
        surface.blit(image, (0, 0))

    pygame.display.flip()

def split_lines_on_spaces(text):
    '''
    returns a list of words which have been
    extracted from the text.
    Spaces on the ends of words are
    preserved
    '''
    result = []
    got_space = False
    word = ''
    for ch in text:
        if ch == ' ':
            got_space = True
            word = word + ch
        else:
            if got_space:
                # first character of next word
                result.append(word)
                word=ch
                got_space=False
            else:
                word = word + ch

    result.append(word)

    return result            
        

def get_display_lines(text, font, width):
    '''
    Returns a list of strings which have been split
    to fit the given window width using the supplied font
    '''
    result = []
    text_lines =  text.splitlines()
    for text_line in text_lines:
        words = split_lines_on_spaces(text_line)
        x = 0
        line = ''
        for word in words:
            word_width = font.size(word)[0]
            if x + word_width > width:
                # Remove the trailing space from the line
                # before adding to the list of lines to return
                result.append(line)
                line = word
                x = word_width
            else:
                line = line + word
                x = x + word_width

        result.append(line)
    return result


def render_message(text, size=200, margin=20, horiz='center', vert='center',
                    color=(255, 0, 0), cursor=''):

    # Get the text version of the input
    text = str(text)

    font = pygame.font.Font(None, size)

    available_width = window_size[0] - (margin * 2)

    lines = get_display_lines(text, font, available_width)

    rendered_lines = []

    height = 0

    for line in lines:
        rendered_line = font.render(line, 1, color)
        height += rendered_line.get_height()
        rendered_lines.append(rendered_line)

    if height > window_size[1]:
        raise Exception('Text too large for window')

    if vert == 'center':
        y = (window_size[1] - height) / 2.0
    elif vert == 'bottom':
        y=(window_size[1]-margin) - height
    else:
        # default vertical cursor position is top
        y = margin


    for rendered_line in rendered_lines:
        width = rendered_line.get_width()
        height = rendered_line.get_height()
        if horiz == 'center':
            x = (available_width - width) / 2.0 + margin
        elif horiz == 'right':
            x = window_size[0] - width - margin
        else:
            # default position is left margin
            x = margin
        surface.blit(rendered_line, (x, y))
        y += height

    if cursor:
        cursor_size = font.size(cursor)
        cursor_width = cursor_size[0]
        cursor_height = cursor_size[1]
        if len(rendered_lines):
            # put the cursor on the end of an existing line
            y -= height
            x += width
        else:
            # put the cursor in the start position for this
            # orientation
            # default x position is the margin
            x = margin
            
            if horiz == 'center':
                x = (available_width - cursor_width) / 2.0 + margin
            elif horiz == 'right':
                x = window_size[0] - cursor_width - margin
            else:
                # default position is left margin
                x = margin

            if vert == 'center':
                y = (window_size[1] - cursor_height) / 2.0
            elif vert == 'bottom':
                y=(window_size[1]-margin) - cursor_height
            else:
                # default vertical cursor position is top
                y = margin
            
        cursor_image = font.render(cursor, 1, color)
        surface.blit(cursor_image, (x, y))
        
    pygame.display.flip()


def display_message(text, size=200, margin=20, horiz='center', vert='center',
                    color=(255, 0, 0)):
    '''
    Displays the text as a message
    Size can be used to select the size of the
    text
    '''
    global window_size
    global surface

    handle_events()

    clear_display()

    render_message(text, size=size, margin=margin, horiz=horiz, vert=vert, color=color)

def get_dot():
    '''
    Waits for a mouse movement and then returns it
    as a tuple of x and y coordinates
    '''
    setup()
    while True:
        event = pygame.event.wait()
        if event.type == 4:
            # Event 4 is mouse motion
            pos = event.dict['pos']
            return pos

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW =   (255,   255,   0)
MAGENTA =   (255,   0,   255)
CYAN =   (0,   255,   255)
 
dot_color = WHITE

def set_color(r,g,b):
    dot_color = (r,g,b)

def set_random_color():
    global dot_color
    dot_color = (random.randint(0,255),
                 random.randint(0,255),
                 random.randint(0,255))

def get_mouse_pressed():
    return pygame.mouse.get_pressed()[0]


def draw_dot(pos, radius):
    setup()
    pygame.draw.circle(surface, dot_color, pos, radius)
    pygame.display.flip()


def get_key():
    '''
    Waits for a keypress and then returns it as a string
    Only characters are returned, not control keys
    '''
    setup()
    while True:
        event = pygame.event.wait()
        if event.type == 2:
            # Event 2 is keydown
            key_code = event.dict['unicode']
            if key_code:
                return key_code
            

def get_string(prompt, size=50, margin=20,
               color=(255, 0, 0), horiz='left', vert='center',
               max_line_length=20):
    '''
    Reads a string from the user
    '''

    setup()

    result = ''
    cursor_char = '*'
    cursor = None
    
    def redraw():
        clear_display()
       
        render_message(prompt+result, margin=margin, size=size,
                       horiz=horiz, vert=vert, color=color, cursor=cursor)

    def cursor_flip():
        nonlocal cursor

    # create a timer for the cursor

    cursor_event = pygame.USEREVENT+1
    
    pygame.time.set_timer(cursor_event,500)

    while True:
        event = pygame.event.wait()

        if event.type == cursor_event:
            if cursor:
                cursor = None
            else:
                cursor = cursor_char
            redraw()
        elif event.type == 2:
            # Event 2 is keydown
            key_code = event.dict['unicode']
            if key_code is None:
                continue
            if key_code == '\r':
                break
            elif key_code == '\x08':
                if len(result) > 0:
                    result=result[:-1]
                    redraw()
            else:
                if len(result) < max_line_length:
                    result += key_code
                    redraw()

    # disable the timer for the cursor
    pygame.time.set_timer(cursor_event,0)
    return result

import urllib.request
import xml.etree.ElementTree

def get_weather_temp(latitude,longitude):
    '''
    Uses forecast.weather.gov to get the weather
    for the specified latitude and longitude
    '''
    url="http://forecast.weather.gov/MapClick.php?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml".format(latitude,longitude)
    req=urllib.request.urlopen(url)
    page=req.read()
    doc=xml.etree.ElementTree.fromstring(page)
    # I'm not proud of this, but by gum it works...
    for child in doc:
        if child.tag == 'data':
            if child.attrib['type'] == 'current observations':
                for item in child:
                    if item.tag == 'parameters':
                        for i in item:
                            if i.tag == 'temperature':
                                if i.attrib['type'] == 'apparent':
                                    for t in i:
                                        if t.tag =='value':
                                            return int(t.text)


def get_weather_desciption(latitude,longitude):
    '''
    Uses forecast.weather.gov to get the weather
    for the specified latitude and longitude
    '''
    url="http://forecast.weather.gov/MapClick.php?lat={0}&lon={1}&unit=0&lg=english&FcstType=dwml".format(latitude,longitude)
    req=urllib.request.urlopen(url)
    page=req.read()
    doc=xml.etree.ElementTree.fromstring(page)
    # I'm not proud of this, but by gum it works...
    for child in doc:
        if child.tag == 'data':
            if child.attrib['type'] == 'current observations':
                for item in child:
                    if item.tag == 'parameters':
                        for i in item:
                            if i.tag == 'weather':
                                for t in i:
                                    if t.tag == 'weather-conditions':
                                        if t.get('weather-summary') is not None:
                                            return t.get('weather-summary')


