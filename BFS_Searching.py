maze = {"A": ["D", "B"], "B": ["A", "C"], "C": ["B", "D", "H", "G"], "D": ["A", "E", "F", "C"], 
        "E": ["D", "I"], "F": ["D", "J"], "G": ["C"], "H": ["C", "L"], "I": ["E", "M", "K", "J"], 
        "J": ["F", "I", "N", "L"], "K": ["I", "N"], "L": ["J", "H", "N"], "N": ["O"], "O": ["N"]
        }
class BFS_Search:
    def __int__(self):
        pass

    def store_data(self, graph, start, goal):
        store_graph = []
        visited_graph = []
        for key in graph.keys():
            if key == start:
                if(self.is_goal(start, goal)):
                    return start, visited_graph, store_graph
                store_graph = self.enqueue(store_graph, start)
                
                break
            
        



    def is_visited(self, arr, value):
        for i in range(len(arr)):
            if(arr[i] == value):
                return True
            
        return False
    
    def is_goal(self, value, goal):
        if(value == goal):
            return True
        return False

    def enqueue(self, arr, new_val):
        new_arr = [None] * (len(arr) + 1)
        for i in range(0, len(arr)):
            new_arr[i] = arr[i]
        new_arr[len(arr)] = new_val
        return new_arr

    def dequeue(self, arr):
        if(self.isEmpty(arr)):
            return arr
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
enqueued = bfs.enqueue(array_val, "E")
print("the dequeued value is: ", dequeued)
print("the enqueued value is: ", enqueued)

maze = {"A": ["D", "B"], "B": ["A", "C"], "C": ["B", "D", "H", "G"], "D": ["A", "E", "F", "C"], 
        "E": ["D", "I"], "F": ["D", "J"], "G": ["C"], "H": ["C", "L"], "I": ["E", "M", "K", "J"], 
        "J": ["F", "I", "N", "L"], "K": ["I", "N"], "L": ["J", "H", "N"], "N": ["O"], "O": ["N"]
        }

print("the maze is: ", maze.get("A"))
for key in maze.keys():
    print("the keys are: ", key)


