<h1 class="gap">0x0B. Python - Input/Output</h1>
  <h4 class="task">
    0. Read file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that reads a text file (<code>UTF8</code>) and prints it to stdout:</p>

<ul>
<li>Prototype: <code>def read_file(filename=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage file permission/file doesn&#39;t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    1. Number of lines
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns the number of lines of a text file:</p>

<ul>
<li>Prototype: <code>def number_of_lines(filename=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage file permission/file doesn&#39;t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    2. Read n lines
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that reads <code>n</code> lines of a text file (<code>UTF8</code>) and prints it to stdout:</p>

<ul>
<li>Prototype: <code>def read_lines(filename=&quot;&quot;, nb_lines=0):</code></li>
<li>Read the entire file if <code>nb_lines</code> is lower or equal to <code>0</code> OR greater or equal to the total number of lines of the file</li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage file permission/file doesn&#39;t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    3. Write to a file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that writes a string to a text file (<code>UTF8</code>) and returns the number of characters written:</p>

<ul>
<li>Prototype: <code>def write_file(filename=&quot;&quot;, text=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage file permission exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    4. Append to a file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that appends a string at the end of a text file (<code>UTF8</code>) and returns the number of characters added:</p>

<ul>
<li>Prototype: <code>def append_write(filename=&quot;&quot;, text=&quot;&quot;):</code></li>
<li>If the file doesn&#39;t exist, it should be created</li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage file permission/file doesn&#39;t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    5. To JSON string
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns the JSON representation of an object (string):</p>

<ul>
<li>Prototype: <code>def to_json_string(my_obj):</code></li>
<li>You don&#39;t need to manage exceptions if the object can&#39;t be serialized.</li>
</ul>
  <h4 class="task">
    6. From JSON string to Object
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns an object (Python data structure) represented by a JSON string:</p>

<ul>
<li>Prototype: <code>def from_json_string(my_str):</code></li>
<li>You don&#39;t need to manage exceptions if the JSON string doesn&#39;t represent an object.</li>
</ul>
  <h4 class="task">
    7. Save Object to a file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that writes an Object to a text file, using a JSON representation:</p>

<ul>
<li>Prototype: <code>def save_to_json_file(my_obj, filename):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage exceptions if the object can&#39;t be serialized.</li>
<li>You don&#39;t need to manage file permission exceptions.</li>
</ul>
  <h4 class="task">
    8. Create object from a JSON file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that creates an Object from a &quot;JSON file&quot;:</p>

<ul>
<li>Prototype: <code>def load_from_json_file(filename):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage exceptions if the JSON string doesn&#39;t represent an object.</li>
<li>You don&#39;t need to manage file permissions / exceptions.</li>
</ul>
  <h4 class="task">
    9. Load, add, save
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a script that adds all arguments to a Python list, and then save them to a file:</p>

<ul>
<li>You must use your function <code>save_to_json_file</code> from <code>7-save_to_json_file.py</code></li>
<li>You must use your function <code>load_from_json_file</code> from <code>8-load_from_json_file.py</code></li>
<li>The list must be saved as a JSON representation in a file named <code>add_item.json</code></li>
<li>If the file doesn&#39;t exist, it should be created</li>
<li>You don&#39;t need to manage file permissions / exceptions.</li>
</ul>
  <h4 class="task">
    10. Class to JSON
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:</p>

<ul>
<li>Prototype: <code>def class_to_json(obj):</code></li>
<li><code>obj</code> is an instance of a Class</li>
<li>All attributes of the <code>obj</code> Class are serializable: list, dictionary, string, integer and boolean</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    11. Student to JSON
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Student</code> that defines a student by:</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>10-class_to_json.py</code>)</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    12. Student to JSON with filter
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Student</code> that defines a student by: (based on <code>11-student.py</code>)</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>10-class_to_json.py</code>):

<ul>
<li>If <code>attrs</code> is a list of strings, only attributes name contain in this list must be retrieved. </li>
<li>Otherwise, all attributes must be retrieved</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    13. Student to disk and reload
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a class <code>Student</code> that defines a student by: (based on <code>12-student.py</code>)</p>

<ul>
<li>Public instance attributes: 

<ul>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
<li><code>age</code></li>
</ul></li>
<li>Instantiation with <code>first_name</code>, <code>last_name</code> and <code>age</code>: <code>def __init__(self, first_name, last_name, age):</code></li>
<li>Public method <code>def to_json(self, attrs=None):</code> that retrieves a dictionary representation of a <code>Student</code> instance (same as <code>10-class_to_json.py</code>):

<ul>
<li>If <code>attrs</code> is a list of strings, only attributes name contain in this list must be retrieved. </li>
<li>Otherwise, all attributes must be retrieved</li>
</ul></li>
<li>Public method <code>def reload_from_json(self, json):</code> that replaces all attributes of the <code>Student</code> instance:

<ul>
<li>You can assume <code>json</code> will always be a dictionary</li>
<li>A dictionary key will be the public attribute name</li>
<li>A dictionary value will be the value of the public attribute</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<p>Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)</p>
  <h4 class="task">
    14. Search and update
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that inserts a line of text to a file, after each line containing a specific string (see example):</p>

<ul>
<li>Prototype: <code>def append_after(filename=&quot;&quot;, search_string=&quot;&quot;, new_string=&quot;&quot;):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don&#39;t need to manage file permission/file doesn&#39;t exist exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    15. Log parsing
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a script that reads <code>stdin</code> line by line and computes metrics:</p>

<ul>
<li>Input format: <code>&lt;IP Address&gt; - [&lt;date&gt;] &quot;GET /projects/260 HTTP/1.1&quot; &lt;status code&gt; &lt;file size&gt;</code></li>
<li>Each 10 lines and after a keyboard interruption (<code>CTRL + C</code>), prints those statistics since the beginning:

<ul>
<li>Total file size: <code>File size: &lt;total size&gt;</code></li>
<li>where <total size> is the sum of all previous <file size> (see input format above)</li>
<li>Number of lines by status code: 

<ul>
<li>possible status code: <code>200</code>, <code>301</code>, <code>400</code>, <code>401</code>, <code>403</code>, <code>404</code>, <code>405</code> and <code>500</code></li>
<li>if a status code doesn&#39;t appear, don&#39;t print anything for this status code</li>
<li>format: <code>&lt;status code&gt;: &lt;number&gt;</code></li>
<li>status codes should be printed in ascending order</li>
</ul></li>
</ul></li>
</ul>
  <h4 class="task">
    16. Hack the VM
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a script that finds a string in the heap of a running process, and replaces it.</p>

<ul>
<li>Read <a href="https://www.kernel.org/doc/Documentation/filesystems/proc.txt">The /proc filesystem</a></li>
<li>Usage: <code>read_write_heap.py pid search_string replace_string</code>

<ul>
<li>where <code>pid</code> is the pid of the running process</li>
<li>and strings are ASCII</li>
</ul></li>
<li>The script should look only in the heap of the process</li>
<li>Output: you can print whatever you think is interesting</li>
<li>On usage error, print an error message on <code>stdout</code> and exit with status code <code>1</code></li>
</ul>
