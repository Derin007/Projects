cover = 24.95
discount = 0.4
shipping = 3
shipping1 = 0.75
bookCost = cover * discount
n = 60
shippingValue = shipping + (shipping1 * (n-1))
totalCost = shippingValue + bookCost
print(totalCost)





def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I am a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

repeat_lyrics()