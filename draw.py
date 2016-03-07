from display import *
from matrix import *

def drawScreen(matrix, screen, color):
    cur = 0
    #prev = matrix[0]
    while cur < (len(matrix)-1):
        drawLine(screen, int(matrix[cur][0]), int(matrix[cur][1]), int(matrix[cur+1][0]), int(matrix[cur+1][1]), color)
        cur+=2
        #prev = matrix[cur-1]

def addPoint(matrix, x, y, z=0):
    matrix.append([x,y,z,1])
    
def addEdge( matrix, x0, y0,z0, x1, y1, z1):
    addPoint(matrix, x0, y0, z0)
    addPoint(matrix, x1, y1, z1)

def drawLine( screen, x0, y0, x1, y1, color ):
    if x1 < x0:
        holder = x0
        x0 = x1
        x1 = holder
        holder = y0
        y0 = y1
        y1 = holder
    #8 cases reduced to 4
    if (y1 >= y0): #if positive slope
        if y1 - y0 > x1 - x0: #if slope > 1
            dx = x1 - x0
            dy = y1 - y0
            dx2 = dx * 2
            dif2 = 2 * (dx - dy)
            k = (dx * 2) - dy
            x = x0
            y = y0
            while y <= y1:
                if (k < 0):
                    k += dx2
                    plot(screen, color, x, y)
                else:
                    k += dif2
                    x += 1
                    plot(screen, color, x, y)
                y+=1
        else: #if slope <= 1
            dx = x1 - x0
            dy = y1 - y0
            dy2 = dy * 2
            dif2 = 2 * (dy - dx)
            k = (dy * 2) - dx
            y = y0
            x = x0
            while x <= x1:
                if (k < 0):
                    k += dy2
                    plot(screen, color, x, y)
                else:
                    k += dif2
                    y += 1
                    plot(screen, color, x, y)
                x+=1
    else: #negative slope
        if y0 - y1 > x1 - x0: #if slope > -1
            y0, y1 = -1*y0, -1*y1
            dx = x1 - x0
            dy = y1 - y0
            dx2 = dx * 2
            dif2 = 2 * (dx - dy)
            k = (dx * 2) - dy
            x = x0
            y = y0
            while y <=y1:
                if (k < 0):
                    k += dx2
                    plot(screen, color, x, -1*y)
                else:
                    k += dif2
                    x += 1
                    plot(screen, color, x, -1*y)
                y+=1
        else: #if slope < -1
            y0, y1 = -1*y0, -1*y1
            dx = x1 - x0
            dy = y1 - y0
            dy2 = dy * 2
            dif2 = 2 * (dy - dx)
            k = (dy * 2) - dx
            y = y0
            x = x0
            while x<=x1:
                if (k < 0):
                    k += dy2
                    plot(screen, color, x, -1*y)
                else:
                    k += dif2
                    y += 1
                    plot(screen, color, x, -1*y)
                x+=1
    pass
