# The Python Data model

### Consistency of python 

dunder = under under special method under under

special method = magic method(slang)

e.g. <br/>
`__getitem__` is pronounced dunder getitem <br/>
`__len__` is pronounced dunder len
## Special methods so far
<ol>
    <li>__init__</li>
    <li>__getitem__</li>
    <li>__len__</li>
    <li>__iter__</li>
    <li>__repr__</li>
    <li>__abs__</li>
    <li>__bool__</li>
    <li>__add__</li>
    <li>__mul__</li>
    <li>__str__</li>
</ol>

## HOW Special methods are used

Using built in functions like len, str, iter(indirect via 'for..in' consntruct), reversed

#### Emulating numeric types
#### String representation
#### Arithmetic Operators
#### Boolean value of a custom type

# An Array of Sequences

## Overview of Built-In sequences

### Container sequences
<p> list, tuple, collections.deque </p>

### Flat Sequences
<p> str, bytes, bytearray, _memoryview_ and array.array </p>


# List of interesting built in functions
`ord('A')` <br/>
`chr(65)` <br/>
`map(<function>,[lis_here])` <br/>
`filter(<function>,[list_here])` <br/>

tuple()<br>
list()<br>
divmod(5,2)->(2,1)<br>
range()<br>

collections.namedtuple<br>