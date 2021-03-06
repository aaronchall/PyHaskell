"""
The goal of this module is to write all 
the Prelude functions (and maybe types?) in Python

Prelude> :browse Prelude
(!!) :: [a] -> Int -> a
($) :: (a -> b) -> a -> b
($!) :: (a -> b) -> a -> b
(&&) :: Bool -> Bool -> Bool
(++) :: [a] -> [a] -> [a]
(.) :: (b -> c) -> (a -> b) -> a -> c
(<$>) :: Functor f => (a -> b) -> f a -> f b
(=<<) :: Monad m => (a -> m b) -> m a -> m b
class Functor f => Applicative (f :: * -> *) where
  pure :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b
  (*>) :: f a -> f b -> f b
  (<*) :: f a -> f b -> f a
data Bool = False | True
class Bounded a where
  minBound :: a
  maxBound :: a
data Char = GHC.Types.C# GHC.Prim.Char#
data Double = GHC.Types.D# GHC.Prim.Double#
data Either a b = Left a | Right b
class Enum a where
  succ :: a -> a
  pred :: a -> a
  toEnum :: Int -> a
  fromEnum :: a -> Int
  enumFrom :: a -> [a]
  enumFromThen :: a -> a -> [a]
  enumFromTo :: a -> a -> [a]
  enumFromThenTo :: a -> a -> a -> [a]
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
type FilePath = String
data Float = GHC.Types.F# GHC.Prim.Float#
class Fractional a => Floating a where
  pi :: a
  exp :: a -> a
  log :: a -> a
  sqrt :: a -> a
  (**) :: a -> a -> a
  logBase :: a -> a -> a
  sin :: a -> a
  cos :: a -> a
  tan :: a -> a
  asin :: a -> a
  acos :: a -> a
  atan :: a -> a
  sinh :: a -> a
  cosh :: a -> a
  tanh :: a -> a
  asinh :: a -> a
  acosh :: a -> a
  atanh :: a -> a
class Foldable (t :: * -> *) where
  Data.Foldable.fold :: Monoid m => t m -> m
  foldMap :: Monoid m => (a -> m) -> t a -> m
  foldr :: (a -> b -> b) -> b -> t a -> b
  Data.Foldable.foldr' :: (a -> b -> b) -> b -> t a -> b
  foldl :: (b -> a -> b) -> b -> t a -> b
  Data.Foldable.foldl' :: (b -> a -> b) -> b -> t a -> b
  foldr1 :: (a -> a -> a) -> t a -> a
  foldl1 :: (a -> a -> a) -> t a -> a
  Data.Foldable.toList :: t a -> [a]
  null :: t a -> Bool
  length :: t a -> Int
  elem :: Eq a => a -> t a -> Bool
  maximum :: Ord a => t a -> a
  minimum :: Ord a => t a -> a
  sum :: Num a => t a -> a
  product :: Num a => t a -> a
class Num a => Fractional a where
  (/) :: a -> a -> a
  recip :: a -> a
  fromRational :: Rational -> a
class Functor (f :: * -> *) where
  fmap :: (a -> b) -> f a -> f b
  (<$) :: a -> f b -> f a
newtype IO a
  = GHC.Types.IO (GHC.Prim.State# GHC.Prim.RealWorld
                  -> (# GHC.Prim.State# GHC.Prim.RealWorld, a #))
type IOError = GHC.IO.Exception.IOException
data Int = GHC.Types.I# GHC.Prim.Int#
data Integer
  = integer-gmp-1.0.0.0:GHC.Integer.Type.S# !GHC.Prim.Int#
  | integer-gmp-1.0.0.0:GHC.Integer.Type.Jp# {-# UNPACK #-}integer-gmp-1.0.0.0:GHC.Integer.Type.BigNat
  | integer-gmp-1.0.0.0:GHC.Integer.Type.Jn# {-# UNPACK #-}integer-gmp-1.0.0.0:GHC.Integer.Type.BigNat
class (Real a, Enum a) => Integral a where
  quot :: a -> a -> a
  rem :: a -> a -> a
  div :: a -> a -> a
  mod :: a -> a -> a
  quotRem :: a -> a -> (a, a)
  divMod :: a -> a -> (a, a)
  toInteger :: a -> Integer
data Maybe a = Nothing | Just a
class Applicative m => Monad (m :: * -> *) where
  (>>=) :: m a -> (a -> m b) -> m b
  (>>) :: m a -> m b -> m b
  return :: a -> m a
  fail :: String -> m a
class Monoid a where
  mempty :: a
  mappend :: a -> a -> a
  mconcat :: [a] -> a
class Num a where
  (+) :: a -> a -> a
  (-) :: a -> a -> a
  (*) :: a -> a -> a
  negate :: a -> a
  abs :: a -> a
  signum :: a -> a
  fromInteger :: Integer -> a
class Eq a => Ord a where
  compare :: a -> a -> Ordering
  (<) :: a -> a -> Bool
  (<=) :: a -> a -> Bool
  (>) :: a -> a -> Bool
  (>=) :: a -> a -> Bool
  max :: a -> a -> a
  min :: a -> a -> a
data Ordering = LT | EQ | GT
type Rational = GHC.Real.Ratio Integer
class Read a where
  readsPrec :: Int -> ReadS a
  readList :: ReadS [a]
  GHC.Read.readPrec :: Text.ParserCombinators.ReadPrec.ReadPrec a
  GHC.Read.readListPrec ::
    Text.ParserCombinators.ReadPrec.ReadPrec [a]
type ReadS a = String -> [(a, String)]
class (Num a, Ord a) => Real a where
  toRational :: a -> Rational
class (RealFrac a, Floating a) => RealFloat a where
  floatRadix :: a -> Integer
  floatDigits :: a -> Int
  floatRange :: a -> (Int, Int)
  decodeFloat :: a -> (Integer, Int)
  encodeFloat :: Integer -> Int -> a
  exponent :: a -> Int
  significand :: a -> a
  scaleFloat :: Int -> a -> a
  isNaN :: a -> Bool
  isInfinite :: a -> Bool
  isDenormalized :: a -> Bool
  isNegativeZero :: a -> Bool
  isIEEE :: a -> Bool
  atan2 :: a -> a -> a
class (Real a, Fractional a) => RealFrac a where
  properFraction :: Integral b => a -> (b, a)
  truncate :: Integral b => a -> b
  round :: Integral b => a -> b
  ceiling :: Integral b => a -> b
  floor :: Integral b => a -> b
class Show a where
  showsPrec :: Int -> a -> ShowS
  show :: a -> String
  showList :: [a] -> ShowS
type ShowS = String -> String
type String = [Char]
class (Functor t, Foldable t) => Traversable (t :: * -> *) where
  traverse :: Applicative f => (a -> f b) -> t a -> f (t b)
  sequenceA :: Applicative f => t (f a) -> f (t a)
  mapM :: Monad m => (a -> m b) -> t a -> m (t b)
  sequence :: Monad m => t (m a) -> m (t a)
data Word = GHC.Types.W# GHC.Prim.Word#
(^) :: (Num a, Integral b) => a -> b -> a
(^^) :: (Fractional a, Integral b) => a -> b -> a
all :: Foldable t => (a -> Bool) -> t a -> Bool
and :: Foldable t => t Bool -> Bool
any :: Foldable t => (a -> Bool) -> t a -> Bool
appendFile :: FilePath -> String -> IO ()
asTypeOf :: a -> a -> a
break :: (a -> Bool) -> [a] -> ([a], [a])
concat :: Foldable t => t [a] -> [a]
concatMap :: Foldable t => (a -> [b]) -> t a -> [b]
const :: a -> b -> a
curry :: ((a, b) -> c) -> a -> b -> c
cycle :: [a] -> [a]
drop :: Int -> [a] -> [a]
dropWhile :: (a -> Bool) -> [a] -> [a]
either :: (a -> c) -> (b -> c) -> Either a b -> c
error :: [Char] -> a
even :: Integral a => a -> Bool
filter :: (a -> Bool) -> [a] -> [a]
flip :: (a -> b -> c) -> b -> a -> c
fromIntegral :: (Integral a, Num b) => a -> b
fst :: (a, b) -> a
gcd :: Integral a => a -> a -> a
getChar :: IO Char
getContents :: IO String
getLine :: IO String
head :: [a] -> a
id :: a -> a
init :: [a] -> [a]
interact :: (String -> String) -> IO ()
ioError :: IOError -> IO a
iterate :: (a -> a) -> a -> [a]
last :: [a] -> a
lcm :: Integral a => a -> a -> a
lex :: ReadS String
lines :: String -> [String]
lookup :: Eq a => a -> [(a, b)] -> Maybe b
map :: (a -> b) -> [a] -> [b]
mapM_ :: (Foldable t, Monad m) => (a -> m b) -> t a -> m ()
maybe :: b -> (a -> b) -> Maybe a -> b
not :: Bool -> Bool
notElem :: (Foldable t, Eq a) => a -> t a -> Bool
odd :: Integral a => a -> Bool
or :: Foldable t => t Bool -> Bool
otherwise :: Bool
print :: Show a => a -> IO ()
putChar :: Char -> IO ()
putStr :: String -> IO ()
putStrLn :: String -> IO ()
read :: Read a => String -> a
readFile :: FilePath -> IO String
readIO :: Read a => String -> IO a
readLn :: Read a => IO a
readParen :: Bool -> ReadS a -> ReadS a
reads :: Read a => ReadS a
realToFrac :: (Real a, Fractional b) => a -> b
repeat :: a -> [a]
replicate :: Int -> a -> [a]
reverse :: [a] -> [a]
scanl :: (b -> a -> b) -> b -> [a] -> [b]
scanl1 :: (a -> a -> a) -> [a] -> [a]
scanr :: (a -> b -> b) -> b -> [a] -> [b]
scanr1 :: (a -> a -> a) -> [a] -> [a]
seq :: a -> b -> b
sequence_ :: (Foldable t, Monad m) => t (m a) -> m ()
showChar :: Char -> ShowS
showParen :: Bool -> ShowS -> ShowS
showString :: String -> ShowS
shows :: Show a => a -> ShowS
snd :: (a, b) -> b
span :: (a -> Bool) -> [a] -> ([a], [a])
splitAt :: Int -> [a] -> ([a], [a])
subtract :: Num a => a -> a -> a
tail :: [a] -> [a]
take :: Int -> [a] -> [a]
takeWhile :: (a -> Bool) -> [a] -> [a]
uncurry :: (a -> b -> c) -> (a, b) -> c
undefined :: a
unlines :: [String] -> String
until :: (a -> Bool) -> (a -> a) -> a -> a
unwords :: [String] -> String
unzip :: [(a, b)] -> ([a], [b])
unzip3 :: [(a, b, c)] -> ([a], [b], [c])
userError :: String -> IOError
words :: String -> [String]
writeFile :: FilePath -> String -> IO ()
zip :: [a] -> [b] -> [(a, b)]
zip3 :: [a] -> [b] -> [c] -> [(a, b, c)]
zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith3 :: (a -> b -> c -> d) -> [a] -> [b] -> [c] -> [d]
(||) :: Bool -> Bool -> Bool
"""

