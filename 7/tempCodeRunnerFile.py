    def propagate_gold(self):
        if not self.contains_gold or self.color == "shiny gold":
            self.contains_gold = True
            for i in self.parents:
                i.propagate_gold()