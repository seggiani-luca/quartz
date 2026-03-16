# Define a TypedList class inheriting from the built-in class list. A type must 
# be defined at creation. Override the append method so that only objects of 
# the same type can be appended

class TypedList(list):
    def __init__(self, typ):
        self.typ = typ

    def append(self, elem):
        if type(elem) != self.typ:
            return
        super().append(elem)

typ_list = TypedList(float)

typ_list.append(0.1)
typ_list.append(0.2)
typ_list.append("gatto")
typ_list.append(3)

print(typ_list)
