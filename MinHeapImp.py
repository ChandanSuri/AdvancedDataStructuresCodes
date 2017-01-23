class BinHeap:
    # Constructor for initialization..

    def __init__(self):
        self.h_list = [0]
        self.c_size = 0

# To check that Heap is Empty or Not

    def isEmpty(self):
        if self.c_size != 0:
            return False
        else:
            return True
# To move up the element if needed

    def moveUp(self, i):
        while i/2 > 0:
            if self.h_list[i] < self.h_list[i/2]:
                tmp = self.h_list[i]
                self.h_list[i] = self.h_list[i/2]
                self.h_list[i/2] = tmp
            i /= 2
# to insert in a heap and recover heap Property using move Up function

    def insert(self, num):
        self.h_list.append(num)
        self.c_size += 1
        self.moveUp(self.c_size)

    def moveDown(self, i):
        while (i*2) <= self.c_size:
            min_child_index = self.minChild(i)
            if self.h_list[i] > self.h_list[min_child_index]:
                tmp = self.h_list[i]
                self.h_list[i] = self.h_list[min_child_index]
                self.h_list[min_child_index] = tmp
            i = min_child_index
# to find which child is minimum of the two for its parent

    def minChild(self, i):
        if i*2+1 > self.c_size:
            return i*2
        else :
            if self.h_list[i*2] > self.h_list[i*2+1]:
                return i*2+1
            else:
                return i*2
# This is min Heap so minimum element is at the root

    def findMin(self):
        min_val = self.h_list[1]
        return min_val
# To delete the Root that is the minimum element in the Heap or List

    def delMin(self):
        del_val = self.h_list[1]
        self.h_list[1] = self.h_list[self.c_size]
        self.c_size -= 1
        self.h_list.pop()
        self.moveDown(1)
        return del_val
# Building the Heap all at once takes O(n) time..

    def buildHeap(self, l):
        i = len(l) / 2
        self.c_size = len(l)
        self.h_list = [0] + l[:]
        while i>0:
            self.moveDown(i)
            i -= 1

h_obj = BinHeap()  # Object Creation
inp = raw_input("Enter the List that you want to form the heap of: ")
l = [int(x) for x in inp.split()]
h_obj.buildHeap(l)

print "The Heap formed after the operation of insertion is => ", h_obj.h_list
while True:
    i = raw_input("Enter the element to be appended => ")
    if i == "Quit":
        break
    i = int(i)
    h_obj.insert(i)
    print "The New Heap formed is => ", h_obj.h_list
    print "Enter Quit if want to quit the appending process..."

print "Now, the minimum element present in the Heap is => ", h_obj.findMin()
while True:
    del_or_not = raw_input("If You want to delete the minimum element please enter \'Delete\' => ")
    if del_or_not == "Delete" and not(h_obj.isEmpty()):
        h_obj.delMin()
    else:
        break
    print "The Heap at the moment is => ", h_obj.h_list

print "Now Check is done whether the Heap is empty or not??? "
if h_obj.isEmpty():
    print "The heap is Empty..."
else:
    print "The heap is not Empty..."

print "Ending............"





