class Gtree:
    def __init__(self, func):
        self.func = func
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def execute(self, number):
        results = [self.func(number)]
        for child in self.children:
            results += child.execute(results[-1])
        return results

def square(n):
    return n * n

def subtract_one(n):
    return n - 1

root = Gtree(square)
node1 = Gtree(subtract_one)


root.add(node1)
root.add(node2)
number = 5
res = root.execute(number)
print(res) 