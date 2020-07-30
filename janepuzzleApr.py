import copy
import sys

class Dot:
    def __init__(self,  connected, bottomLeft=None, bottomRight=None, right=None):
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        self.right = right
        self.connected = connected

class Graph:
    def __init__(self, size):
        self.dots = []
        for i in range(size, 0, -1):
            tempList = []
            # Top Dot
            if i == 1:
                tempDot = Dot(False)
                tempDot.bottomRight = self.dots[0][1]
                tempDot.bottomLeft = self.dots[0][0]
                tempList.append(tempDot)
            # Bottom Row
            elif i == size:
                for j in range(i, 0, -1):
                    tempDot = Dot(False)
                    if j != i:
                        tempDot.right = tempList[0]
                    tempList.insert(0, tempDot)
            # All middle rows
            else:
                for j in range(i, 0, -1):
                    tempDot = Dot(False)
                    tempDot.bottomRight = self.dots[0][j]
                    tempDot.bottomLeft = self.dots[0][j-1]
                    if j != i:
                        tempDot.right = tempList[0]
                    tempList.insert(0, tempDot)

            self.dots.insert(0, tempList)

    def __str__(self):
        dotties = self.dots
        ret = ""
        for list in dotties:
            ret += "Next Tier\n"
            for item in list:
                ret += "item: " + str(item) + ", BL: " + str(item.bottomLeft)  + ", BR: " + str(item.bottomRight) + ", R: " + str(item.right) + ", C: " + str(item.connected) + "\n"
        return ret


def allConnected(g):
    for list in g.dots:
        for dot in list:
            if dot.connected == False:
                return False
    return True


def canConnectAll(g):
    if allConnected(g):
        return True
    else:
        result = False
        # Get dot to connect
        tempDot = g.dots[0][0]
        i = 0
        j = 0
        while(tempDot.connected == True):
            if i == j:
                i += 1
                j = 0
            else:
                j += 1
            tempDot = g.dots[i][j]

        # Make copies and recurse with new possible connections

        # Right and bottom right
        if (tempDot.right != None and tempDot.bottomRight != None and tempDot.right.connected == False and tempDot.bottomRight.connected == False):
            # Try each type of connection, recursing
            tempGraph = copy.deepcopy(g)
            dotToConnect = tempGraph.dots[i][j]
            # Connect dots
            dotToConnect.connected = True
            dotToConnect.bottomRight.connected = True
            dotToConnect.right.connected = True
            result = canConnectAll(tempGraph)
        # Bottom left and bottom right
        if (result == False and tempDot.bottomLeft != None and tempDot.bottomRight != None and tempDot.bottomLeft.connected == False and tempDot.bottomRight.connected == False):
            # Connect to bottom left and bottom bottom right
            tempGraph = copy.deepcopy(g)
            dotToConnect = tempGraph.dots[i][j]
            # Connect dots
            dotToConnect.connected = True
            dotToConnect.bottomLeft.connected = True
            dotToConnect.bottomRight.connected = True
            result = canConnectAll(tempGraph)

        return result


# Test print out a graph
graph = Graph(int(sys.argv[1]))
print(canConnectAll(graph))
