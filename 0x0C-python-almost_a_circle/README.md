<h1 class="gap">0x0C. Python - Almost a circle</h1>
  <h4 class="task">
    0. If it&#39;s not tested it doesn&#39;t work
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>All your files, classes and methods must be unit tested and be PEP 8 validated. </p>
  <h4 class="task">
    1. Base class
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write the first class <code>Base</code>:</p>

<p>Create a folder named <code>models</code> with an empty file <code>__init__.py</code> inside - with this file, the folder will become a Python module</p>

<p>Create a file named <code>models/base.py</code>:</p>

<ul>
<li>Class <code>Base</code>:

<ul>
<li>private class attribute <code>__nb_objects = 0</code></li>
<li>class constructor: <code>def __init__(self, id=None):</code>:

<ul>
<li>if <code>id</code> is not <code>None</code>, assign the public instance attribute <code>id</code> to this argument value</li>
<li>otherwise, increment <code>__nb_objects</code> and assign the new value to the public instance attribute <code>id</code></li>
</ul></li>
</ul></li>
</ul>
  <h4 class="task">
    2. First Rectangle
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write the class <code>Rectangle</code> that inherits from <code>Base</code>:</p>

<ul>
<li>In the file <code>models/rectangle.py</code></li>
<li>Class <code>Rectangle</code> inherits from <code>Base</code></li>
<li>Private instance attributes, each with it&#39;s own public getter and setter:

<ul>
<li><code>__width</code> -&gt; <code>width</code></li>
<li><code>__height</code> -&gt; <code>height</code></li>
<li><code>__x</code> -&gt; <code>x</code></li>
<li><code>__y</code> -&gt; <code>y</code></li>
</ul></li>
<li>Class constructor: <code>def __init__(self, width, height, x=0, y=0, id=None)</code>:

<ul>
<li>Call the super class with <code>id</code> - this super call with use the logic of the <code>__init__</code> of the <code>Base</code> class</li>
<li>Assign each argument <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code> to the right attribute</li>
</ul></li>
</ul>
  <h4 class="task">
    3. Validate attributes
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (<code>id</code> excluded):</p>

<ul>
<li>If the input is not an integer, raise the <code>TypeError</code> exception with the message: <code>&lt;name of the attribute&gt; must be an integer</code>. Example: <code>width must be an integer</code></li>
<li>If <code>width</code> or <code>height</code> is under or equals 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt; 0</code>. Example: <code>width must be &gt; 0</code></li>
<li>If <code>x</code> or <code>y</code> is under 0, raise the <code>ValueError</code> exception with the message: <code>&lt;name of the attribute&gt; must be &gt;= 0</code>. Example: <code>x must be &gt;= 0</code></li>
</ul>
  <h4 class="task">
    4. Area first
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def area(self):</code> that returns the area value of the <code>Rectangle</code> instance.</p>
  <h4 class="task">
    5. Display #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def display(self):</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don&#39;t need to handle <code>x</code> and <code>y</code> here.</p>
  <h4 class="task">
    6. __str__
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by overloading the <code>__str__</code> method that returns <code>[Rectangle] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;width&gt;/&lt;height&gt;</code></p>
  <h4 class="task">
    7. Display #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by improving the public method <code>def display(self):</code> to print in stdout the <code>Rectangle</code> instance with the character <code>#</code> by taking care of <code>x</code> and <code>y</code></p>
  <h4 class="task">
    8. Update #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def update(self, *args):</code> that assigns an argument to each attribute:</p>

<ul>
<li>1st argument should be the <code>id</code> attribute</li>
<li>2nd argument should be the <code>width</code> attribute</li>
<li>3rd argument should be the <code>height</code> attribute</li>
<li>4th argument should be the <code>x</code> attribute</li>
<li>5th argument should be the <code>y</code> attribute</li>
</ul>

<p>This type of argument is called a &quot;no-keyword argument&quot; - Argument order is super important.</p>
  <h4 class="task">
    9. Update #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by updating the public method <code>def update(self, *args):</code> by changing the prototype to <code>update(self, *args, **kwargs)</code> that assigns a key/value argument to attributes:</p>

<ul>
<li><code>**kwargs</code> is a double pointer to a dictionary: key/value</li>
<li><code>**kwargs</code> must be skipped if <code>*args</code> exists and is not empty</li>
<li>Each key in this dictionary represents an attribute to the instance</li>
</ul>

<p>This type of argument is called a &quot;key-worded argument&quot;. Argument order is not important.</p>
  <h4 class="task">
    10. And now, the Square!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write the class <code>Square</code> that inherits from <code>Rectangle</code>:</p>

<ul>
<li>In the file <code>models/square.py</code></li>
<li>Class <code>Square</code> inherits from <code>Rectangle</code></li>
<li>Class constructor: <code>def __init__(self, size, x=0, y=0, id=None):</code>:

<ul>
<li>Call the super class with <code>id</code>, <code>x</code>, <code>y</code>, <code>width</code> and <code>height</code> - this super call will use the logic of the <code>__init__</code> of the <code>Rectangle</code> class. The <code>width</code> and <code>height</code> must be assigned to the value of <code>size</code></li>
<li>You must not create new attributes for this class, use all attributes of <code>Rectangle</code> - As reminder: a Square is a Rectangle with the same width and height</li>
<li>All <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code> validation must inherit from <code>Rectangle</code> - same behavior in case of wrong data</li>
</ul></li>
<li>The overloading <code>__str__</code> method should return <code>[Square] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;size&gt;</code> - in our case, <code>width</code> or <code>height</code></li>
</ul>
  <h4 class="task">
    11. Square size
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Square</code> by adding the public getter and setter <code>size</code></p>

