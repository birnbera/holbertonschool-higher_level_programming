<h1 class="gap">0x0A. Python - Inheritance</h1>
  <h4 class="task">
    0. Lookup
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns the list of available attributes and methods of an object:</p>

<ul>
<li>Prototype: <code>def lookup(obj):</code></li>
<li>Returns a <code>list</code> object</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    1. My list
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>MyList</code> that inherits from <code>list</code>:</p>

<ul>
<li>Public instance method: <code>def print_sorted(self):</code> that prints the list, but sorted (ascending sort)</li>
<li>You can assume that all the elements of the list will be of type <code>int</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    2. Exact same object
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns <code>True</code> if the object is <em>exactly</em> an instance of the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def is_same_class(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    3. Same class or inherit from
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns <code>True</code> if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def is_kind_of_class(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    4. Only sub class of
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns <code>True</code> if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def inherits_from(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    5. Geometry module
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write an empty class <code>BaseGeometry</code>.</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    6. Improve Geometry
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>BaseGeometry</code> (based on <code>5-base_geometry.py</code>).</p>

<ul>
<li>Public instance method: <code>def area(self):</code> that raises an <code>Exception</code> with the message <code>area() is not implemented</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    7. Integer validator
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>BaseGeometry</code> (based on <code>6-base_geometry.py</code>).</p>

<ul>
<li>Public instance method: <code>def area(self):</code> that raises an <code>Exception</code> with the message <code>area() is not implemented</code></li>
<li>Public instance method: <code>def integer_validator(self, name, value):</code> that validates <code>value</code>:

<ul>
<li>you can assume <code>name</code> is always a string</li>
<li>if <code>value</code> is not an integer: raise a <code>TypeError</code> exception, with the message <code>&lt;name&gt; must be an integer</code></li>
<li>if <code>value</code> is less or equal to 0: raise a <code>ValueError</code> exception with the message <code>&lt;name&gt; must be greater than 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    8. Rectangle
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).</p>

<ul>
<li>Instantiation with <code>width</code> and <code>height</code>: <code>def __init__(self, width, height):</code>

<ul>
<li><code>width</code> and <code>height</code> must be private. No getter or setter</li>
<li><code>width</code> and <code>height</code> must be positive integers, validated by <code>integer_validator</code></li>
</ul></li>
</ul>
  <h4 class="task">
    9. Full rectangle
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
(task based on <code>8-rectangle.py</code>)</p>

<ul>
<li>Instantiation with <code>width</code> and <code>height</code>: <code>def __init__(self, width, height):</code>:

<ul>
<li><code>width</code> and <code>height</code> must be private. No getter or setter</li>
<li><code>width</code> and <code>height</code> must be positive integers validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
<li><code>print()</code> should print, and <code>str()</code> should return, the following rectangle description: <code>[Rectangle] &lt;width&gt;/&lt;height&gt;</code></li>
</ul>
  <h4 class="task">
    10. Square #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>):</p>

<ul>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size):</code>:

<ul>
<li><code>size</code> must be private. No getter or setter</li>
<li><code>size</code> must be a positive integer, validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
</ul>
  <h4 class="task">
    11. Square #2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>).
(task based on <code>10-square.py</code>).</p>

<ul>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size):</code>:

<ul>
<li><code>size</code> must be private. No getter or setter</li>
<li><code>size</code> must be a positive integer, validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
<li><code>print()</code> should print, and <code>str()</code> should return, the square description: <code>[Square] &lt;width&gt;/&lt;height&gt;</code></li>
</ul>
  <h4 class="task">
    12. My integer
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>MyInt</code> that inherits from <code>int</code>:</p>

<ul>
<li><code>MyInt</code> is a rebel. <code>MyInt</code> has <code>==</code> and <code>!=</code> operators inverted</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    13. Can I?
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that adds a new attribute to an object if it&#39;s possible:</p>

<ul>
<li>Raise a <code>TypeError</code> exception, with the message <code>can&#39;t add new attribute</code> if the object can&#39;t have new attribute</li>
<li>You are not allowed to use <code>try/catch</code></li>
<li>You are not allowed to import any module</li>
</ul>