import builtins


def index(list_of_a, integer) -> 'a':
    """(!!) :: [a] -> Int -> a
    "bang-bang" - get by index (zero based)
    """
    return list_of_a[integer]
  
def apply(fn, *args) -> 'b':
    """($) :: (a -> b) -> a -> b
    ($)                     :: (a -> b) -> a -> b
    f $ x                   =  f x
    application operator - useful because Haskell applies 
    fn a b
    like python: fn(a, b)
    but sometimes we want haskell to do fn(a(b)), and apply lets us write it:
    fn $ a b
    f $ g $ h x  =  f (g (h x))
    """
    return fn(*args)

def applystrict(fn, *args) -> 'b':
    """($!) :: (a -> b) -> a -> b
    According to Stack Overflow - strict function application.
    Starts to evaluate arguments *before* calling the function.
    Haskell source says:
    -- | Strict (call-by-value) application operator. It takes a function and an
    -- argument, evaluates the argument to weak head normal form (WHNF), then calls
    -- the function with that value.
    
    ($!)                    :: (a -> b) -> a -> b
    f $! x                  = let !vx = x in f vx  -- see #2273
    Perhaps it allows us to treat functions as arguments?
    Haskell wiki says:
    
    "An expression is in weak head normal form (WHNF), if it is either:

    - a constructor (eventually applied to arguments) like True, Just (square 42) or (:) 1
    - a built-in function applied to too few arguments (perhaps none) like (+) 2 or sqrt.
    - or a lambda abstraction \x -> expression."
    Since Python treats functions as objects until called, maybe this is the same as cash
    or maybe we should return it as a partial application that would require being called?
    """
    return cash(fn, *args) # since Python does strict evaluation
    
