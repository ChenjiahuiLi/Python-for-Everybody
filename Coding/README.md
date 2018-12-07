For python 3:

## 1. Generate Number
1. range(): range(n) will give range(0,n), if you want to create a iterable list, use list(range(n))


## 2. Built-in functions
1. map(): list(map(function, list_of_input)) will be the same as [function(i) for i in list(range(i))]
2. count(): str.count(sub-str), count the occurance of sub-str in str
   # map(str.count, str1) : think of str1 as a list, where the map function pass in every character in str1 into str, and check the occurance of that particular character in str. Here we could use sum() to adds up the occurance of every character in str1. see leetcode 771.

   
          