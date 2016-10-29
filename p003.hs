-- https://wiki.haskell.org/Testing_primality

import Data.List (unfoldr)
import Data.Maybe (listToMaybe)
 
factors :: Integer -> [Integer]
factors n = unfoldr (\(d,n) -> listToMaybe [(x, (x, div n x)) | x <- takeWhile ((<=n).(^2)) 
                                                 [d..] ++ [n|n>1], mod n x==0]) (2,n)
isPrime n = n > 1 && head (factors n) == n