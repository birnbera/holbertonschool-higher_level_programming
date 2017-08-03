## 0x02. Python - import & modules
#### 0. Import a simple function from a simple file mandatory
Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
  - You have to use `print` function with string format to display integers
  - You have to assign:
    - the value `1` to a variable called `a`
    - the value `2` to a variable called `b`
    - and use those two variables as arguments when calling the functions `add` and `print`
  - Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
  - You can only use the word `add_0` once in your code
  - You are not allowed to use `*` for importing
  - Your code should not be executed when imported
#### 1. My first toolbox! mandatory
  - Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
  - Do not use the function `print` (with string format to display integers) more than 4 times
  - You have to define:
    - the value `10` to a variable `a`
    - the value `5` to a variable `b`
    - and use those two variables only, as arguments when calling functions (included `print`)
  - Your program should call each of the imported functions. See example bellow for format
  - the word `calculator_1` should be used only once in your file
  - You are not allowed to use `*` for importing
  - Your code should not be executed when imported
#### 2. How to make a script dynamic! mandatory
Write a program that prints the number of and the list of its arguments.
  - The output should be:
    - Number of argument(s) followed by `argument` or `arguments`, followed by
    - `:` (or `.` if no argument where passed) followed by
    - a new line, followed by (if at least one argument),
    - one line per argument:
      - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
  - Your code should not be executed when imported
  - The number of elements of `argv` can be retrieved by using: `len(argv)`
  - You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (preferred in a near Future), if you know them you can use them.
#### 3. Infinite addition mandatory
Write a program that prints the result of the addition of all arguments
  - The output should be the result of the addition of all arguments, followed by a new line
  - You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
  - Your code should not be executed when imported
#### 4. Who are you? mandatory
Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc) (please download it locally).

  - You should print one name per line, in alpha order
  - You should print only names that do **not** start with `__`
  - Your code should not be executed when imported
#### 5. Everything can be imported mandatory
Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
  - You are not allowed to use `*` for importing
  - Your code should not be executed when imported
