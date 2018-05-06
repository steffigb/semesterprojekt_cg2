import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 1000, 650                               # window size

startpoint_for_move = 900

#def draw_background():

def draw_rectangle(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def draw_dog(x, y, z):
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex3f(x, y, z)
    glEnd()


def move_dog(x, y, z):
    global startpoint_for_move
    #glPushMatrix()
    #glTranslatef(startpoint_for_move, 0.0, 0.0)
    startpoint_for_move = startpoint_for_move - 3.0
    if startpoint_for_move < 30:
        startpoint_for_move = 900
    draw_dog(startpoint_for_move, y, z)
    #glPopMatrix()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

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


    glutSwapBuffers()                                  # important for double buffering
    time.sleep(1 / 32)

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Hund und Vogel")            # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything
