import sys

if len(sys.argv) < 3 or int(sys.argv[2]) < 9:
	print("ERROR - Usage is:")
	print("python3 janepuzzleMay.py numToFind numRows")
	print("where numRows is at least 9.")
	sys.exit(1)

# Make at twice as wide because pattern removes 2 horizontal for every 1 down.
# Always uses 3 past the black dividing line, horizontally.
# Therefore, technically for row x, you need 2x-2 columns above.
rows, cols = (int(sys.argv[2]), int(sys.argv[2])*2)
arr = [[0 for i in range(cols)] for j in range(rows)]

# Initial setting of increasing counts in rows
for i in range(rows):
    for j in range(cols):
        arr[i][j] = j + 1 + i

# Problem statement hardcoding
arr[2][0]    = 2
arr[3][0:3]  = [4,6,2]
arr[4][0:5]  = [2,8,6,9,4]
arr[5][0:7]  = [9,10,6,11,8,12,2]
arr[6][0:9]  = [8,2,11,13,6,14,10,15,9]
arr[7][0:11] = [14,15,6,9,13,16,11,17,2,18,8]
arr[8][0:13] = [11,2,16,18,13,8,9,19,6,20,15,21,14]

# Edit rows that need to be changed
for rowIndex in range(9,rows):
    valsToChange = 2 * rowIndex - 3
    yIndex = rowIndex - 2
    yIndex2 = rowIndex
    for colIndex in range(valsToChange):
    	if colIndex % 2 == 0:
    		arr[rowIndex][colIndex] = arr[rowIndex-1][yIndex]
    		yIndex -= 1
    	else:
    		arr[rowIndex][colIndex] = arr[rowIndex-1][yIndex2]
    		yIndex2 += 1

# Print array
for row in arr:
    print(row)
    
# Find the answer
currRow = 1
numToFind = int(sys.argv[1])
print("Searching for: " + str(numToFind))
while currRow <= rows:
	if arr[currRow-1][currRow-1] == numToFind:
		break
	currRow += 1
	
if currRow > rows:
	print("Sorry, could not find " + sys.argv[1] + " in " + sys.argv[2] + " rows.")
else:
	print("FOUND " + sys.argv[1] + " to be in row/col number " + str(currRow) + ".")