# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are Tuples are both data structures in python that can contain multiple values or elements. While lists are mutable, tuples are immutable. Therefore, tuples are the one that will work as keys in dictionaries because only immutable element can play as keys.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Just like above, they are data structures in python that can contain multiple values or elements. While lists allow the duplicates, sets don't.
>> Ex. for List) list = [1, 2, 3, 4] // [1, 2, 3, 4]
>> Ex. for set) set = set(1, 2, 2, 3, 4, 5, 5) // set([1, 2, 3, 4, 5])
>> In List, searching uses the iteration going through elements to find. Set uses the hash computing for the search. Usually sets are faster for searching an element unless it is a case where list is already sorted so it's quite simple.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is an operator to quickly create inline function so such simple function can be defined very easily and quickly, even without the name of the function.
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a very easy and convenient way to generate a list by providing detail condition for the elements.
>> map) map(lambda x : x * 2, [1, 2, 3, 4]) // [2, 4, 6, 8]
>> filter) filter(lambda x : x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8] // [2, 4, 6, 8]
>> Although examples above yielded the same results between map and filter, while map function returns a list of elements that result from the condition given from the map argument, filter function returns(filter out) a list of elements that satisfy the condition provided from the filter argument. So usually, the elements given out from filter function are the ones out of the original list, while map does not necessarily do so.
>> ex) S = [x ** 2 for x in range(10)] // gives out a list with squared values from 0 to 9
>> ex set comprehension) S = { x for x in range(5) } // set([0, 1, 2, 3, 4])
>> ex dict comprehension) S = {x : True for x in range(5)}
>> S -> // {0: True, 1: True, 2: True, 3: True, 4: True}
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>>7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)
>> Code saved in python/q5_datetime.py

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)
>> File saved with code

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)
>> File saved with code

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
>> File saved with code
