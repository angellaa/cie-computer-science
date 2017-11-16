#
#  Variables:
#  - i: integer
#

PCode = list(range(0, 1000))

def ProductCodeSearch(SearchCode):

    for i in range(0, 1000):
        if SearchCode == PCode[i]:
            return i

    return -1

print(ProductCodeSearch(-20))
