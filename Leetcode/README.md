For python 3:

## 1. Generate Number
1. range(): range(n) will give range(0,n), if you want to create a iterable list, use list(range(n))


## 2. Built-in functions for list and string
1. map(): list(map(function, list_of_input)) will be the same as [function(i) for i in list(range(i))], see lc771
2. count(): str.count(sub-str), count the occurance of sub-str in str

      for example :
      map(str.count, str1) : think of str1 as a list, where the map function pass in every character in str1 into str, and check the occurance of that particular character in str. Here we could use sum() to adds up the occurance of every character in str1. see leetcode 771.

3. find() and index(): 

	str.find('character'), see if a character lies inside a string, if exist, returns the index of the LEFT MOST 'character', if not, return -1.

	list.index('element') similarily, you can find whether an element exist in a list by calling index() function. If the element does not exist, it will return an ValueError message.

4. split() and join():

	str.split('character') : separate string by every occurance of 'character', return a list of the separated parts, could use list indexation to retrieve sub_strings.

	'character'.join(a_list_of_string) : in contrast to split(), use join() to merge a list of strings into one big string, connected by designated 'character', for example, join with @ will be '@'.join(list).

5. list.pop(index): pop() will remove the index'th element of the list and return it, useful for Stack data type where you need to take out the first or lastest element that put into the stack.

6. To check if a list is empty: **For sequences, (strings, lists, tuples), use the fact that empty sequences are false.** 

7. Unlike list, in string, you cannot assign value to an existing element in the string. If you want to change the ith element of the string, or swap 2 element in the string, this error will pop-up ‘TypeError: 'str' object does not support item assignment’, see lc345 reverse a string, which is basically a changed version of reverse string.

8. chr() and ord() : ord('a') = 97, chr(97) = 'a'. This pair of functions gives the Unicode code point of the character. see leetcode 709, upper and lower case letters.




   
          
