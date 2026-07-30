class MinStack(object):

    def __init__(self):
        self.item = []

    def push(self, val):
        if len(self.item) == 0:
            self.item.append([val, val])
        else:
            mini = min(self.item[-1][1], val)
            self.item.append([val, mini])

    def pop(self):
        return self.item.pop()

    def top(self):
        return self.item[-1][0]

    def getMin(self):
        return self.item[-1][1]