## 0x03. Python - Data Structures: Lists, Tuples
  <h4 class="task">
    0. Print a list of integers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that prints all integers of a list.</p>

<ul>
<li>Prototype: <code>def print_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

  <h4 class="task">
    1. Secure access to an element in a list
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that retrieves an element from a list.</p>

<ul>
<li>Prototype: <code>def element_at(my_list, idx):</code></li>
<li>If <code>idx</code> is out of range, the function should return <code>None</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

  <h4 class="task">
    2. Replace element
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that replaces an element of a list at a specific position.</p>

<ul>
<li>Prototype: <code>def replace_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is out of range, the function should not modify anything, and returns the original list</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

  <h4 class="task">
    3. Print a list of integers... in reverse!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that prints all integers of a list, in reverse order.</p>

<ul>
<li>Prototype: <code>def print_reversed_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

  <h4 class="task">
    4. Replace in a copy
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that replaces an element in a list at a specific position without modifying the original list.</p>

<ul>
<li>Prototype: <code>def new_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is out of range, the function should return a copy of the original <code>list</code></li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

  <h4 class="task">
    5. Can you C me now?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that removes all characters <code>c</code> and <code>C</code> from a string.</p>

<ul>
<li>Prototype: <code>def no_c(my_string):</code></li>
<li>The function shoud return the new string</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.replace()</code></li>
</ul>

  <h4 class="task">
    6. Lists of lists = Matrix
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that prints a matrix of integers.</p>

<ul>
<li>Prototype: <code>def print_matrix_integer(matrix=[[]]):</code></li>
<li>Format: see example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

  <h4 class="task">
    7. Tuples addition
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that adds 2 tuples.</p>

<ul>
<li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code></li>
<li>Returns a tuple with 2 integers:

<ul>
<li>The first element should be the addition of the first element of each argument</li>
<li>The second element should be the addition of the second element of each argument</li>
</ul></li>
<li>You are not allowed to import any module</li>
<li>You can assume that the two tuples will only contain integers</li>
<li>If a tuple is smaller than 2, use the value <code>0</code> for each missing integer</li>
<li>If a tuple is bigger than 2, use only the first 2 integers</li>
</ul>

  <h4 class="task">
    8. More returns!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns a tuple with the length of a string and its first character.</p>

<ul>
<li>Prototype: <code>def multiple_returns(sentence):</code></li>
<li>If the sentence is empty, the first character should be equal to <code>None</code></li>
<li>You are not allowed to import any module</li>
</ul>

  <h4 class="task">
    9. Find the max
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that finds the biggest integer of a list. </p>

<ul>
<li>Prototype: <code>def max_integer(my_list=[]):</code></li>
<li>If the list is empty, return <code>None</code></li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use the builtin <code>max()</code></li>
</ul>

  <h4 class="task">
    10. Only by 2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that finds all multiples of 2 in a list.</p>

<ul>
<li>Prototype: <code>def divisible_by_2(my_list=[]):</code></li>
<li>Return a new list with <code>True</code> or <code>False</code>, depending on wether the integer at the same position in the original list is a multiple of 2</li>
<li>The new list should have the same size as the original list</li>
<li>You are not allowed to import any module</li>
</ul>

  <h4 class="task">
    11. Delete at
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that deletes the item at a specific position in a list.</p>

<ul>
<li>Prototype: <code>def delete_at(my_list=[], idx=0):</code></li>
<li>You are not allowed to use <code>pop()</code></li>
<li>You are not allowed to import any module</li>
</ul>

  <h4 class="task">
    12. Switch
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Complete the source code in order to switch value of <code>a</code> and <code>b</code></p>

<ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py">here</a></li>
<li>Your code should be inserted where the comment is (line 4)</li>
<li>Your program should be exactly 5 lines long</li>
</ul>

  <h4 class="task">
    13. CPython #0: Python lists
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.<br />
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let&#39;s have fun with Python and C, and let&#39;s look at what makes Python so easy to use.</p>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/241/giphy-3.gif" alt="CPython">
<br /><br />
Create a C function that prints some basic info about Python lists.</p>

<ul>
<li>Prototype: <code>void print_python_list_info(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Python version: 3.4</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c</code></li>
<li>OS: <code>Ubuntu 14.04 LTS</code></li>
<li>Start by reading:

<ul>
<li>listobject.h</li>
<li>object.h</li>
<li><a href="https://docs.python.org/3.4/c-api/structures.html">Common Object Structures</a></li>
<li><a href="https://docs.python.org/3.4/c-api/list.html">List Objects</a></li>
</ul></li>
</ul>
