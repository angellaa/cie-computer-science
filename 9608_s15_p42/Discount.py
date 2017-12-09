
def Discount(GoodsTotal, HasDiscountCard):
    if GoodsTotal > 100 and HasDiscountCard:
        return 10

    if GoodsTotal > 100 or HasDiscountCard:
        return 5

    return 0

print(Discount(20, False))
print(Discount(25, False))
print(Discount(80, True))
print(Discount(120, False))
print(Discount(120, True))
