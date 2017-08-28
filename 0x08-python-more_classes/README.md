<h2>0x08. Python - More Classes and Objects</h2>
  <h4 class="task">
    0. Simple rectangle
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    1. Real definition of a rectangle
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>0-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    2. Area and Perimeter
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>1-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    3. String representation
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>2-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    4. Eval is magic
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>3-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    5. Detect instance deletion
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>4-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message &quot;Bye rectangle...&quot; when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    6. How many instances
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message &quot;Bye rectangle...&quot; when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    7. Change representation
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>6-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message &quot;Bye rectangle...&quot; when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    8. Compare rectangles
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>7-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message &quot;Bye rectangle...&quot; when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    9. A square is a rectangle
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>8-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message &quot;Bye rectangle...&quot; when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code></li>
<li>You are not allowed to import any module</li>
</ul>