def andand(a_bool, another_bool) -> bool:
    """(&&) :: Bool -> Bool -> Bool
    since Python treats all objects as booleans 
    and `and` returns the first thing if false and the second if true
    this is simply:
    """
    return bool(a_bool and another_bool)

def concat(list_of_as, another_list_of_as):
    """(++) :: [a] -> [a] -> [a]
    Append. list concatenation, Python uses the `+` operator
    this is also for strings, in Haskell a list of chars, so same for Python as well.
    """
    return list_of_as + another_list_of_as

def compose(fn_b_c, fn_a_b, a) -> 'c':
    """(.) :: (b -> c) -> (a -> b) -> a -> c
    (.) f g = \x -> f (g x)
    f . g x
    also called "dot". Haskel uses infix.
    """
    return fn_b_c(fn_a_b(a))

def infix_fmap():
    """(<$>) :: Functor f => (a -> b) -> f a -> f b
    An infix synonym for fmap.

    The name of this operator is an allusion to $. Note the similarities between their types:

     ($)  ::              (a -> b) ->   a ->   b
    (<$>) :: Functor f => (a -> b) -> f a -> f b

    Whereas $ is function application, <$> is function application lifted over a Functor.
    "the applicative"
    """

def leftbind(fn, a_list):
    """(=<<) :: Monad m => (a -> m b) -> m a -> m b
    (=<<) :: Monad m => (a -> m b) -> m a -> m b infixr 1

    Same as >>=, but with the arguments interchanged.
    """
    return (fn(a) for a in a_list)
    
