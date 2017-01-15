

class Heap :
    def __init__(self):
        self.hlist = []
        self.size = 0

    def percolate_up(self,i):
        if i < self.size :
            while i >= 0 :
                if self.hlist[i//2] < self.hlist[i] :
                    self.hlist[i],self.hlist[i//2] = self.hlist[i//2],self.hlist[i]
                i = i//2

    def insert(self,item):
        self.hlist.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_down(self,i):

        while i*2 < self.size :
            _min = self.hlist[i]
            

















