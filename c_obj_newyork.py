class American:
    pass

class NewYorker(American):
    pass

obj = NewYorker()
print(isinstance(obj, NewYorker))
print(isinstance(obj, American))