class Functor f => Applicative (f :: * -> *) where
  pure :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b
  (*>) :: f a -> f b -> f b
  (<*) :: f a -> f b -> f a
data Bool = False | True
class Bounded a where
  minBound :: a
  maxBound :: a
data Char = GHC.Types.C# GHC.Prim.Char#
data Double = GHC.Types.D# GHC.Prim.Double#
data Either a b = Left a | Right b
class Enum a where
  succ :: a -> a
  pred :: a -> a
  toEnum :: Int -> a
  fromEnum :: a -> Int
  enumFrom :: a -> [a]
  enumFromThen :: a -> a -> [a]
  enumFromTo :: a -> a -> [a]
  enumFromThenTo :: a -> a -> a -> [a]
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
type FilePath = String
data Float = GHC.Types.F# GHC.Prim.Float#
class Fractional a => Floating a where
  pi :: a
  exp :: a -> a
  log :: a -> a
  sqrt :: a -> a
  (**) :: a -> a -> a
  logBase :: a -> a -> a
  sin :: a -> a
  cos :: a -> a
  tan :: a -> a
  asin :: a -> a
  acos :: a -> a
  atan :: a -> a
  sinh :: a -> a
  cosh :: a -> a
  tanh :: a -> a
  asinh :: a -> a
  acosh :: a -> a
  atanh :: a -> a
class Foldable (t :: * -> *) where
  Data.Foldable.fold :: Monoid m => t m -> m
  foldMap :: Monoid m => (a -> m) -> t a -> m
  foldr :: (a -> b -> b) -> b -> t a -> b
  Data.Foldable.foldr' :: (a -> b -> b) -> b -> t a -> b
  foldl :: (b -> a -> b) -> b -> t a -> b
  Data.Foldable.foldl' :: (b -> a -> b) -> b -> t a -> b
  foldr1 :: (a -> a -> a) -> t a -> a
  foldl1 :: (a -> a -> a) -> t a -> a
  Data.Foldable.toList :: t a -> [a]
  null :: t a -> Bool
  length :: t a -> Int
  elem :: Eq a => a -> t a -> Bool
  maximum :: Ord a => t a -> a
  minimum :: Ord a => t a -> a
  sum :: Num a => t a -> a
  product :: Num a => t a -> a
class Num a => Fractional a where
  (/) :: a -> a -> a
  recip :: a -> a
  fromRational :: Rational -> a
