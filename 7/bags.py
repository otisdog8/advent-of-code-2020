instuff = open("bags.in", "r")
instuff1 = instuff.readlines()

bags = {}


class Bag:
    def __init__(self, color):
        self.color = color
        self.contains_gold = False
        self.parents = []
        self.children = []
        self.containedchildren = []

    def propagate_gold(self):
        if not self.contains_gold or self.color == "shiny gold":
            self.contains_gold = True
            for i in self.parents:
                i.propagate_gold()

    def add_child(self, child):
        if child.contains_gold:
            self.propagate_gold()


class BagContainer:
    def __init__(self, bag, number):
        self.bag = bag
        self.number = number

    def count_bag(self):
        if len(self.bag.containedchildren) == 0:
            return 1
        else:
            bags = 0
            for i in self.bag.containedchildren:
                bags += i.count_bag() * i.number
            return bags + 1


for i in instuff1:
    j = i.split(" bags contain ")
    parent = 0
    if j[0] not in bags:
        parent = Bag(j[0])
        bags[j[0]] = parent
        print("New parent ", parent.color)
    else:
        parent = bags[j[0]]
    if "no other bags." in j[1]:
        pass
    else:
        k = j[1].split(", ")
        childs = []
        for l in k:
            l = l.split(" ")
            child = l[1] + " " + l[2]
            childx = 0
            if child not in bags:
                print("New child ", child)
                childx = Bag(child)
                bags[child] = childx
            else:
                childx = bags[child]
            parent.add_child(childx)
            childx.parents.append(parent)
            parent.containedchildren.append(BagContainer(childx, int(l[0])))
            if childx.color == "shiny gold":
                childx.propagate_gold()

result = 0
for i in bags.values():
    if i.contains_gold and i.color != "shiny gold":
        result += 1
        print(i.color)

print(BagContainer(bags["shiny gold"], 1).count_bag())
print(result)