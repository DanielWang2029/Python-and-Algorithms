
# Disjoint set have an average O(log(n)) runtime for completing a single find or union operation
# it is good for finding connectivity between points, nodes or any objects
class DisjointSet:

    # we need to initialize a parnets/roots array and a rank array to keep track of their rank/height of the tree
    # if the numbers to be put in is unbounded, we could sort them and use their indexes as input
    def __init__(self, size):
        
        # assuming each start with their own set
        # we can set the initial condition to be empty (None/-1) and add an "self.add(x)" function that initialize each node
        self.parents = [i for i in range(size)]
        
        # the starting rank/size of tree for each node is 1
        self.rank = [1 for _ in range(size)]

    # find the root of a node w/ path compression
    # this takes O(log(n)) on average
    def find(self, x):
        
        # return itself if its the root parent
        if self.parents[x] == x:
            return x
        
        # update all node's parent to the root parent
        self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]

    # union two set/tree according to their rank
    # note that this only changes the parents for two roots, xroot and yroot
    # the parents of x and y does not necessarily change
    # this is ok because the next time we want to find the root of a non-root node
    # pass compression will automatically set their parents to the root parent in O(log(n)) time
    def union(self, x, y):
        
        xroot, yroot = self.find(x), self.find(y)
        
        if xroot == yroot:
            return
        
        # if rank of x < rank of y, meaning the height of y tree is larger than height of x tree
        # assign x as y's parent so that the rank keeps the same/result tree does not change in height
        if self.rank[xroot] < self.rank[yroot]:
            self.parents[xroot] = yroot
            
        # same thing here, assign y's parent to x so that rank does not change
        elif self.rank[xroot] > self.rank[yroot]:
            self.parents[yroot] = xroot
        
        # if they have the same rank, we have to point one to another, resulting in higher rank
        else:
            self.parents[yroot] = xroot
            
            # here we only update xroot because only the rank of root parents matters
            self.rank[xroot] += 1


if __name__ == '__main__':
    
    ds = DisjointSet(5)
    print(ds.parents)  # prints [0, 1, 2, 3, 4]
    
    ds.union(0, 1)
    print(ds.parents)  # prints [0, 0, 2, 3, 4]
    
    ds.union(2, 3)
    print(ds.parents)  # prints [0, 0, 2, 2, 4]
    
    ds.union(1, 3)
    print(ds.parents)  # prints [0, 0, 0, 2, 4]
    
    # only the rank of root parents matters
    print(ds.rank)  # prints [3, 1, 2, 1, 1]
    
    # although union 1 and 3 again does nothing, the parent of 3 is updated to 0 due to path compression
    ds.union(1, 3)
    print(ds.parents)  # prints [0, 0, 0, 0, 4]
    
    print("Done!")
