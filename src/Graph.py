class Queue:
    def __init__(self, data):
        self.queue_data = data

    def add(self, element):
        self.queue_data.append(element)

    def get(self):
        return self.queue_data.pop(0)


queue = Queue([])

graph = {"a": ["b", "e"],
         "b": ["a", "c", "d"],
         "c": ["b", "d", "k"],
         "d": ["b", "c"],
         "e": ["a", "k"],
         "k": ["c", "e"]
         }


def width_search(graph, start, find):
    visited = []
    visited.append(start)
    queue.add(start)
    while queue.queue_data:
        element = queue.get()
        elements = graph[element]
        for i in elements:
            if i == find:
                break
            if i not in visited:
                visited.append(i)
                queue.add(i)
    
    for i in visited:
        if find in graph[i] and start in graph[i]:
            path = i
    return path




print(width_search(graph, "a", "d"))


