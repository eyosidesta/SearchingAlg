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
                get_child = graph.get(key)
                store_graph, visited_value = self.dequeue(store_graph)
                visited_graph = self.enqueue(visited_graph, visited_value)
                store_graph = self.enqueue_array(store_graph, get_child)
                break
        goal_value, new_store_graph, new_visited_graph = self.apply_bfs(store_graph, visited_graph, graph, goal)
        return goal_value, new_store_graph, new_visited_graph
    
    def apply_bfs(self, store_graph, visited_graph, graph, goal):
        store_graph, visited_value = self.dequeue(store_graph)
        visited_graph = self.enqueue(visited_graph, visited_value)
        get_child = graph.get(visited_value)
        if(get_child):
            for i in range(len(get_child)):
                if(get_child[i] == goal):
                    return goal, store_graph, visited_graph
                if(not(self.is_visited(visited_graph, get_child[i]))):
                    store_graph = self.enqueue(store_graph, get_child[i])
        return self.apply_bfs(store_graph, visited_graph, graph, goal)


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
    
    def enqueue_array(self, arr, add_arr):
        new_arr = [None] * (len(arr) + len(add_arr))
        for i in range(0, len(arr)):
            new_arr[i] = arr[i]
        for j in range(len(add_arr)):
            new_arr[len(arr) + j] = add_arr[j]
        return new_arr

    def dequeue(self, arr):
        if(self.isEmpty(arr)):
            return arr
        new_arr = [None] * (len(arr) - 1)
        dequeued_value = arr[0]
        for i in range(1, len(arr)):
            new_arr[i-1] = arr[i]
        return new_arr, dequeued_value

    def isEmpty(self, arr):
        if(len(arr) == 0):
            return True
        return False
    
bfs = BFS_Search()

maze = {"A": ["D", "B"], "B": ["A", "C"], "C": ["B", "D", "H", "G"], "D": ["A", "E", "F", "C"], 
        "E": ["D", "I"], "F": ["D", "J"], "G": ["C"], "H": ["C", "L"], "I": ["E", "M", "K", "J"], 
        "J": ["F", "I", "N", "L"], "K": ["I", "N"], "L": ["J", "H", "N"], "N": ["O"], "O": ["N"]
        }


goal, stored_data, visited_graph = bfs.store_data(maze, "A", "O")

print("the goal is: ", goal)
print("the visited graph is: ", visited_graph)


