# PyHaskell
Rewriting Haskell modules and libraries in Python.

Let's start with prelude!

Reference the builtins from the `builtins` module:

``` python
import builtins

def all(fn, a) -> bool:
    """all :: Foldable t => (a -> Bool) -> t a -> Bool
    """
    return builtins.all(fn(i) for i in a)
```

Let's keep them in order that we get them from 
the following command:

``` haskell
Prelude> :browse Prelude
```

Functions that aren't legal python names 
(keywords or symbols) should get a
name that uses a short nickname for it.

- bang means !
- hat means ^
- cash means $
- ampersand means & (unless we can get away with and)

For example:

``` python
def bangbang(list_of_a, integer) -> 'a':
    """(!!) :: [a] -> Int -> a
    """    
```
