
import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 1000, 650                               # window size

startpoint_dog = 700
startpoint_bird = 40

#def draw_background():

def draw_rectangle(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def draw_dog(x, y, z):
    glPointSize(40.0)
    glBegin(GL_POINTS)
    glVertex3f(x, y, z)
    glEnd()

def draw_bird(x, y, z):
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex3f(x, y, z)
    glEnd()


def move_dog(x, y, z):
    global startpoint_dog
    #glPushMatrix()
    #glTranslatef(startpoint_for_move, 0.0, 0.0)
    #startpoint_dog = startpoint_dog - 3.0
    #if startpoint_dog < 30:
        #startpoint_dog = 900
    draw_dog(startpoint_dog, y, z)
    #glPopMatrix()

def move_bird(x, y, z):
    global startpoint_bird
    #glPushMatrix()
    #glTranslatef(startpoint_for_move, 0.0, 0.0)
    startpoint_bird = startpoint_bird + 2.0
    if startpoint_bird > 900:
        startpoint_bird = 40
    draw_bird(startpoint_bird, y, z)
    #glPopMatrix()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# The keyboard controls
def special(key, x, y):
    global startpoint_dog
    # Rotate cube according to keys pressed
    if key == GLUT_KEY_LEFT:
        if startpoint_dog >= 30:
            startpoint_dog = startpoint_dog - 5.0
    if key == GLUT_KEY_RIGHT:
        if startpoint_dog <= 970:
            startpoint_dog = startpoint_dog + 5.0
    # if key == space:
    # Hundchen bellt
    # maybe ~ if key == "q":
    #       ~ sys.exit()



def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d

    #glDisable(GL_CULL_FACE)
    glDisable(GL_LIGHTING)



    glColor3f(0.0, 1.0, 0.0)
    draw_rectangle(0.0, 0.0, 1000, 400)                # rect for grass (0, 0) with width 1000, height 400

    glColor3f(0.0, 0.0, 1.0)
    draw_rectangle(0.0, 400.0, 1000, 250)              # rect for sky (0, 400) with width 1000, height 250

    glColor3f(0.2, 0, 0)
    draw_rectangle(150.0, 90.0, 100, 300)

    glColor3f(1.0, 1.0, 0.0)
    move_dog(900.0, 100.0, 0.0)




    # glTranslatef(200.0, 0.0, 400.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.2, 0.0)
    glVertex3f(50.0, 390.0, 0.0)
    glVertex3f(350.0, 390.0, 0.0)
    glVertex3f(200.0, 625.0, 0.0)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    move_bird(40.0, 500.0, 0.0)


    glutSwapBuffers()                                  # important for double buffering
    #time.sleep(1 / 32)

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Hund und Vogel")            # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
# The callback function for keyboard controls
glutSpecialFunc(special)
glutMainLoop()                                         # start everything
