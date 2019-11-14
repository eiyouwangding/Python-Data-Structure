class SimpleTree:
    def __init__(self, element, left=None, right=None, parent=None):
        self._element = element
        self._left = left
        self._right = right
        self._parent = parent

    def __str__(self):
        return str(self._element)
