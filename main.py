from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]


#display(screen)
m = []
addEdge(m, -20, -20, 0, 20, -20, 0)
addEdge(m, 20, -20, 0, 20, 20, 0)
addEdge(m, 20, 20, 0, -20, 20, 0)
addEdge(m, -20, 20, 0, -20, -20, 0)
#draw_lines(m, screen, color)
printMatrix(m)
mT = makeTranslationMatrix(250, 250, 0)
m = scalarMultiply(m, 4)
for r in range(40):
	mFi = matrixMultiply(makeZRotationMatrix(r * 11), m)
	mFi = matrixMultiply(mT, mFi)
	drawScreen(mFi, screen, color)
"""m = scalarMultiply(m, 2)
for r in range(5):
	mFi = matrixMultiply(makeZRotationMatrix(r*18), m)
	mFi = matrixMultiply(mT, mFi)
	drawScreen(mFi, screen, [255, 0, 0])
m = scalarMultiply(m, 2)
for r in range(9):
	mFi = matrixMultiply(makeZRotationMatrix(r*10), m)
	mFi = matrixMultiply(mT, mFi)
	drawScreen(mFi, screen, [0, 0, 255])
"""
save_extension(screen,"pic.png")
