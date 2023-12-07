"""
Definition of Generator?
    A generator is a function that produces a sequence of results instead of a single value.
    In other words, a generator is a function that can be used to control the iteration behaviour of a loop.
    A generator is a special kind of iterator, and the only way to obtain one is to call a generator function.
    A generator function is a function that contains the yield keyword. The yield keyword is used to return a value from a generator function.
    The yield keyword suspends the function's execution and sends a value back to the caller.
    When the generator function is called again, it resumes from the point it left off.
    The yield keyword is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
    Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off.
    Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.
    The following example illustrates the generator function that generates the squares of numbers.
    The generator function is called with the for loop to iterate over the sequence of values returned by the generator.

    def squares(n):
        for i in range(n):
            yield i ** 2    # yield keyword returns a value from a generator function

    sq = squares(5)
    print(sq)   # <generator object squares at 0x0000020F4F6F9C80>


Definition of Iterator?
    An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
    Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
    An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple, string etc. are iterables.
    The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
    The __next__() method (next() in Python 3.x) returns the next value from the iterator.
    The for loop implicitly calls the __next__() method of the iterator object returned by the iter() function.
    The __iter__() method returns the iterator object itself.
    If the class defines __next__() method, then the class is an iterator.
    The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.
    The __iter__() method can be used to make an iterable class iterable.
    The __iter__() method is called whenever the iter() function is called on an object.
    The __next__() method is called whenever the next() function is called on an iterator object.
    The __next__() method returns the next value from the iterator.
    The __next__() method raises StopIteration exception when there are no more elements left to return.
    The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.
    The __iter__() method can be used to make an iterable class iterable.
    The __iter__() method is called whenever the iter() function is called on an object.
    The __next__() method is called whenever the next() function is called on an iterator object.
    The __next__() method returns the next value from the iterator.
    The __next__() method raises StopIteration exception when there are no more elements left to return.
    The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.
    The __iter__() method can be used to make an iterable class iterable.
    The __iter__() method is called whenever the iter() function is called on an object.
    The __next__() method is called whenever the next() function is called on an iterator object.
    The __next__() method returns the next value from the iterator.
    The __next__() method raises StopIteration exception when there are no more elements left to return.


    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self    # returns the iterator object itself (self)

        def __next__(self):
            if self.a <= 20:   # if the condition is True, the function returns the next value in the sequence (self.a) and increments it by 1
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration

    myclass = MyNumbers()
    myiter = iter(myclass)
    print(next(myiter)) # 1
    print(next(myiter)) # 2
    print(next(myiter)) # 3


Definition of Iterable?
    An iterable is an object that can be iterated upon, meaning that you can traverse through all the values.
    Technically, in Python, an iterable is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
    An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple, string etc. are iterables.
    The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
    The __next__() method (next() in Python 3.x) returns the next value from the iterator.
    The for loop implicitly calls the __next__() method of the iterator object returned by the iter() function.
    The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.
    The __iter__() method can be used to make an iterable class iterable.
    The __iter__() method is called whenever the iter() function is called on an object.
    The __next__() method is called whenever the next() function is called on an iterator object.
    The __next__() method returns the next value from the iterator.
    The __next__() method raises StopIteration exception when there are no more elements left to return.
    The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.
    The __iter__() method can be used to make an iterable class iterable.
    The __iter__() method is called whenever the iter() function is called on an object.


Definition of Yield?
    The yield keyword is used to return a value from a generator function.
    The yield keyword suspends the function's execution and sends a value back to the caller.
    When the generator function is called again, it resumes from the point it left off.
    The yield keyword is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
    Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off.
    Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.
    The following example illustrates the generator function that generates the squares of numbers.
    The generator function is called with the for loop to iterate over the sequence of values returned by the generator.

    def squares(n):
        for i in range(n):
            yield i ** 2    # yield keyword returns a value from a generator function

    sq = squares(5)
    print(sq)   # <generator object squares at 0x0000020F4F6F9C80>
    print(next(sq))   # 0
    print(next(sq))   # 1
    print(next(sq))   # 4
    print(next(sq))   # StopIteration exception raised

    for i in sq:
        print(i)   # 0 1 4 9 16



Iterator vs Iterable?
    An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
    Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
    An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple, string etc. are iterables.
    The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
    The __next__() method (next() in Python 3.x) returns the next value from the iterator.
    The for loop implicitly calls the __next__() method of the iterator object returned by the iter() function.
    The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.
    The __iter__() method can be used to make an iterable class iterable.
    The __iter__() method is called whenever the iter() function is called on an object.
    The __next__() method is called whenever the next() function is called on an iterator object.
    The __next__() method returns the next value from the iterator.
    The __next__() method raises StopIteration exception when there are no more elements left to return.
    The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.
    The __iter__() method can be used to make an iterable class iterable.
    The __iter__() method is called whenever the iter() function is called on an object.


Yield vs Return?
    The yield keyword is used to return a value from a generator function.
    The yield keyword suspends the function's execution and sends a value back to the caller.
    When the generator function is called again, it resumes from the point it left off.
    The yield keyword is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
    Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off.
    Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.
    The following example illustrates the generator function that generates the squares of numbers.
    The generator function is called with the for loop to iterate over the sequence of values returned by the generator.


Comprehension?
    Comprehension is a concise and expressive way to create a new list, set, or dictionary from an existing list, set, or dictionary.

    Syntax:
        [expression for item in iterable]   # list comprehension
        {expression for item in iterable}   # set comprehension
        {key_expression: value_expression for item in iterable}   # dictionary comprehension

    Example:
        # list comprehension
        x = [i for i in range(10)]
        print(x)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # set comprehension
        x = {i for i in range(10)}
        print(x)   # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

        # dictionary comprehension
        x = {i: i * i for i in range(10)}
        print(x)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

what is Closure?
    A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
    It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
    A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

    Example:
        def outer_func():
            message = 'Hi'
            def inner_func():
                print(message)
            return inner_func
        inner_func = outer_func()
        inner_func()   # Hi

        def outer_func(msg):
            message = msg
            def inner_func():
                print(message)
            return inner_func
        inner_func = outer_func('Hi')
        inner_func()   # Hi


what is Decorator?
    A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

    Example:
        def decorator_func(func):
            def wrapper_func():
                print('wrapper function executed this before {}'.format(func.__name__))
                return func()
            return wrapper_func()
        @decorator_func
        def regular_func():
            print('regular function executed this after decorator_func')
        regular_func()   # wrapper function executed this before regular_func




lambda function?
    A lambda function is a small anonymous function.
    A lambda function can take any number of arguments, but can only have one expression.
    The expression is evaluated and returned.
    Lambda functions can be used wherever function objects are required.
    Lambda functions are syntactically restricted to a single expression.

    Syntax:
        lambda arguments : expression   # lambda keyword is used to create a lambda function

    Example:
        x = lambda a : a + 10
        print(x(5))   # 15

        x = lambda a, b : a * b
        print(x(5, 6))   # 30

        x = lambda a, b, c : a + b + c
        print(x(5, 6, 2))   # 13


map function?
    The map() function executes a specified function for each item in an iterable.
    The item is sent to the function as a parameter.
    The map() function returns a map object(which is an iterator) containing the results. The map object is iterable as well.
    The map() function executes a specified function for each item in an iterable.

    Syntax:
        map(function, iterable(s))   # map() function returns a map object(which is an iterator) containing the results. The map object is iterable as well.

    Example:
        def myfunc(n):
            return len(n)

        x = map(myfunc, ('apple', 'banana', 'cherry'))
        print(x)   # <map object at 0x0000020F4F6F9C80>
        print(list(x))   # [5, 6, 6]

        def myfunc(a, b):
            return a + b

        x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
        print(x)   # <map object at 0x0000020F4F6F9C80>
        print(list(x))   # ['appleorange', 'bananalemon', 'cherrypineapple']

        def myfunc(n):
            return len(n)

        x = map(myfunc, ('apple', 'banana', 'cherry'))
        print(x)   # <map object at 0x0000020F4F6F9C80>
        print(tuple(x))   # (5, 6, 6)

        def myfunc(a, b):
            return a + b

        x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
        print(x)   # <map object at 0x0000020F4F6F9C80>
        print(tuple(x))   # ('appleorange', 'bananalemon', 'cherrypineapple')



filter function?
    The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

    Syntax:
        filter(function, iterable)   # filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

    Example:
        def myfunc(x):
            if x < 18:
                return False
            else:
                return True

        x = filter(myfunc, [5, 12, 17, 18, 24, 32])
        print(x)   # <filter object at 0x0000020F4F6F9C80>
        print(list(x))   # [18, 24, 32]

reduce function?
    The reduce() function accepts a function and a sequence and returns a single value calculated as follows:
        Initially, the function is called with the first two items from the sequence and the result is returned.
        The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.
        The reduce() function is defined in the functools module.
        The reduce() function is used to apply a function to every item of a sequence and returns a single value.
        The reduce() function accepts a function and a sequence and returns a single value calculated as follows:
            Initially, the function is called with the first two items from the sequence and the result is returned.
            The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.
            The reduce() function is defined in the functools module.
            The reduce() function is used to apply a function to every item of a sequence and returns a single value.

        syntax:
            reduce(function, sequence[, initial])   # The reduce() function accepts a function and a sequence and returns a single value calculated as follows:

        Example:
            from functools import reduce
            def myfunc(a, b):
                return a + b

            x = reduce(myfunc, [1, 2, 3, 4, 5])
            print(x)   # 15  # Initially, the function is called with the first two items from the sequence and the result is returned. The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.



zip function?
    The zip() function returns an iterator that will aggregate elements from each of the iterables passed.
    The zip() function is defined in the itertools module.
    The zip() function is used to aggregate elements from each of the iterables passed.

    syntax:
        zip(*iterables)   # The zip() function returns an iterator that will aggregate elements from each of the iterables passed.

    Example:
        x = [1, 2, 3]
        y = [4, 5, 6]
        zipped = zip(x, y)
        print(zipped)   # <zip object at 0x0000020F4F6F9C80>
        print(list(zipped))   # [(1, 4), (2, 5), (3, 6)]

enumerate function?
    The enumerate() function returns an enumerate object. It contains the index and value of all the items in the iterable as pairs.
    The enumerate() function is defined in the itertools module.
    The enumerate() function is used to add counter to an iterable and returns it.

    syntax:
        enumerate(iterable, start=0)   # The enumerate() function returns an enumerate object. It contains the index and value of all the items in the iterable as pairs.

    Example:
        x = ('apple', 'banana', 'cherry')
        y = enumerate(x)
        print(y)   # <enumerate object at 0x0000020F4F6F9C80>
        print(list(y))   # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

chain function?
    The chain() function returns an iterator that aggregates elements from each of the iterables passed.
    The chain() function is defined in the itertools module.
    The chain() function is used to chain a series of iterables together.

    syntax:
        chain(*iterables)   # The chain() function returns an iterator that aggregates elements from each of the iterables passed.

    Example:
        x = [1, 2, 3]
        y = [4, 5, 6]
        z = [7, 8, 9]
        result = chain(x, y, z)
        print(result)   # <itertools.chain object at 0x0000020F4F6F9C80>
        print(list(result))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

islice function?
    The islice() function returns an iterator that returns selected items from the input iterable, by index.
    The islice() function is defined in the itertools module.
    The islice() function is used to slice a given iterable.

    syntax:
        islice(iterable, start, stop[, step])   # The islice() function returns an iterator that returns selected items from the input iterable, by index.

    Example:
        from itertools import islice
        x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        result = islice(x, )
        print(result)   # <itertools.islice object at 0x0000020F4F6F9C80>
        print(list(result))   # ['a', 'b', 'c']


accumulate function?
    The accumulate() function returns an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).
    The accumulate() function is defined in the itertools module.
    The accumulate() function is used to calculate accumulated values.

    syntax:
        accumulate(iterable[, func])   # The accumulate() function returns an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).


    Example:
        from itertools import accumulate
        x = [1, 2, 3, 4, 5]
        result = accumulate(x)  # default function is addition
        print(result)   # <itertools.accumulate object at 0x0000020F4F6F9C80>
        print(list(result))   # [1, 3, 6, 10, 15]

        from itertools import accumulate
        x = [1, 2, 3, 4, 5]
        result = accumulate(x, func = operator.mul)  # default function is addition
        print(result)   # <itertools.accumulate object at 0x0000020F4F6F9C80>
        print(list(result))   # [1, 2, 6, 24, 120]

        from itertools import accumulate
        x = [1, 2, 3, 4, 5]
        result = accumulate(x, func = max)  # default function is addition
        print(result)   # <itertools.accumulate object at 0x0000020F4F6F9C80>
        print(list(result))   # [1, 2, 3, 4, 5]

        from itertools import accumulate
        x = [1, 2, 3, 4, 5]
        result = accumulate(x, func = min)  # default function is addition
        print(result)   # <itertools.accumulate object at 0x0000020F4F6F9C80>
        print(list(result))   # [1, 1, 1, 1, 1]


starmap function?
    The starmap() function returns an iterator that computes the function using arguments obtained from the iterable.
    The starmap() function is defined in the itertools module.
    The starmap() function is used to compute the values using the function and iterable.

    syntax:
        starmap(function, iterable)   # The starmap() function returns an iterator that computes the function using arguments obtained from the iterable.

    Example:
        from itertools import starmap
        x = [(1, 2), (3, 4), (5, 6)]
        result = starmap(operator.mul, x)  # default function is addition
        print(result)   # <itertools.starmap object at 0x0000020F4F6F9C80>
        print(list(result))   # [2, 12, 30]

        from itertools import starmap
        x = [(1, 2, 3), (3, 4, 5), (5, 6, 7)]
        result = starmap(operator.mul, x)  # default function is addition
        print(result)   # <itertools.starmap object at 0x0000020F4F6F9C80>
        print(list(result))   # [6, 60, 210]


tee function?
    The tee() function returns several independent iterators (defaults to 2) based on a single original input.
    The tee() function is defined in the itertools module.
    The tee() function is used to create independent iterators from a single iterable.

    syntax:
        tee(iterable, n=2)   # The tee() function returns several independent iterators (defaults to 2) based on a single original input.

    Example:
        from itertools import tee
        x = [1, 2, 3, 4, 5]
        result = tee(x)  # default function is addition
        print(result)   # <itertools.tee object at 0x0000020F4F6F9C80>
        print(list(result))   # [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]

        from itertools import tee
        x = [1, 2, 3, 4, 5]
        result = tee(x, 3)  # default function is addition
        print(result)   # <itertools.tee object at 0x0000020F4F6F9C80>
        print(list(result))   # [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5)]


groupby function?
    The groupby() function returns an iterator that produces sets of values grouped by a common key.
    The groupby() function is defined in the itertools module.
    The groupby() function is used to group the values by the same key.

    syntax:
        groupby(iterable[, keyfunc])   # The groupby() function returns an iterator that produces sets of values grouped by a common key.

    Example:
        from itertools import groupby
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = groupby(x)  # default function is addition
        print(result)   # <itertools.groupby object at 0x0000020F4F6F9C80>
        print(list(result))   # [(1, [1]), (2, [2]), (3, [3]), (4, [4]), (5, [5]), (6, [6]), (7, [7]), (8, [8]), (9, [9]), (10, [10])]


        from itertools import groupby
        x = [1, 2, 3, 4, 5]
        result = groupby(x, lambda x: x < 3)  # default function is addition
        print(result)   # <itertools.groupby object at 0x0000020F4F6F9C80>
        print(list(result))   # [(True, [1, 2]), (False, [3, 4, 5])]

        from itertools import groupby
        x = [1, 2, 3, 4, 5]
        result = groupby(x, lambda x: x % 2)  # default function is addition
        print(result)   # <itertools.groupby object at 0x0000020F4F6F9C80>
        print(list(result))   # [(1, [1]), (0, [2]), (1, [3]), (0, [4]), (1, [5])]

        from itertools import groupby
        x = [1, 2, 3, 4, 5]
        result = groupby(x, lambda x: x % 3)  # default function is addition
        print(result)   # <itertools.groupby object at 0x0000020F4F6F9C80>
        print(list(result))   # [(1, [1, 4]), (2, [2, 5]), (0, [3])]

        from itertools import groupby
        x = [1, 2, 3, 4, 5]
        result = groupby(x, lambda x: x % 4)  # default function is addition
        print(result)   # <itertools.groupby object at 0x0000020F4F6F9C80>
        print(list(result))   # [(1, [1, 5]), (2, [2]), (3, [3]), (0, [4])]



count function?
    The count() function returns an iterator that produces consecutive integers, forever.
    The count() function is defined in the itertools module.
    The count() function is used to count the values.

    syntax:
        count(start=0, step=1)   # The count() function returns an iterator that produces consecutive integers, forever.

    example:
        from itertools import count
        x = count()  # default function is addition
        print(x)   # <itertools.count object at 0x0000020F4F6F9C80>
        print(list(x))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    Example:
        from itertools import count
        x = count(10)  # default function is addition
        print(x)   # <itertools.count object at 0x0000020F4F6F9C80>
        print(list(x))   # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        from itertools import count
        x = count(10, 2)  # default function is addition
        print(x)   # <itertools.count object at 0x0000020F4F6F9C80>
        print(list(x))   # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


cycle function?
    The cycle() function returns an iterator that repeats the contents of the arguments it is given indefinitely.
    The cycle() function is defined in the itertools module.
    The cycle() function is used to cycle through the values.

    syntax:
        cycle(iterable)   # The cycle() function returns an iterator that repeats the contents of the arguments it is given indefinitely.

    Example:
        from itertools import cycle
        x = cycle('ABCD')  # default function is addition
        print(x)   # <itertools.cycle object at 0x0000020F4F6F9C80>
        print(list(x))   # ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']

        from itertools import cycle
        x = cycle([1, 2, 3, 4])  # default function is addition
        print(x)   # <itertools.cycle object at 0x0000020F4F6F9C80>
        print(list(x))   # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]








"""
# questions
"""
How can we create a generator in Python?


A. With a for loop and the in keyword


B. With the __iter__ and __next__ built-in methods


C. With a function or class that uses the yield keyword in place of return


D. With a list comprehension inside a pair of parenthesis "()"



A, C


C, D


B, D

Answer: C, D 

Explanation: 
    A generator is a function that produces a sequence of results instead of a single value.
    In other words, a generator is a function that can be used to control the iteration behaviour of a loop.    
    A generator is a special kind of iterator, and the only way to obtain one is to call a generator function.  
    A generator function is a function that contains the yield keyword. The yield keyword is used to return a value from a generator function.
    The yield keyword suspends the function's execution and sends a value back to the caller.
    When the generator function is called again, it resumes from the point it left off.
    The yield keyword is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
    Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off. 
    Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.
    The following example illustrates the generator function that generates the squares of numbers.
    The generator function is called with the for loop to iterate over the sequence of values returned by the generator.
    
    def squares(n):
        for i in range(n):
            yield i ** 2    # yield keyword returns a value from a generator function
            
    sq = squares(5)  # sq is a generator object
    print(sq)   # <generator object squares at 0x0000020F4F6F9C80>
    print(next(sq))   # 0
    print(next(sq))   # 1
    print(next(sq))   # 4
    print(next(sq))   # 9
    
    
    for i in sq:
        print(i)   # 0 1 4 9 16
        
    # The __iter__() method returns the iterator object itself. If the class defines __iter__(), then it is an iterator.    
    # The __iter__() method can be used to make an iterable class iterable.
    # The __iter__() method is called whenever the iter() function is called on an object.
    # The __next__() method is called whenever the next() function is called on an iterator object.
    # The __next__() method returns the next value from the iterator.   
    # The __next__() method raises StopIteration exception when there are no more elements left to return.  
    
    class MyNumbers:
        def __iter__(self):
            self.a = 1  
            return self    # returns the iterator object itself (self)
            
        def __next__(self):
            if self.a <= 20:   # if the condition is True, the function returns the next value in the sequence (self.a) and increments it by 1
                x = self.a
                self.a += 1
                return x
            else:   # if the condition is False, the function raises the StopIteration exception
                raise StopIteration
                
    myclass = MyNumbers()  # myclass is an object of the MyNumbers class
    myiter = iter(myclass)  # myiter is an iterator object that can be iterated over using the next() function
    print(next(myiter)) # 1
    print(next(myiter)) # 2
    print(next(myiter)) # 3
    


Which of the following statements are true about the yield keyword?



turns a function into a generator function


it replaces the return keyword


all of the above


it stores the last iterated value until it is called again


the function cannot be called on its own

Answer: all of the above

Explanation:
    The yield keyword is used to return a value from a generator function.
    The yield keyword suspends the function's execution and sends a value back to the caller.
    When the generator function is called again, it resumes from the point it left off.
    The yield keyword is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
    Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off.
    Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.
    The following example illustrates the generator function that generates the squares of numbers.
    The generator function is called with the for loop to iterate over the sequence of values returned by the generator.
    
    def squares(n):
        for i in range(n):
            yield i ** 2    # yield keyword returns a value from a generator function
            
    sq = squares(5)  # sq is a generator object
    print(sq)   # <generator object squares at 0x0000020F4F6F9C80>
    print(next(sq))   # 0
    print(next(sq))   # 1
    print(next(sq))   # 4
    

What is a lambda function?



a function that is written in one line


all of the above


an anonymous function


a function that can be used within list comprehensions


a function called from another function

Answer: all of the above

Explanation:
    A lambda function is a small anonymous function. It is a function that is defined without a name. It is defined using the lambda keyword.
    A lambda function can take any number of arguments, but can only have one expression.
    The expression is evaluated and returned.
    Lambda functions can be used wherever function objects are required.
    Lambda functions are syntactically restricted to a single expression.
    Lambda functions are used to create anonymous
    The following example illustrates the lambda function that adds 10 to the number passed in as an argument.
    
    x = lambda a : a + 10
    print(x(5))   # 15
    
    The following example illustrates the lambda function that multiplies the two numbers passed in as arguments.
    
    x = lambda a, b : a * b
    print(x(5, 6))   # 30
    
    The following example illustrates the lambda function that adds the three numbers passed in as arguments.
    
    x = lambda a, b, c : a + b + c
    print(x(5, 6, 2))   # 13
    
    The following example illustrates the lambda function that returns the sum of the two numbers passed in as arguments.
    
    
    def myfunc(n):
        return lambda a : a * n
        
    mydoubler = myfunc(2)
    print(mydoubler(11))   # 22
    
    mytripler = myfunc(3)
    print(mytripler(11))   # 33
    
    The following example illustrates the lambda function that returns the sum of the two numbers passed in as arguments.
    
    def myfunc(n):
        return lambda a : a * n
        
    mydoubler = myfunc(2)
    print(mydoubler(11))   # 22
    
    

How can we declare a lambda function?



lambda x, y = x + y


lambda x, y: x + y


lambda[x, y: x+ y]


lambda(x, y): x + y

Answer: lambda x, y: x + y
lambda is a keyword that is used to declare a lambda function. The syntax of a lambda function is as follows:
    lambda arguments : expression
    The following example illustrates the lambda function that adds 10 to the number passed in as an argument.
    
    x = lambda a : a + 10
    print(x(5))   # 15
    
    The following example illustrates the lambda function that multiplies the two numbers passed in as arguments.
    
    x = lambda a, b : a * b
    print(x(5, 6))   # 30
    
    The following example illustrates the lambda function that adds the three numbers passed in as arguments.
    
    x = lambda a, b, c : a + b + c
    print(x(5, 6, 2))   # 13
    
    

What is the order of the arguments inside the map() and filter() functions?



function, iterable


iterable, function

Answer: function, iterable 

Explanation:
    The map() function executes a specified function for each item in an iterable.
    The item is sent to the function as a parameter.
    The map() function returns a map object(which is an iterator) containing the results. The map object is iterable as well.
    The map() function executes a specified function for each item in an iterable.
    The syntax of the map() function is as follows:
        map(function, iterable)
    The following example illustrates the map() function that returns the length of each item in the list.
    
    def myfunc(n):
        return len(n)
        
    x = map(myfunc, ('apple', 'banana', 'cherry'))
    print(x)   # <map object at 0x0000020F4F6F9C80>
    print(list(x))   # [5, 6, 6]
    
    The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
    The filter() function is defined in the itertools module.
    The filter() function is used to filter the values.
    The syntax of the filter() function is as follows:
        filter(function, iterable)
    The following example illustrates the filter() function that returns the items that are greater than 18.
    
    def myfunc(x):
        if x < 18:
            return False
        else:
            return True
            
    x = filter(myfunc, [5, 12, 17, 18, 24, 32]) 
    print(x)   # <filter object at 0x0000020F4F6F9C80>
    print(list(x))   # [18, 24, 32]
    

Which of the following statements are correct?


A. filter() returns an iterable


B. map() returns an iterable


C. map() can accept more than one iterable, as long as the function has one parameter for each iterable


D. filter() returns an object



A, C


B, A


C, D

Answer: A, C

Explanation:
    The map() function executes a specified function for each item in an iterable.
    The item is sent to the function as a parameter.
The map() function returns a map object(which is an iterator) containing the results. The map object is iterable as well.
    The map() function executes a specified function for each item in an iterable.
    The syntax of the map() function is as follows:
        map(function, iterable)
    The following example illustrates the map() function that returns the length of each item in the list.
    
    def myfunc(n):
        return len(n)
        
    x = map(myfunc, ('apple', 'banana', 'cherry'))
    print(x)   # <map object at 0x0000020F4F6F9C80>
    print(list(x))   # [5, 6, 6]
    
    The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
    The filter() function is defined in the itertools module.
    The filter() function is used to filter the values.
    The syntax of the filter() function is as follows:
        filter(function, iterable)
    The following example illustrates the filter() function that returns the items that are greater than 18.
    
    def myfunc(x):
        if x < 18:
            return False
        else:
            return True
            
    x = filter(myfunc, [5, 12, 17, 18, 24, 32])
    print(x)   # <filter object at 0x0000020F4F6F9C80>
    print(list(x))   # [18, 24, 32]
    
    
What is a closure in Python?


A. A function that can pass a previous state of its invocation to its next


B. A function that calls itself


C. A function that calls another function


D. A function that returns an inner function



A, B


C, D


B, D


A, D

Answer: A, D

Explanation:
    A closure is a function that can pass a previous state of its invocation to its next.
    A closure is a function that returns an inner function.
    
    def outer_func():
        message = 'Hi'
        def inner_func():
            print(message)
        return inner_func
        
    my_func = outer_func() # my_func is a closure
    
    print(my_func)   # <function outer_func.<locals>.inner_func at 0x0000020F4F6F9C80>
    print(my_func.__name__)   # inner_func
    my_func()   # Hi
    
    

While we can assign a variable to a lambda function, the official Python documentation recommends that lambdas should not be assigned to variables. They should rather be used as anonymous functions.


# Correct:
def f(x): 
    return 2*x

# Wrong:
f = lambda x: 2*x


See: https://www.python.org/dev/peps/pep-0008/#programming-recommendations


However we can still see this kind of code as it does not raise an error. And we can see the lambda be called as a typical function that takes as many parameters as defined in the lambda:


f = lambda x: 2*x
print(f(2))
print(f(3))


Which of the following options can replace the code below and return the same results?


>>> [x for x in range(10) if x % 2 == 0]

[map(lambda x: x % 2 == 0, [x for x in range(10)])]


[filter(lambda x: x % 2 == 0, [x for x in range(10)])]


list(filter(lambda x: x % 2 == 0, [x for x in range(10)]))


map(filter(lambda x: x % 2 == 0, [x for x in range(10)]))

Answer: list(filter(lambda x: x % 2 == 0, [x for x in range(10)]))

Explanation:
    The map() function executes a specified function for each item in an iterable.
    The item is sent to the function as a parameter.
    The syntax of the map() function is as follows:
        map(function, iterable)
    The following example illustrates the map() function that returns the length of each item in the list.
    
    def myfunc(n):
        return len(n)
            
    x = map(myfunc, ('apple', 'banana', 'cherry'))
    print(x)   # <map object at 0x0000020F4F6F9C80>
    print(list(x))   # [5, 6, 6]
    
    
    The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
    The filter() function is defined in the itertools module.
    The filter() function is used to filter the values.
    The syntax of the filter() function is as follows:
        filter(function, iterable)
    The following example illustrates the filter() function that returns the items that are greater than 18.
    
    def myfunc(x):
        if x < 18:
            return False
        else:
            return True
            
    x = filter(myfunc, [5, 12, 17, 18, 24, 32])
    print(x)   # <filter object at 0x0000020F4F6F9C80>
    print(list(x))   # [18, 24, 32]
    
    
    
Which of the following options can replace the code below with the same results?


>>> [1 if x % 2 == 0 else 0 for x in range(5)]

map(lambda x: 1 if x % 2 == 0 else 0, [x for x in range(5)])


list(filter(lambda x: 1 if x % 2 == 0 else 0, [x for x in range(5)]))


list(map(lambda x: 1 if x % 2 == 0 else 0, [x for x in range(5)]))


filter(lambda x: 1 if x % 2 == 0 else 0 for x in range(5)))

Answer: list(map(lambda x: 1 if x % 2 == 0 else 0, [x for x in range(5)]))

Explanation:
    The map() function executes a specified function for each item in an iterable.
    The item is sent to the function as a parameter.
    The syntax of the map() function is as follows:
        map(function, iterable)
    The following example illustrates the map() function that returns the length of each item in the list.
        
    def myfunc(n):
        return len(n)
            
    x = map(myfunc, ('apple', 'banana', 'cherry'))
    print(x)   # <map object at 0x0000020F4F6F9C80>
    print(list(x))   # [5, 6, 6]
    

What is the correct closure invocation if we want the output of the following code to be: <h4>Python Class<h4>


def tag(t):
    t2 = t
    t2 = t[0] + '/' + t[1:]

    def title(str):
        return t + str.title() + t2
    return title

tag('<')


tg = tag('python class')

t = tag('<')


t('python class')

tag('<')


tag('python class')

Answer: tag('<')('python class')

Explanation:
    A closure is a function that can pass a previous state of its invocation to its next.
    A closure is a function that returns an inner function.
    
    def tag(t):
        t2 = t
        t2 = t[0] + '/' + t[1:]
        def title(str):
            return t + str.title() + t2
        return title
    return tag
    
    tag('<')('python class')   # <h4>Python Class<h4>   
    
    
    
Open the file comprehensions.py, and complete the code so that a new list, called numbers is created. It should contain only numeric data types, hence strings and symbols should be filtered out.


Expected output:


[1, 0.5, 3.0]


CheckCompleteIncomplete

mix_list = [1, "Python", 0.5, "Apple", 3.0, "\n"]
# create the numbers list using the lambda and filter functions
#
#

print(numbers)


mix_list = [1, "Python", 0.5, "Apple", 3.0, "\n"]

numbers = [x for x in mix_list if isinstance(x, (int, float))]

print(numbers)


The quizzes for the lambda functions we’ve seen so far are not really doing justice to the lambda function and its idiomatic use in Python. They were just illustrative of how lambdas work. A real life example of using lambda functions could be the case of creating a calendar app, where we need to sort upcoming events.


Open the file events.py, and complete the code so that the events are sorted by date.


CheckCompleteIncomplete
Code Check

events = [
        {'date': 11212021, 'name': 'Bengali wedding'},
        {'date': 11012021, 'name': 'Project meeting'},
        {'date': 11112021, 'name': 'Guitar class'},
]

# Add the sorted code here

print(sorted_events)


events = [
    {'date': 11212021, 'name': 'Bengali wedding'},
    {'date': 11012021, 'name': 'Project meeting'},
    {'date': 11112021, 'name': 'Guitar class'},
]

sorted_events = sorted(events, key=lambda event: event['date'])

print(sorted_events)

Did you know that we can call a generator object with the built-in function next()? The yield keyword allows for a lazy execution of the generator. So if our generator is called counter(), each time we call next(counter()), we move forward one iteration.


Open the file generator.py, and complete the code by creating the counter generator function.


The generator should iterate as many times as its number argument, including it. So slightly different from the range() generator. Also, a fix is required in the print statement so that the StopIteration exception is not raised.


Expected output:


0 1 2 3


CheckCompleteIncomplete
Code Check

# Create the counter generator
def counter(n)
    #
    #
        #
        #

c = counter(3)
print(next(c), next(c), next(c), next(c), next(c))


# Create the counter generator
def counter(n):
    count = 0
    while count <= n:
        yield count
        count += 1

c = counter(3)
print(*(c))

***************************************************************************************************

# file and input/output operations

Which of the following are correct ways to write a Windows file path in Python?


A.

name = "/dir/file" # Python internally converts the required syntax


B.

name = "c:/dir/file" # Python internally converts the required syntax


C.

name = "c:\dir\file" # like we usually do for Windows


D.

name = "c:\\dir\\file" # Python needs to escape the special character '\'



B, D


All options are correct


A, D

Answer: A, D 

Explanation: 
    The backslash "\" is a special character in Python. It is used to escape characters that otherwise have a special meaning, such as newline, backslash itself, or the quote character.
    The backslash "\" is used to escape characters that otherwise have a special meaning, such as newline, backslash itself, or the quote character.
    The single backslash "\" is used to escape the single quote character in a string.
    The double backslash "\\" is used to escape the backslash character in a string.
The following example illustrates the single backslash "\" that is used to escape the single quote character in a string.

    txt = 'It\'s alright.'
    print(txt)   # It's alright.
    
    The following example illustrates the double backslash "\\" that is used to escape the backslash character in a string.
    
    txt = "This will insert one \\ (backslash)."
    print(txt)   # This will insert one \ (backslash).
    
    txt = "Hello\nWorld!"
    print(txt)   # Hello
                # World!
    
    txt = "Hello\tWorld!"
    print(txt)   # Hello   World!
    
    txt = "Hello\rWorld!"
    print(txt)   # World!
    
    txt = "Hello\bWorld!"
    print(txt)   # HelloWorld!
    
    txt = "Hello\fWorld!"
    print(txt)   # Hello World!
    
    txt = "\110\145\154\154\157"
    print(txt)   # Hello
    
    txt = "\x48\x65\x6c\x6c\x6f"
    print(txt)   # Hello
    
    txt = "\u0048\u0065\u006c\u006c\u006f"
    print(txt)   # Hello
    
    txt = "\U00000048\U00000065\U0000006c\U0000006c\U0000006f"
    print(txt)   # Hello
    
    txt = "Hello World!"
    print(txt)   # Hello World!
    
    

Python can perform operations directly on the files.



False


True


Depends on the operation

Answer: True  # Python can perform operations directly on the files. 


Explanation:

    Python can perform operations directly on the files.
    The open() function is used to open a file.
    The open() function returns a file object.
    The open() function takes two parameters: filename and mode.
    The mode parameter is optional and the default value is r.
    The following example illustrates the open() function that opens a file in read mode.
    
    f = open("demofile.txt")   # opens a file in read mode
    print(f)   # <_io.TextIOWrapper name='demofile.txt' mode='r' encoding='cp1252'>
    
    The following example illustrates the open() function that opens a file in read mode.
    
    f = open("demofile.txt", "r")   # opens a file in read mode
    print(f)   # <_io.TextIOWrapper name='demofile.txt' mode='r' encoding='cp1252'>
    
    The following example illustrates the open() function that opens a file in write mode.
    
    f = open("demofile.txt", "w")   # opens a file in write mode
    print(f)   # <_io.TextIOWrapper name='demofile.txt' mode='w' encoding='cp1252'>
    
    The following example illustrates the open() function that opens a file in append mode.
    
    f = open("demofile.txt", "a")   # opens a file in append mode
    print(f)   # <_io.TextIOWrapper name='demofile.txt' mode='a' encoding='cp1252'>
    
    The following example illustrates the open() function that opens a file in read mode.
    

What do we need to do to interact with a file in Python?



Inside our program, we just need to open the file, python would close the file at the end of our program


Inside our program, we need to give the path of the file


Open the file inside our program, and close it at the end of the file's processing.

Answer: Open the file inside our program, and close it at the end of the file's processing.

      
We want to open a file and read some lines, and write at the end of the file.


Which mode in the open() function should we use?



write mode


read mode


update mode

Answer: update mode


How are files processed in Python?


A. By writing or reading from a file


B. By writing or reading from a variable stored in memory


C. By writing or reading from a stream saved in memory


D. Once a file is accessed with open(), it becomes an object



C, D


B


A, D

Answer: C, D

When we open a non-human readable file in Python, which class should handle it?



TextIOBase


BufferIOBase


RawIOBase


IOBase

Answer: RawIOBase or BufferedIOBase had doubts on this one.

Explanation (RawIOBase):
    The RawIOBase class is the raw stream IO base class.
    It inherits the IOBase class.
    The RawIOBase class is used to specify the interface for raw binary I/O.
    
    The following example illustrates the RawIOBase class that is used to specify the interface for raw binary I/O.
    
    class RawIOBase(_io._RawIOBase):
        def read(self, n=-1):
            raise NotImplementedError("should not be called")
        def write(self, b):
            raise NotImplementedError("should not be called")
        def readable(self):
            return False
        def writable(self):
            return False
        def seekable(self):
            return False
        def truncate(self, pos=None):
            raise NotImplementedError("should not be called")
        def flush(self):
            raise NotImplementedError("should not be called")
        def fileno(self):
            raise NotImplementedError("should not be called")
        def isatty(self):
            return False
        def __iter__(self):
            raise TypeError("not readable")
        def __next__(self):
            raise TypeError("not readable")
        def readall(self):
            raise NotImplementedError("should not be called")
        def readinto(self, b):
            raise NotImplementedError("should not be called")
        def readinto1(self, b):
            raise NotImplementedError("should not be called")
        def readline(self, limit=-1):
            raise NotImplementedError("should not be called")
        def readlines(self, hint=-1):
            raise NotImplementedError("should not be called")
        def writelines(self, lines):
            raise NotImplementedError("should not be called")
        def detach(self):
            raise NotImplementedError("should not be called")
        def read1(self, n=-1):
            raise NotImplementedError("should not be called")
        def peek(self, n=0):
            raise NotImplementedError("should not be called")
        def readinto(self, b):
            raise NotImplementedError("should not be called")
        def readinto1(self, b):
            raise NotImplementedError("should not be called")
            
explanation (BufferedIOBase):

    The BufferedIOBase class is the buffered stream IO base class.
    It inherits the IOBase class.
    The BufferedIOBase class is used to specify the interface for buffered I/O.
    The following example illustrates the BufferedIOBase class that is used to specify the interface for buffered I/O.
        
        
    class BufferedIOBase(IOBase):
        def read(self, n=None):
            raise NotImplementedError("should not be called")
        def read1(self, n=None):
            raise NotImplementedError("should not be called")
        def peek(self, n=0):
            raise NotImplementedError("should not be called")
        def readinto(self, b):
            raise NotImplementedError("should not be called")
        def readinto1(self, b):
            raise NotImplementedError("should not be called")
        def write(self, b):
            raise NotImplementedError("should not be called")
        def detach(self):
            raise NotImplementedError("should not be called")
        def readable(self):
            return True
        def writable(self):
            return True
        def seekable(self):
            return False
        def flush(self):
            raise NotImplementedError("should not be called")
        def truncate(self, pos=None):
            raise NotImplementedError("should not be called")
        def readall(self):
            raise NotImplementedError("should not be called")
        def readinto(self, b):
            raise NotImplementedError("should not be called")
        def readinto1(self, b):
            raise NotImplementedError("should not be called")
        def readline(self, limit=-1):
            raise NotImplementedError("should not be called")
        def readlines(self, hint=-1):
            raise NotImplementedError("should not be called")
        def writelines(self, lines):
            raise NotImplementedError("should not be called")
        def __iter__(self):
            raise TypeError("not readable")
        def __next__(self):
            raise TypeError("not readable")
        def fileno(self):
            raise io.UnsupportedOperation("fileno")
        def isatty(self):
            return False
            
            
The built-in function open() has a number of parameters. Some of them default to:


A. The file extension 'txt'


B. The read mode


C. The UTF-8 encoding


D. The update mode


E. The text mode



C, E


B, D


B, E


A, C

Answer: B, E


Select the correct answers for the code snippets below:


>>> f = open("file.txt", "w")
>>> f.close()


A. It deletes the file contents if the file already exists


B. It leaves the file contents unchanged if the file already exists


C. It creates the file file.txt if it does not exist


D. It raises the FileNotFoundError exception if the file does not exist



A, C


B, D

Answer: A, C


If we would like to open a file in Python and we are not sure if it exists, but if it does, we want to append to it, 
which mode should we use?


A. r+


B. a


C. w+


D. w



A, B


B, C


B, D

Answer: B, C    

Explanation:

Which of the following modes suits the case where we want to read a file and append to it at the end, without worrying about the file's write permissions?



w+


a


r+

Answer: w+ or a had doubts on this one.

    
When using errno for analyzing errors related to files' streams, Python has a list of code names related to these. Which of the following are they?


A. errno.EEXIST (File exists)


B. errno.EFBIG (Filename too large)


C. errno.EMFILE (Bad encoding in the file)


D. errno.ENOENT (No such file or directory)


E. errno.ENOSPC (No space left in memory)



B, C


C, E


A, D


B, E

Answer: A, D 

Explanation:
    The errno module defines the symbolic error codes.
    The errno module defines the following symbolic error codes:
        errno.EPERM (Operation not permitted)
        errno.ENOENT (No such file or directory)
        errno.ESRCH (No such process)
        errno.EINTR (Interrupted system call)
        errno.EIO (I/O error)
        errno.ENXIO (No such device or address)
        errno.E2BIG (Argument list too long)
        errno.ENOEXEC (Exec format error)
        errno.EBADF (Bad file descriptor)
        errno.ECHILD (No child processes)
        errno.EAGAIN (Try again)
        errno.ENOMEM (Out of memory)
        errno.EACCES (Permission denied)
        errno.EFAULT (Bad address)
        errno.ENOTBLK (Block device required)
        errno.EBUSY (Device or resource busy)
        errno.EEXIST (File exists)
        errno.EXDEV (Cross-device link)
        errno.ENODEV (No such device)
        errno.ENOTDIR (Not a directory)
        errno.EISDIR (Is a directory)
        errno.EINVAL (Invalid argument)
        errno.ENFILE (File table overflow)
        errno.EMFILE (Too many open files)
        errno.ENOTTY (Not a typewriter)
        errno.ETXTBSY (Text file busy)
        errno.EFBIG (File too large)
        errno.ENOSPC (No space left on device)
        errno.ESPIPE (Illegal seek)
        errno.EROFS (Read-only file system)
        errno.EMLINK (Too many links)
        errno.EPIPE (Broken pipe)
        errno.EDOM (Math argument out of domain of func)
        errno.ERANGE (Math result not representable)
        errno.EDEADLK (Resource deadlock would occur)
        errno.ENAMETOOLONG (File name too long)
        errno.ENOLCK (No record locks available)
        errno.ENOSYS (Function not implemented)
        errno.ENOTEMPTY (Directory not empty)
        errno.ELOOP (Too many symbolic links encountered)
        errno.EWOULDBLOCK (Operation would block)
        errno.ENOMSG (No message of desired type)
        errno.EIDRM (Identifier removed)
        errno.ECHRNG (Channel number out of range)
        errno.EL2NSYNC (Level 2 not synchronized)
        errno.EL3HLT (Level 3 halted)
        errno.EL3RST (Level 3 reset)
        errno.ELNRNG (Link number out of range)
        errno.EUNATCH (Protocol driver not attached)
        errno.ENOCSI (No CSI structure available)
        errno.EL2HLT (Level 2 halted)
        errno.EBADE (Invalid exchange)
        errno.EBADR (Invalid request descriptor)
        errno.EXFULL (Exchange full)
        errno.ENOANO (No anode)
        errno.EBADRQC (Invalid request code)
        errno.EBADSLT (Invalid slot)
        errno.EDEADLOCK (Resource deadlock would occur)
        errno.EBFONT (Bad font file format)
        errno.ENOSTR (Device not a stream)
        errno.ENODATA (No data available)
        errno.ETIME (Timer expired)
        errno.ENOSR (Out of streams resources)
        
        
Open the file f_error.py, and complete the code so that the exceptions raised give insight on what went wrong.


CheckCompleteIncomplete
Check Code

import errno

try:
    stream = open("filename", "r")
    print("File exists")
    stream.close()
except # complete the code
    # check if file does not exist
        print("The file doesn't exist")
    else:
        print("Something went wrong")

try:
    stream = open("filename", "r")
    print("File exists")
    stream.close()
except FileNotFoundError:  # Catch the exception for file not found
    print("The file doesn't exist")
except Exception as e:  # Catch other exceptions
    print(f"Something went wrong: {e}")

It is considered good practice to always open files with a try/except block, since file permissions or name errors 
are encountered regularly. Moreover, Python offers the default streams when we run our programs:


sys.stdin, sys.stdout and sys.stderr. They can be useful since they can be stored and evaluated according to a 
program's needs. For example, sometimes we want to test a program by capturing any errors when we call this program 
from another file, or we want to capture the output of some code while we are running it.

Ok

# working with real file 

What does the read() function return when applied to a file object?



specific amount of characters in the file as a string


the first line of the file as a sting


a list of all characters in the file


all characters of the file as a string, if no argument is provided

Answer: all characters of the file as a string, if no argument is provided

Explanation:
    The read() function returns all characters of the file as a string, if no argument is provided.
    The read() function returns the specified number of characters of the file as a string, if an argument is provided.
    The following example illustrates the read() function that returns all characters of the file as a string, if no argument is provided.
    
    f = open("demofile.txt", "r")
    print(f.read())   # Hello World!
    f.close()
    
    The following example illustrates the read() function that returns the specified number of characters of the file as a string, if an argument is provided.
    
    f = open("demofile.txt", "r")
    print(f.read(5))   # Hello
    f.close()
    
    The following example illustrates the read() function that returns the specified number of characters of the file as a string, if an argument is provided.
        
    f = open("demofile.txt", "r")
    print(f.read(5))   # Hello
    print(f.read(5))   # World
    f.close()
    
    The following example illustrates the read() function that returns the specified number of characters of the file as a string, if an argument is provided.
    
    f = open("demofile.txt", "r")
    print(f.read(5))   # Hello
    print(f.read(5))   # World
    print(f.read(5))   # !
    f.close()
    
    The following example illustrates the read() function that returns the specified number of characters of the file as a string, if an argument is provided.
    
    f = open("demofile.txt", "r")
    print(f.read(5))   # Hello
    print(f.read(5))   # World
    print(f.read(5))   # !
    print(f.read(5))   # ?
    f.close()
    
    The following example illustrates the read() function that returns the specified number of characters of the file as a string, if an argument is provided.
    
    f = open("demofile.txt", "r")
    print(f.read(5))   # Hello
    print(f.read(5))   # World
    print(f.read(5))   # !
    print(f.read(5))   # ?
    print(f.read(5))   #
    f.close()
    
    The following example illustrates the read() function that returns the specified number of characters of the file as a string, if an argument is provided.
    
    f = open("demofile.txt", "r")
    print(f.read(5))   # Hello
    print(f.read(5))   # World
    print(f.read(5))   # !
    print(f.read(5))   # ?
    print(f.read(5))   #
    print(f.read(5))   #
    f.close()

How can we create a bytes stream in Python?



with the built-in function bytearray()


with the built-in class bytearray()


with the built-in class bytes()


with the built-in function bytes()

Answer: with the built-in class bytearray() or bytes() had doubts on this one.

Explanation:


    
How can we open a video file in Python?


A.

>>> vf = open("video.mkv", "rb")
>>> video = bytearray(vf.read(100)) # up to 100 bytes


B.

>>> vf = open("video.mkv", "rb")
>>> video = bytearray(vf))


C.

>>> vf = open("video.mkv", "r")
>>> video = bytearray(vf))


A


C


B

Answer: A

Explanation:
    A is the most common way to open a video file in Python.


How can we read a video file in Python?


A.

>>> vf = open("video.mp4", 'rb')
>>> buffer = bytearray(1024)
>>> readin = vf.readlines(buffer)


B.

>>> vf = open("video.mp4", 'rb')
>>> buffer = bytearray(1024)
>>> readin = vf.read(buffer)


C.

>>> vf = open("video.mp4", 'rb')
>>> buffer = bytearray(1024)
>>> readin = vf.readinto(buffer)


C


B


A

Answer: C

Explanation:
    C is the most common way to read a video file in Python.
    
    The readinto() function reads bytes into a pre-allocated, writable bytes-like object b, and returns the number of bytes read.
    The readinto() function returns the number of bytes read.
    The following example illustrates the readinto() function that reads bytes into a pre-allocated, writable bytes-like object b, and returns the number of bytes read.
    
    f = open("demofile.txt", "r")
    b = bytearray(5)
    print(f.readinto(b))   # 5
    print(b)   # bytearray(b'Hello')
    f.close()

If we open a non-zero size file in write mode, what is the output of the following code?


try:
    f = open("file.txt", "w")
    print(len(f.readlines()))
except Exception as e:
    print(e)
finally:
    f.close()

NameError


not readable


errno.EEXIST


file doesn't exist

Answer: not readable

Explanation:
    The write mode truncates the file to zero length or creates a new file if it does not exist.
    

Open the file lipogram.py, and complete the code. The program should read a text file and check whether a specific letter is found and how many times in a file.


Follow the instructions in the file comments.


Note: We provide a text file for this exercise, called oulipo.txt. Oulipo is a loose gathering of mostly French-speaking writers and mathematicians who seek to create works using constrained writing techniques. The poem is an excerpt of "Fate of Nassan", an anonymous poem dating from pre-1870, where every letter of the alphabet except E is used.


from os import strerror


def lipogram(letter):
    letter.lower()
    # Write a try/except block to open the oulipo file
    # use the absolute path /root/code/oulipo.txt
    # and handle an IOError
    try:

    except IOError as e:
        # print the error with the use of strerror and errno
        txt = None
    except Exception as e:
        print(e)
    else:
        # Do the count here using sum(), map(), lambda
        # to count occurences of the letter
        print(letter, "appears", count, "times")
    finally:
        if txt:
            txt.close()


lipogram("E")

from os import strerror

def lipogram(letter):
    letter = letter.lower()  # Fix: Convert letter to lowercase

    try:
        # Open the oulipo file using the absolute path
        with open("/root/code/oulipo.txt", "r") as txt:
            text = txt.read()
            count = sum(map(lambda x: x.lower() == letter, text))
    except IOError as e:
        print("I/O error:", strerror(e.errno))
    except Exception as e:
        print(e)
    else:
        print(letter, "appears", count, "times")
    finally:
        if 'txt' in locals():
            txt.close()

lipogram("E")


Sometimes we may need to format text in HTML for sending emails from our code, or for generating HTML documents dynamically.


Open the file html.py, and complete the code so that each line has its first character wrapped in bold tags. Use the HTML notation <b></b>


Note: we make use of the same oulipo.txt file.


Expected output:


<b>B</b>old Nassan quits his caravan,


<b>A</b> hazy mountain grot to scan;


<b>C</b>limbs jaggy rocks to find his way,


<b>D</b>oth tax his sight, but far doth stray.


CheckCompleteIncomplete
Code Check

f = open("/root/code/oulipo.txt", "r")
# Read the lines of the file

# Iterate through the lines
    # fetch the first char of each line
    # print the line with its first char wrapped

olipo.txt file 
Bold Nassan quits his caravan,
A hazy mountain grot to scan;
Climbs jaggy rocks to find his way,
Doth tax his sight, but far doth stray.



***************************************************************************************************

OS module in Python

Which of the following attributes are listed with os.uname()?



All of the above


machine architecture


Local name of machine


Kernel/OS release


OS version


Operating System (OS)

Answer: All of the above

Explanation:
    The os.uname() function returns the following attributes:
        machine architecture
        Local name of machine
        Kernel/OS release
        OS version
        Operating System (OS)
    The following example illustrates the os.uname() function that returns the following attributes:    
    
    import os
    print(os.uname())  # posix.uname_result(sysname='Linux', nodename='ip-172-31-22-247', release='4.14.225-169.362.amzn2.x86_64', version='#1 SMP Wed Nov 18 19:05:20 UTC 2020', machine='x86_64')
    
    The following example illustrates the os.uname() function that returns the following attributes:


The module os provides the property name, which based on your system, outputs one of three names:


posix (if you use a Unix OS (Linux, MacOS, raspberry-pi)


nt (if you use Windows)


java (if your code is written in something like Jython)



Ok

Which of the following commands would create a new directory?



os.chdir("/home/python/coding")


os.rmdir("/home/python/coding")


os.listdir("/home/python/coding")


os.mkdir("/home/python/coding")

Answer: os.mkdir("/home/python/coding")

Explanation:
    The os.mkdir() function creates a new directory.
    The os.mkdir() function takes one parameter: path.
    The os.mkdir() function returns None.
    The following example illustrates the os.mkdir() function that creates a new directory.
    
    import os
    os.mkdir("/home/python/coding")
    
    
Which of the following commands would recursively delete subdirectories?



os.removedirs("/home/python/coding")


os.rmdir("/home/python/*")

Answer: os.removedirs("/home/python/coding")

Explanation:
    The os.removedirs() function recursively deletes subdirectories.
    The os.removedirs() function takes one parameter: path.
    The os.removedirs() function returns None.
    The following example illustrates the os.removedirs() function that recursively deletes subdirectories.
    
    import os
    os.removedirs("/home/python/coding")
    
    
How can we execute shell commands from within Python?



os.system("cd")


os.path("cd")


os.sys("cd")


os.chdir("cd")

Answer: os.system("cd")

Explanation:

    The os.system() function executes the command (a string) in a subshell.
    The os.system() function takes one parameter: command.
    The os.system() function returns the exit status of the command.
    The following example illustrates the os.system() function that executes the command (a string) in a subshell.
    
    import os
    os.system("cd")
    
    
What is the output of the following code snippet?


import os

os.mkdir("python")
print(os.listdir())

'python'


['python']


('python')

Answer: ['python']

Explanation:
    The os.listdir() function returns a list containing the names of the entries in the directory given by path.
    The os.listdir() function takes one parameter: path.
    The os.listdir() function returns a list.
    The following example illustrates the os.listdir() function that returns a list containing the names of the entries in the directory given by path.
    
    import os
    print(os.listdir())   # ['python']
    os.tupledir()   # AttributeError: module 'os' has no attribute 'tupledir'
    os.dictdir()   # AttributeError: module 'os' has no attribute 'dictdir'
    os.listdir()   # ['python']
    
What is the output of the following code snippet?


import os

os.mkdir("python/examples/docs")
os.chdir("python/examples")
print(os.listdir())

['python']


['examples/docs']


FileNotFoundError


[]


['docs']

Answer: ['docs'] or file not fount error -->  doubts on this one. 

Explanation:
    The os.listdir() function returns a list containing the names of the entries in the directory given by path.
    The os.listdir() function takes one parameter: path.
    The os.listdir() function returns a list.
    The following example illustrates the os.listdir() function that returns a list containing the names of the entries in the directory given by path.
    
    import os
    os.mkdir("python/examples/docs")
    os.chdir("python/examples") to change the directory to python/examples directory 
    Now the current working directory is python/examples directory
    
    print(os.listdir())   # ['docs']
    
What is the output of the following code snippet?


import os

os.makedirs("/dir/inner_dir1/inner_dir2/inner_dir3")
os.chdir("/dir/inner_dir1/inner_dir2/inner_dir3")
os.chdir("../../")
print(os.getcwd())

'/dir/inner_dir1'


'/dir/inner_dir1/inner_dir2'


'/'


'/dir'

Answer: '/dir/inner_dir1

Explanation:
    The os.getcwd() function returns the current working directory.
    The os.getcwd() function takes no parameters.
    The os.getcwd() function returns a string.
    The following example illustrates the os.getcwd() function that returns the current working directory.
    
    import os
    os.makedirs("/dir/inner_dir1/inner_dir2/inner_dir3")
    os.chdir("/dir/inner_dir1/inner_dir2/inner_dir3/inner_dir4")
    os.chdir("../../")
    print(os.getcwd()) # /dir/inner_dir1/inner_dir2
    
    
    
What is the output of the following code snippet, if dir3 already exists?


import os

os.makedirs("/dir/dir1/dir2/dir3")
os.chdir("./dir1/dir2/dir3")
os.getcwd()

FileExistsError


the code will overwrite the existing dir3


'/dir/dir1/dir2/dir3'


DirExistsError

Answer: FileExistsError

Explanation:
    The os.makedirs() function creates a directory named path with a numeric mode mode.
    The os.makedirs() function takes two parameters: path and mode.
    The os.makedirs() function returns None.
    The following example illustrates the os.makedirs() function that creates a directory named path with a numeric mode mode.
    
    import os
    os.makedirs("/dir/dir1/dir2/dir3")
    os.chdir("./dir1/dir2/dir3")    # FileNotFoundError: [Errno 2] No such file or directory: './dir1/dir2/dir3'
    os.getcwd()   # FileNotFoundError: [Errno 2] No such file or directory: './dir1/dir2/dir3'
    


    
All the best!
You are now fully ready to crack the PCAP Certification.

Head over to the below-shared link to enroll in the Certification Exam. Remember to keep the code – KODEKLOUD20 – handy for a 20% discount while registering for the exam.

Click here to purchase the PCAP EXAM: https://pythoninstitute.org/pcap





"""