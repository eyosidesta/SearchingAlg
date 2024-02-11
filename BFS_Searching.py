maze = {"A": ["D", "B"], "B": ["A", "C"], "C": ["B", "D", "H", "G"], "D": ["A", "E", "F", "C"], 
        "E": ["D", "I"], "F": ["D", "J"], "G": ["C"], "H": ["C", "L"], "I": ["E", "M", "K", "J"], 
        "J": ["F", "I", "N", "L"], "K": ["I", "N"], "L": ["J", "H", "N"], "N": ["O"], "O": ["N"]
        }
class BFS_Search:
    def __int__(self):
        pass

    def enqueue(self, arr):
        pass

    def dequeue(self, arr):
        if(self.isEmpty(arr)):
            return arr
        # Object new_arr = new object[]

        new_arr = [None] * (len(arr) - 1)
        print("the len: ", len(new_arr))
        for i in range(1, len(arr)):
            new_arr[i-1] = arr[i]
        return new_arr

    def isEmpty(self, arr):
        if(len(arr) == 0):
            return True
        return False
    

array_val = ["A", "B", "C", "D"]

bfs = BFS_Search()
dequeued = bfs.dequeue(array_val)
print("the dequeued value is: ", dequeued)


