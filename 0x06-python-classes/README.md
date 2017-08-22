## 0x06. Python - Classes and Objects
  <h4 class="task">
    0. My first square
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write an empty class <code>Square</code> that defines a square:</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    1. Square with size
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>0-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with <code>size</code> (no type/value verification)</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    2. Size validation
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>1-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    3. Area of a square
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>2-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    4. Access and update private attribute
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>3-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    5. Printing a square
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    6. Coordinates of a square
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>5-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>position</code>:

<ul>
<li>property <code>def position(self):</code> to retrieve it</li>
<li>property setter <code>def position(self, value):</code> to set it:

<ul>
<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code><br></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
<li><code>position</code> should be use by using space</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    7. Singly linked list
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Node</code> that defines a node of a singly linked list by: </p>

<ul>
<li>Private instance attribute: <code>data</code>:

<ul>
<li>property <code>def data(self):</code> to retrieve it</li>
<li>property setter <code>def data(self, value):</code> to set it:

<ul>
<li><code>data</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>data must be an integer</code><br></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>next_node</code>:

<ul>
<li>property <code>def next_node(self):</code> to retrieve it</li>
<li>property setter <code>def next_node(self, value):</code> to set it:

<ul>
<li><code>next_node</code> can be <code>None</code> or must be a <code>Node</code>, otherwise raise a <code>TypeError</code> exception with the message <code>next_node must be a Node object</code><br></li>
</ul></li>
</ul></li>
<li>Instantiation with <code>data</code> and <code>next_node</code>: <code>def __init__(self, data, next_node=None):</code></li>
</ul>

<p>And, write a class <code>SinglyLinkedList</code> that defines a singly linked list by: </p>

<ul>
<li>Private instance attribute: <code>head</code> (no setter or getter)</li>
<li>Simple instantiation: <code>def __init__(self):</code></li>
<li>Should be printable:

<ul>
<li>print the entire list in stdout</li>
<li>one node number by line</li>
</ul></li>
<li>Public instance method: <code>def sorted_insert(self, value):</code> that inserts a new <code>Node</code> into the correct sorted position in the list (increasing order)</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    8. Print Square instance
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>6-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>position</code>:

<ul>
<li>property <code>def position(self):</code> to retrieve it</li>
<li>property setter <code>def position(self, value):</code> to set it:

<ul>
<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integer</code><br></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
<li><code>position</code> should be use by using space</li>
</ul></li>
<li>Printing a <code>Square</code> instance should have the same behavior as <code>my_print()</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    9. Compare 2 squares
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be a number (float or integer), otherwise raise a <code>TypeError</code> exception with the message <code>size must be a number</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li><code>Square</code> instance can answer to comparators: <code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code> and <code>&lt;=</code> based on the square area</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    10. ByteCode -&gt; Python #5
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write the Python class <code>MagicClass</code> that does exactly the same as the following Python bytecode:</p>

<pre><code>Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 (&#39;radius must be a number&#39;)
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     &gt;&gt;   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
</code></pre>

<ul>
<li>Tip: <a href="https://docs.python.org/3.4/library/dis.html">Python bytecode</a></li>
</ul>
