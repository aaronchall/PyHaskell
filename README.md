# PyHaskell
Rewriting Haskell modules and libraries in Python.

We care about the function signatures, not the implementation.
For example, consider a function in Haskell that operates on 
what is semantically a list, taking other arguments, and
then returns a list. 

We don't care how Haskell did it. We'll do the
correct semantic thing for Python.

Let's start with Prelude!

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