<ul>
<li>The setter should assign (in this order) the <code>width</code> and the <code>height</code> - with the same value</li>
<li>The setter should have the same value validation as the <code>Rectangle</code> for <code>width</code> and <code>height</code> - No need to change the exception error message (It should be the one from <code>width</code>)</li>
</ul>
  <h4 class="task">
    12. Square update
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Square</code> by adding the public method <code>def update(self, *args, **kwargs)</code> that assigns attributes:</p>

<ul>
<li><code>*args</code> is the list of arguments - no-keyworded arguments

<ul>
<li>1st argument should be the <code>id</code> attribute</li>
<li>2nd argument should be the <code>size</code> attribute</li>
<li>3rd argument should be the <code>x</code> attribute</li>
<li>4th argument should be the <code>y</code> attribute</li>
</ul></li>
<li><code>**kwargs</code> is a double pointer to a dictionary: key/value (keyworded arguments)</li>
<li><code>**kwargs</code> must be skipped if *args exists and is not empty</li>
<li>Each key in this dictionary represents an attribute to the instance</li>
</ul>
  <h4 class="task">
    13. Rectangle instance to dictionary representation
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Rectangle</code> by adding the public method <code>def to_dictionary(self):</code> that returns the dictionary representation of a <code>Rectangle</code>:</p>

<p>This dictionary must contain:</p>

<ul>
<li><code>id</code></li>
<li><code>width</code></li>
<li><code>height</code></li>
<li><code>x</code></li>
<li><code>y</code></li>
</ul>
  <h4 class="task">
    14. Square instance to dictionary representation
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Square</code> by adding the public method <code>def to_dictionary(self):</code> that returns the dictionary representation of a <code>Square</code>:</p>

<p>This dictionary must contain:</p>

<ul>
<li><code>id</code></li>
<li><code>size</code></li>
<li><code>x</code></li>
<li><code>y</code></li>
</ul>
  <h4 class="task">
    15. Dictionary to JSON string
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>JSON is one of the standard formats for sharing data representation.</p>

<p>Update the class <code>Base</code> by adding the static method <code>def to_json_string(list_dictionaries):</code> that returns the JSON string representation of <code>list_dictionaries</code>:</p>

<ul>
<li><code>list_dictionaries</code> is a list of dictionaries</li>
<li>If <code>list_dictionaries</code> is <code>None</code> or empty, return the string: <code>&quot;[]&quot;</code></li>
<li>Otherwise, return the JSON string representation of <code>list_dictionaries</code></li>
</ul>
  <h4 class="task">
    16. JSON string to file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Base</code> by adding the class method <code>def save_to_file(cls, list_objs):</code> that writes the JSON string representation of <code>list_objs</code> to a file:</p>

<ul>
<li><code>list_objs</code> is a list of instances who inherits of <code>Base</code> - example: list of <code>Rectangle</code> or list of <code>Square</code> instances</li>
<li>If <code>list_objs</code> is <code>None</code>, save an empty list</li>
<li>The filename must be: <code>&lt;Class name&gt;.json</code> - example: <code>Rectangle.json</code></li>
<li>You must use the static method <code>to_json_string</code> (created before)</li>
<li>You must overwrite the file if it already exists</li>
</ul>
  <h4 class="task">
    17. JSON string to dictionary
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Base</code> by adding the static method <code>def from_json_string(json_string):</code> that returns the list of the JSON string representation <code>json_string</code>:</p>

<ul>
<li><code>json_string</code> is a string representing a list of dictionaries</li>
<li>If <code>json_string</code> is <code>None</code> or empty, return an empty list</li>
<li>Otherwise, return the list represented by <code>json_string</code></li>
</ul>
  <h4 class="task">
    18. Dictionary to Instance
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Base</code> by adding the class method <code>def create(cls, **dictionary):</code> that returns an instance with all attributes already set:</p>

<ul>
<li><code>**dictionary</code> is a double pointer to a dictionary</li>
<li>To use the <code>update</code> method to assign all attributes, you must create a &quot;dummy&quot; instance before: 

<ul>
<li>Create a <code>Rectangle</code> or <code>Square</code> instance with &quot;dummy&quot; mandatory attributes (width, height, size, etc.)</li>
<li>Call <code>update</code> instance method to this &quot;dummy&quot; instance to apply your real values</li>
</ul></li>
<li>You must use the method <code>def update(self, *args, **kwargs)</code></li>
<li><code>**dictionary</code> must be used as <code>**kwargs</code> of the method <code>update</code></li>
<li>You are not allowed to use <code>eval</code></li>
</ul>
  <h4 class="task">
    19. File to instances
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Update the class <code>Base</code> by adding the class method <code>def load_from_file(cls):</code> that returns a list of instances:</p>

<ul>
<li>The filename must be: <code>&lt;Class name&gt;.json</code> - example: <code>Rectangle.json</code></li>
<li>If the file doesn&#39;t exist, return an empty list</li>
<li>Otherwise, return a list of instances - the type of these instances depends on <code>cls</code> (current class using this method)</li>
<li>You must use the <code>from_json_string</code> and <code>create</code> methods (implemented previously) </li>
</ul>