class Functor (f :: * -> *) where
  fmap :: (a -> b) -> f a -> f b
  (<$) :: a -> f b -> f a
newtype IO a
  = GHC.Types.IO (GHC.Prim.State# GHC.Prim.RealWorld
                  -> (# GHC.Prim.State# GHC.Prim.RealWorld, a #))
type IOError = GHC.IO.Exception.IOException
data Int = GHC.Types.I# GHC.Prim.Int#
data Integer
  = integer-gmp-1.0.0.0:GHC.Integer.Type.S# !GHC.Prim.Int#
  | integer-gmp-1.0.0.0:GHC.Integer.Type.Jp# {-# UNPACK #-}integer-gmp-1.0.0.0:GHC.Integer.Type.BigNat
  | integer-gmp-1.0.0.0:GHC.Integer.Type.Jn# {-# UNPACK #-}integer-gmp-1.0.0.0:GHC.Integer.Type.BigNat
class (Real a, Enum a) => Integral a where
  quot :: a -> a -> a
  rem :: a -> a -> a
  div :: a -> a -> a
  mod :: a -> a -> a
  quotRem :: a -> a -> (a, a)
  divMod :: a -> a -> (a, a)
  toInteger :: a -> Integer
data Maybe a = Nothing | Just a
class Applicative m => Monad (m :: * -> *) where
                    
def bind():
    """  (>>=) :: m a -> (a -> m b) -> m b
    The list monad operations are traditionally 
    described in terms of concatMap:
    xs >>= f = concatMap f xs
    """
                    
  (>>) :: m a -> m b -> m b
  return :: a -> m a
  fail :: String -> m a
class Monoid a where
  mempty :: a
  mappend :: a -> a -> a
  mconcat :: [a] -> a
class Num a where
  (+) :: a -> a -> a
  (-) :: a -> a -> a
  (*) :: a -> a -> a
  negate :: a -> a
  abs :: a -> a
  signum :: a -> a
  fromInteger :: Integer -> a
class Eq a => Ord a where
  compare :: a -> a -> Ordering
  (<) :: a -> a -> Bool
  (<=) :: a -> a -> Bool
  (>) :: a -> a -> Bool
  (>=) :: a -> a -> Bool
  max :: a -> a -> a
  min :: a -> a -> a
data Ordering = LT | EQ | GT
type Rational = GHC.Real.Ratio Integer
class Read a where
  readsPrec :: Int -> ReadS a
  readList :: ReadS [a]
  GHC.Read.readPrec :: Text.ParserCombinators.ReadPrec.ReadPrec a
  GHC.Read.readListPrec ::
    Text.ParserCombinators.ReadPrec.ReadPrec [a]
type ReadS a = String -> [(a, String)]
class (Num a, Ord a) => Real a where
  toRational :: a -> Rational
class (RealFrac a, Floating a) => RealFloat a where
  floatRadix :: a -> Integer
  floatDigits :: a -> Int
  floatRange :: a -> (Int, Int)
  decodeFloat :: a -> (Integer, Int)
  encodeFloat :: Integer -> Int -> a
  exponent :: a -> Int
  significand :: a -> a
  scaleFloat :: Int -> a -> a
  isNaN :: a -> Bool
  isInfinite :: a -> Bool
  isDenormalized :: a -> Bool
  isNegativeZero :: a -> Bool
  isIEEE :: a -> Bool
  atan2 :: a -> a -> a
class (Real a, Fractional a) => RealFrac a where
  properFraction :: Integral b => a -> (b, a)
  truncate :: Integral b => a -> b
  round :: Integral b => a -> b
  ceiling :: Integral b => a -> b
  floor :: Integral b => a -> b
class Show a where
  showsPrec :: Int -> a -> ShowS
  show :: a -> String
  showList :: [a] -> ShowS
type ShowS = String -> String
type String = [Char]
class (Functor t, Foldable t) => Traversable (t :: * -> *) where
  traverse :: Applicative f => (a -> f b) -> t a -> f (t b)
  sequenceA :: Applicative f => t (f a) -> f (t a)
  mapM :: Monad m => (a -> m b) -> t a -> m (t b)
  sequence :: Monad m => t (m a) -> m (t a)
data Word = GHC.Types.W# GHC.Prim.Word#
(^) :: (Num a, Integral b) => a -> b -> a
(^^) :: (Fractional a, Integral b) => a -> b -> a


def all(fn, a) -> bool:
    """all :: Foldable t => (a -> Bool) -> t a -> Bool
    """
    return builtins.all(fn(i) for i in a)

def and_(
    """and :: Foldable t => t Bool -> Bool
    """
    return builtins.all(a)
    
def any(fn, a):
    """any :: Foldable t => (a -> Bool) -> t a -> Bool"""
    return builtins.any(fn(i) for i in a)
  
appendFile :: FilePath -> String -> IO ()
asTypeOf :: a -> a -> a

def break_(fn, a_list):
    """break :: (a -> Bool) -> [a] -> ([a], [a])"""
    for i, elem in enumerate(a_list):
        if not fn(elem):
            break
    return a_list[:i], a_list[i:]

concat :: Foldable t => t [a] -> [a]
concatMap :: Foldable t => (a -> [b]) -> t a -> [b]
const :: a -> b -> a
curry :: ((a, b) -> c) -> a -> b -> c
cycle :: [a] -> [a]
drop :: Int -> [a] -> [a]
dropWhile :: (a -> Bool) -> [a] -> [a]
either :: (a -> c) -> (b -> c) -> Either a b -> c
error :: [Char] -> a
even :: Integral a => a -> Bool
  
def filter(fn, a_list):
    """filter :: (a -> Bool) -> [a] -> [a]"""
    return (i for i in a_list if fn(i))

def flip(fn):
    """flip :: (a -> b -> c) -> b -> a -> c"""
    def inner(b, a, c):
        return fn(a, b, c)
    return inner

fromIntegral :: (Integral a, Num b) => a -> b

def fst(a_tuple):
    """fst :: (a, b) -> a"""
    return a_tuple[0]

gcd :: Integral a => a -> a -> a
getChar :: IO Char
getContents :: IO String
getLine :: IO String

def head(a_list):
    """head :: [a] -> a"""
    return a_list[0]

def id(a):
    """id :: a -> a"""
    return a

init :: [a] -> [a]
interact :: (String -> String) -> IO ()
ioError :: IOError -> IO a
iterate :: (a -> a) -> a -> [a]
last :: [a] -> a
lcm :: Integral a => a -> a -> a
lex :: ReadS String

def lines(a_string):
    """lines :: String -> [String]"""
    return a_string.splitlines()
  
lookup :: Eq a => a -> [(a, b)] -> Maybe b
map :: (a -> b) -> [a] -> [b]
mapM_ :: (Foldable t, Monad m) => (a -> m b) -> t a -> m ()
maybe :: b -> (a -> b) -> Maybe a -> b

def not_(a_bool):
    """not :: Bool -> Bool"""
    return not a_bool
  
notElem :: (Foldable t, Eq a) => a -> t a -> Bool
odd :: Integral a => a -> Bool
  
def or_(t_sequence):
    """or :: Foldable t => t Bool -> Bool"""
    return builtins.any(t_sequence)

otherwise :: Bool
  
def print(a):
    """print :: Show a => a -> IO ()"""
    builtins.print(a)

putChar :: Char -> IO ()
putStr :: String -> IO ()
putStrLn :: String -> IO ()
read :: Read a => String -> a
readFile :: FilePath -> IO String
readIO :: Read a => String -> IO a
readLn :: Read a => IO a
readParen :: Bool -> ReadS a -> ReadS a
reads :: Read a => ReadS a
realToFrac :: (Real a, Fractional b) => a -> b
repeat :: a -> [a]
replicate :: Int -> a -> [a]
reverse :: [a] -> [a]
scanl :: (b -> a -> b) -> b -> [a] -> [b]
scanl1 :: (a -> a -> a) -> [a] -> [a]
scanr :: (a -> b -> b) -> b -> [a] -> [b]
scanr1 :: (a -> a -> a) -> [a] -> [a]

def seq(a, b):
    """seq :: a -> b -> b
    """
    return b
  

sequence_ :: (Foldable t, Monad m) => t (m a) -> m ()

  
showChar :: Char -> ShowS
showParen :: Bool -> ShowS -> ShowS
showString :: String -> ShowS

def shows(a):
    """shows :: Show a => a -> ShowS
    
    Not everything in Haskell has conversion to str,
    but in Python, we fallback to __repr__."""
    return lambda append_string: str(a) + append_string
  
def snd(a_tuple):
    """snd :: (a, b) -> b"""
    return a_tuple[1]

def span(fn, a_list):
    """span :: (a -> Bool) -> [a] -> ([a], [a])"""
    for i, elem in enumerate(a_list):
         if fn(elem):
             break
    return a_list[:i], a_list[i:]
  
def splitAt(n, a_list):
    """splitAt :: Int -> [a] -> ([a], [a])"""
    return a_list[:n], a_list[n:]

def subtract(a, b):
    """subtract :: Num a => a -> a -> a"""
    return a - b

def tail(a_list):
    """tail :: [a] -> [a]"""
    try:
        return a_list[1:]
    except Exception: #assume an iterator (lazy) instead of a list
        it = builtins.iter(a_list)
        next(it)
        return it

def take(i, a_list):
    """take :: Int -> [a] -> [a]"""
    return a_list[:i]
 
def takewhile(fn, a_list):
    """takeWhile :: (a -> Bool) -> [a] -> [a]"""
    for item in a_list:
        if fn(item):
            yield item
        else:
            break

def uncurry(fn, a_b_tuple):
    """uncurry :: (a -> b -> c) -> (a, b) -> c
    
    In Python, fn(*arg) is idiomatic for applying an 
    iterable of arguments positionally to a function.
    """
    return fn(*a_b_tuple)
undefined :: a
  
def unlines(list_of_strings):
    """unlines :: [String] -> String"""
    return ''.join([s  + '\n' for s in list_of_strings])

def until(p, f, a):
    """-- | @'until' p f@ yields the result of applying @f@ until @p@ holds.
    until                   :: (a -> Bool) -> (a -> a) -> a -> a
    until p f = go
      where
        go x | p x          = x
             | otherwise    = go (f x)
    recursively in python (likely less performant than implementation):
    def go(x):
        if p(x):
            return x
        else:
            return go(f(x))
    return go(a)
    """
    while not p(a):
        a = f(a)
    return a
        
def unwords(list_of_strings):
    """unwords :: [String] -> String"""
    return ' '.join(list_of_strings)
  
def unzip(list_of_tuples):
    """unzip :: [(a, b)] -> ([a], [b])"""
    list1, list2 = [], []
    for a, b in list_of_tuples:
        list1.append(a)
        list2.append(b)
    return list1, list2
  
def unzip3(list_of_tuples):
    """unzip3 :: [(a, b, c)] -> ([a], [b], [c])"""
    list1, list2, list3 = [], [], []
    for a, b, c in list_of_tuples:
        list1.append(a)
        list2.append(b)
        list3.append(c)
    return list1, list2, list3

def userError(a_string):
    """userError :: String -> IOError"""
    raise Exception(a_string) # I suppose, uncertain right now...

def words(a_string):
    """words :: String -> [String]"""
    return a_string.split()

def writeFile(FilePath, a_string):
    """writeFile :: FilePath -> String -> IO ()"""
    with open(FilePath, 'w') as file:
        file.write(a_string)
    # return None # a function that has no return returns None implicitly

def zip(a, b):
    """zip :: [a] -> [b] -> [(a, b)]"""
    return builtins.zip(a, b)

def zip3(a, b, c):
    """zip3 :: [a] -> [b] -> [c] -> [(a, b, c)]"""
    return builtins.zip(a, b, c)

def zipWith(fn, a, b):
    """zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
    
    You can actually do below I (Aaron Hall) prefer 
    people to use generator expressions to
    map and filter:
    return map(fn, a, b) 
    """
    return (fn(i, j) for i, j in zip(a, b))

def zipWith3(fn, a, b, c):
    """zipWith3 :: (a -> b -> c -> d) -> [a] -> [b] -> [c] -> [d]
    Same as zipWith, can do:
    return map(fn, a, b, c)
    """
    return (fn(i, j, k) for i, j, k in zip(a, b, c))

def _or_(bool0, bool1):
    """(||) :: Bool -> Bool -> Bool"""
    return bool0 or bool1


