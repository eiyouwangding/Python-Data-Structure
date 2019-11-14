    #-------------------------- recitation 9 functions --------------------------

    def minimum(self):
        return self.first().element()
    
    def second_minimum(self):
        return self.after(self.first()).element()
    
    def is_valid(self):
        prev = self.first().element()
        for i in self:   # calls inorder()
            if i < prev:
                return False
            prev = i
        return True 
    
    def iter_range(self, start, stop):
        for i in self:  # calls inorder()
            if start <= i < stop:
                yield i

