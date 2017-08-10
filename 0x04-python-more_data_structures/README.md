## 0x04. Python - More Data Structures: Set, Dictionary
  <h4 class="task">
    0. Squared simple
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that computes the square value of all integers of a matrix.</p>

<ul>
<li>Prototype: <code>def square_matrix_simple(matrix=[]):</code></li>
<li><code>matrix</code> is a 2 dimensional array</li>
<li>Returns a new matrix:

<ul>
<li>Same size as <code>matrix</code></li>
<li>Each value should be the square of the value of the input</li>
</ul></li>
<li>Initial matrix should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You are allow to use regular loops, <code>map</code>, etc.</li>
</ul>
  <h4 class="task">
    1. Search and replace
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that replaces all occurrences of an element by another in a new list.</p>

<ul>
<li>Prototype: <code>def search_replace(my_list, search, replace):</code></li>
<li><code>list</code> is the initial list</li>
<li><code>search</code> is the element to replace in the list</li>
<li><code>replace</code> is the new element</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    2. Unique addition
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that makes the addition of all unique integers in a list (only one time each integer).</p>

<ul>
<li>Prototype: <code>def uniq_add(my_list=[]):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    3. Present in both
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns a set of common elements in two sets.</p>

<ul>
<li>Prototype: <code>def common_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    4. Only differents
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns a set of all elements present in only one set.</p>

<ul>
<li>Prototype: <code>def only_diff_elements(set_1, set_2):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    5. Number of keys
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns the number of keys in a dictionary.</p>

<ul>
<li>Prototype: <code>def number_keys(my_dict):</code></li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    6. Print sorted dictionary
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that prints a dictionary by ordered keys.</p>

<ul>
<li>Prototype: <code>def print_sorted_dictionary(my_dict):</code></li>
<li>You can assume that all keys are string</li>
<li>Keys should be sorted by alphabetic order</li>
<li>Only sort keys of the first level (don&#39;t sort keys of a dictionary inside the main dictionary)</li>
<li>Dictionary values can have any type</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    7. Update dictionary
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that replace or add key/value in a dictionary.</p>

<ul>
<li>Prototype: <code>def update_dictionary(my_dict, key, value):</code></li>
<li><code>key</code> argument will be always a string</li>
<li><code>value</code> argument will be any type</li>
<li>If a key exists in the dictionary, the value will be replaced</li>
<li>If a key doesn&#39;t exist in the dictionary, it will be created</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    8. Simple delete by key
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that deletes a key in a dictionary.</p>

<ul>
<li>Prototype: <code>def simple_delete(my_dict, key=&quot;&quot;):</code></li>
<li><code>key</code> argument will be always a string</li>
<li>If a key doesn&#39;t exist, the dictionary won&#39;t change</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    9. Multiply by 2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns a new dictionary with all values multiplied by 2</p>

<ul>
<li>Prototype: <code>def multiply_by_2(my_dict):</code></li>
<li>You can assume that all values are only integers</li>
<li>Returns a new dictionary</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    10. Best score
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns a key with the biggest integer value.</p>

<ul>
<li>Prototype: <code>def best_score(my_dict):</code></li>
<li>You can assume that all values are only integers</li>
<li>If no score found, return <code>None</code></li>
<li>You can assume all students have a different score</li>
<li>You are not allowed to import any module</li>
</ul>
  <h4 class="task">
    11. Multiply by using map
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Write a function that returns a list with all values multiplied by a number without using any loops.</p>

<ul>
<li>Prototype: <code>def mutiply_list_map(my_list=[], number=0):</code></li>
<li>Returns a new list:

<ul>
<li>Same length as <code>my_list</code></li>
<li>Each value should be multiplied by <code>number</code></li>
</ul></li>
<li>Initial list should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>Your file should be max 3 lines</li>
</ul>
