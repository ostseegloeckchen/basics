#Definition einer eigenen Klasse, hier die Klasse "Const"
#mit privaten Attributen über "property"

class Const(object):
    def __init__(self,x):
        self.__x=x

    def get_X(self):
        return self.__x

    x=property(get_X)

k=Const(100)
print(k.x)

print()

k.x=101
