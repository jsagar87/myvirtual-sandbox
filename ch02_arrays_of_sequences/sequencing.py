import array

# Example of cartesian product using list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                         for size in sizes]
print(type(tshirts[0]))

symbols = '$¢£¥€¤'
# Example of tuple sequence generation using expression
symtuple = tuple(ord(symbol) for symbol in symbols)
# Example of array sequence generation using expression
symarr = array.array('I', (ord(symbol) for symbol in symbols))
print(symtuple)
print(symarr)
