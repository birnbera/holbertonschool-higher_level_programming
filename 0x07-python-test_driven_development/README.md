## 0x07. Python - Test-driven development
  <h4 class="task">
    0. Integers addition
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that adds 2 integers.</p>

<ul>
<li>Prototype: <code>def add_integer(a, b):</code></li>
<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    1. Divide a matrix
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that divides all elements of a matrix.</p>

<ul>
<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
<li><code>div</code> can&#39;t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
<li>Returns a new matrix</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    2. Say my name
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that prints &quot;My name is <first name> <last name>&quot;</p>

<ul>
<li>Prototype: <code>def say_my_name(first_name, last_name=&quot;&quot;):</code></li>
<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    3. Print square
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that prints a square with the character <code>#</code>.</p>

<ul>
<li>Prototype: <code>def print_square(size):</code></li>
<li><code>size</code> is the size length of the square</li>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    4. Text indentation
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that prints a text with 2 new lines after each of those characters: <code>.</code>, <code>?</code> and <code>:</code></p>

<ul>
<li>Prototype: <code>def text_indentation(text):</code></li>
<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
<li>There should be no space at the beginning or at the end of each printed line</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    5. Max integer - Unittest
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Since the beginning you are creating &quot;Interactive tests&quot;. For this exercise, you will add Unittests.</p>

<p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>

<ul>
<li>Your test file should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest">unittest module</a> </li>
<li>Your test file should be python files (extension: <code>.py</code>)</li>
<li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code></li>
<li>We strongly encourage you to work together on test cases, so that you don&#39;t miss any edge case</li>
</ul>
  <h4 class="task">
    6. Matrix multiplication
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that multiplies 2 matrices:</p>

<ul>
<li><p>Read: <a href="https://en.wikipedia.org/wiki/Matrix_multiplication">Matrix multiplication - only Matrix product (two matrices)</a></p></li>
<li><p>Prototype: <code>def matrix_mul(m_a, m_b):</code></p></li>
<li><p><code>m_a</code> and <code>m_b</code> must be an list of lists of integers or floats </p>

<ul>
<li>if <code>m_a</code> or <code>m_b</code> us not a list: raise a <code>TypeError</code> exception with the message <code>m_a must be a list</code> or <code>m_b must be a list</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is empty: raise a <code>ValueError</code> exception with the message <code>m_a can&#39;t be empty</code> or <code>m_b can&#39;t be empty</code></li>
<li>if one element of those two lists is not an integer or a float: raise a <code>TypeError</code> exception with the message <code>m_a should contain only integers or floats</code> or <code>m_b should contain only integers or floats</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is not a rectangle (all &#39;rows&#39; should be of the same size): raise a <code>TypeError</code> exception with the message <code>each row of m_a must should be of the same size</code> or <code>each row of m_b must should be of the same size</code></li>
</ul></li>
<li><p>If <code>m_a</code> and <code>m_b</code> can&#39;t be multiplied: raise a <code>ValueError</code> exception with the message <code>m_a and m_b can&#39;t be multiplied</code></p></li>
<li><p>You are not allowed to import any module</p></li>
</ul>
  <h4 class="task">
    7. Lazy matrix multiplication
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that multiplies 2 matrices by using the module <a href="http://www.numpy.org">NumPy</a></p>

<p>To install it: <code>pip3 install numpy</code></p>

<ul>
<li>Prototype: <code>def lazy_matrix_mul(m_a, m_b):</code></li>
<li>Test cases should be the same as <code>100-matrix_mul</code> but with new exception type/message</li>
</ul>
  <h4 class="task">
    8. CPython #3: Python Strings
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-5.gif" alt="Gif">
<br /></p>

<p>Create a function that prints Python strings.</p>

<ul>
<li>Prototype: <code>void print_python_string(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid string, print an error message (see example)</li>
<li>Read: <a href="https://docs.python.org/3.4/howto/unicode.html">Unicode HOWTO</a></li>
</ul>

<p>About:</p>

<ul>
<li>Python version: 3.4</li>
<li>You are allowed to use the C standard library</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Wextra -pedantic -Werror -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c</code></li>
</ul>
