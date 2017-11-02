class Node:
    def __init__(self, data, pointer):
        self._data = data
        self._pointer = pointer

    def setData(self, data):
        self._data = data

    def setPointer(self, pointer):
        self._pointer = pointer

    def getData(self):
        return self._data

    def getPointer(self):
        return self._pointer

class LinkedList:
    def __init__(self):
        self._headPointer = -1
        self._freeListPointer = 0
        self._nodeArray = []

        for i in range(8):
            node = Node("", i + 1)
            self._nodeArray.append(node)

        self._nodeArray[7].setPointer(-1)

    def outputListToConsole(self):
        pointer = self._headPointer

        while pointer != -1:
            print(self._nodeArray[pointer].getData())
            pointer = self._nodeArray[pointer].getPointer()

        print()

    # add at the end
    def findInsertionPoint(self, data):
        previousPointer = -1
        pointer = self._headPointer

        while pointer != -1:
            previousPointer = pointer
            pointer = self._nodeArray[pointer].getPointer()

        return previousPointer, pointer

    def addToList(self, data):
        newNodePointer = self._freeListPointer
        self._nodeArray[newNodePointer].setData(data)
        self._freeListPointer = self._nodeArray[self._freeListPointer].getPointer()

        if self._headPointer == -1:
            self._headPointer = newNodePointer
            self._nodeArray[newNodePointer].setPointer(-1)
        else:
            previousPointer, nextPointer = self.findInsertionPoint(data)
            if previousPointer == -1:
                self._nodeArray[newNodePointer].setPointer(self._headPointer)
                self._headPointer = newNodePointer
            else:
                self._nodeArray[newNodePointer].setPointer(nextPointer)
                self._nodeArray[previousPointer].setPointer(newNodePointer)

def main():
    linkedList = LinkedList()
    linkedList.addToList("Andrea")
    linkedList.addToList("Tom")
    linkedList.addToList("Mark")

    linkedList.outputListToConsole()

if __name__ == '__main__':
    main()
