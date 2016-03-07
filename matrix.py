import math

def makeTranslationMatrix( x, y, z ):
	m = makeNewMatrix()
	for c in range(len(m)):
		m[c][c] = 1
	m[3][0] = x
	m[3][1] = y
	m[3][2] = z
	return m

def makeScalingMatrix( x, y, z ):
	m = makeNewMatrix()
	#for r in range (len(m)):
		#m[r][3] = 1
	m[3][3] = 1
	m[0][0] = x
	m[1][1] = y
	m[2][2] = z
	return m

def makeXRotationMatrix( theta ):#center 
	m = makeIdentityMatrix()
	m[1][1] = math.cos(math.radians(theta))
	m[1][2] = -1*math.sin(math.radians(theta))
	m[2][1] = math.sin(math.radians(theta))
	m[2][2] = math.cos(math.radians(theta))
	return m

def makeYRotationMatrix( theta ): #000 02 20 22
	m = makeIdentityMatrix()
	m[0][0] = math.cos(math.radians(theta))
	m[0][2] = -1*math.sin(math.radians(theta))
	m[2][0] = math.sin(math.radians(theta))
	m[2][2] = math.cos(math.radians(theta))
	return m

def makeZRotationMatrix( theta ):# cos -sin sin cos top left
	m = makeIdentityMatrix()
	m[0][0] = math.cos(math.radians(theta))
	m[0][1] = -1*math.sin(math.radians(theta))
	m[1][0] = math.sin(math.radians(theta))
	m[1][1] = math.cos(math.radians(theta))
	return m


def makeNewMatrix(rows = 4, cols = 4):
	m = []
	for c in range( cols ):
		m.append( [] )
		for r in range( rows ):
			m[c].append( 0 )
	return m

def printMatrix( matrix ):
	thing = ""
	for r in range(len(matrix[0])):
		thing+="|"
		for c in range(len(matrix)):
			thing+=" "
			thing+=str(matrix[c][r])
		thing+=" |\n"
	print thing


def scalarMultiply( matrix, x ):
	return matrixMultiply(makeScalingMatrix(x, x, x), matrix)


def matrixMultiply( m1, m2 ):
	if len(m1) != len(m2[0]):
		pass
	mf = makeNewMatrix(len(m1[0]), len(m2))
	item = 0
	for c in range(len(m2)):
		for r in range(4):
			for i in range(4):
				item += m1[i][r] * m2[c][i]
			mf[c][r] = item
			item = 0
	return mf
def makeIdentityMatrix(rows = 4, cols = 4):
        m = makeNewMatrix(rows, cols);
        for c in range(cols):
                for r in range(rows):
                        if r == c:
                                m[c][r] = 1;
        return m;
