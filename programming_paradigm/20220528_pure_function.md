# Pure function

[TOC]

## Metadata

|        |                        |
| ------ | ---------------------- |
| Author | @jasontr               |
| Date   | 20220528               |
| About  | Functional Programming |

## a simple function

```python
num1 = 0
def func1(num2):
    num1 += 1
    return num1 + num2
for i in range(4):
    print(func1(1))
# print 2
# print 3
# print 4
# print 5
```

We call the function `func1` in the same way but get a different result every time.  For func1 we do not have a one-to-one mapping of input and output. We call this function stateful. 

stateful

For every x has multiple y

![img](https://jigsawye.gitbooks.io/mostly-adequate-guide/content/images/relation-not-function.gif)

stateless

For every x has a fixed y

![img](https://jigsawye.gitbooks.io/mostly-adequate-guide/content/images/function-sets.gif)



We can't control output by a confirmed input for a stateful function. 

How to make it stateless.

## change it to  `pure function` (stateless)

```python
num1 = 0
def pure_func1(_num1, num2):
    return _num1 + num2
for i in range(4):
    num1 += 1
    print(pure_func1(num1, 1))
# print 2
# print 3
# print 4
# print 5
```

## Why pure function

Easy to parallel processing

Pure function describes how inputs relate to outputs, without spelling out the steps to get from A to B. This can **simplify systems** and, **referential transparency** in the face of concurrency.

in details 

- Cacheable

  - for the same input, we just evaluate once

    ```python
    _dict = {}
    def pure_func2(a):
        return a * a
    
    def calc_square(a):
        if a in _dict:
            return _dict.get(a)
        else:
            _dict[a] = pure_func2(a)
            return _dict.get(a)
    ```

    

- Portable/Self-Documenting

  - can use anywhere
  - What you see is what you get

- Testable

  - you don't need to mock anything

- Reasonable

  - referential transparency

  - you can replace function call to result

    ```python
    # stateful one
    num1 = 0
    print(func1(1))
    print(func1(1))
    # print 2
    # print 3
    
    num1 = 0
    print(2)
    print(func1(1))
    # print 2
    # print 2
    -------------------------------
    # pure function
    num1 = 0
    num1 += 1
    print(func1(num1, 1))
    num1 += 1
    print(func1(num1, 1))
    # print 2
    # print 3
    
    num1 = 0
    num1 += 1
    print(2)
    num1 += 1
    print(func1(num1, 1))
    # print 2
    # print 3
    ```

## Pure function in Data processing (mapping)

what is map

a list of inputs mapping to a list of  output

```python
import multiprocess as m
pool = m.Pool(5)
def function(a):
    return a
pool.map(function, list)
```



=> To be continued

