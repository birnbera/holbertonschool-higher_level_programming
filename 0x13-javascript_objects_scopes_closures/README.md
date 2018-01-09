<h1 class="gap">0x13. Javascript - Objects, Scopes and Closures</h1>


<h4 class="task">
    0. Rectangle #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p><ul>
<li>You must use the <code>class</code> notation for defining your class </li>
</ul>


<h4 class="task">
    1. Rectangle #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>Rectangle</code> that defines a rectangle:</p><ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
</ul>


<h4 class="task">
    2. Rectangle #2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>Rectangle</code> that defines a rectangle:</p><ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
</ul>


<h4 class="task">
    3. Rectangle #3
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>Rectangle</code> that defines a rectangle:</p><ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
</ul>


<h4 class="task">
    4. Rectangle #4
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>Rectangle</code> that defines a rectangle:</p><ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
<li>Create an instance method called <code>rotate()</code> that exchanges the <code>width</code> and the <code>height</code> of the rectangle</li>
<li>Create an instance method called <code>double()</code> that multiples the <code>width</code> and the <code>height</code> of the rectangle by 2</li>
</ul>


<h4 class="task">
    5. Square #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>Square</code> that defines a square and inherits from <code>Rectangle</code> of <code>4-rectangle.js</code>:</p><ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>The constructor must take 1 argument: <code>size</code></li>
<li>The constructor of <code>Rectangle</code> must be called (by using <code>super()</code>)</li>
</ul>


<h4 class="task">
    6. Square #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a class <code>Square</code> that defines a square and inherits from <code>Square</code> of <code>5-square.js</code>:</p><ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>Create an instance method called <code>charPrint(c)</code> that prints the rectangle using the character <code>c</code>
<ul>
<li>If <code>c</code> is <code>undefined</code>, use the character <code>X</code></li>
</ul></li>
</ul>


<h4 class="task">
    7. Occurrences
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that returns the number of occurrences in a list:</p><ul>
<li>Prototype: <code>exports.nbOccurences = function (list, searchElement)</code></li>
</ul>


<h4 class="task">
    8. Esrever
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that returns the reversed version of a list:</p><ul>
<li>Prototype: <code>exports.esrever = function (list)</code></li>
<li>You are not allow to use the build-in method <code>reverse</code></li>
</ul>


<h4 class="task">
    9. Log me
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that prints the number of argument already printed and the new argument value. (see example below)</p><ul>
<li>Prototype: <code>exports.logMe = function (item)</code></li>
<li>Output format: <code>&lt;number arguments already printed&gt;: &lt;current argument value&gt;</code></li>
</ul>


<h4 class="task">
    10. Number conversion
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a function that converts a number from base 10 to another base passed as argument:</p><ul>
<li>Prototype: <code>exports.converter = function (base)</code></li>
<li>You are not allowed to import any file</li>
<li>You are not allowed to declare any new variable (<code>var</code>, <code>let</code>, etc..)</li>
</ul>


<h4 class="task">
    11. Factor index
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that imports an array and computes a new array.</p><ul>
<li>Your script must import <code>list</code> from the file <code>100-data.js</code></li>
<li>You must use a <code>map</code>. <a href="/rltoken/aWmgrzMUMiiuFI_ivcgfKw" target="_blank" title="Tips">Tips</a></li>
<li>A new list must be created with each value equal to the value of the initial list, multipled by the index in the list</li>
<li>Print both the initial list and the new list</li>
</ul>


<h4 class="task">
    12. Sorted occurences
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.</p><ul>
<li>Your script must import <code>dict</code> from the file <code>101-data.js</code></li>
<li>In the new dictionary:

<ul>
<li>A key is a number of occurrences</li>
<li>A value is the list of user ids</li>
</ul></li>
<li>Print the new dictionary at the end</li>
</ul>


<h4 class="task">
    13. Concat files
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that concats 2 files.</p><ul>
<li>The first argument is the file path of the first source file</li>
<li>The second argument is the file path of the second source file</li>
<li>The third argument is the file path of the destination</li>
</ul>

