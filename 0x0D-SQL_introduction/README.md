<h1 class="gap">0x0D. SQL - Introduction</h1>


<h4 class="task">
    0. List databases
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all databases of your MySQL server.</p>


<h4 class="task">
    1. Create a database
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>If the database <code>hbtn_0c_0</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>


<h4 class="task">
    2. Delete a database
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that deletes the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>If the database <code>hbtn_0c_0</code> doesn’t exist, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>


<h4 class="task">
    3. List tables
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all the tables of a database in your MySQL server.</p><ul>
<li>The database name will be passed as argument of <code>mysql</code> command (in the following example: <code>mysql</code> is the name of the database)</li>
</ul>


<h4 class="task">
    4. First table
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates a table called <code>first_table</code> in the current database in your MySQL server.</p><ul>
<li><code>first_table</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>first_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>


<h4 class="task">
    5. Full description
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the full description of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>You are not allowed to use the <code>DESCRIBE</code> or <code>EXPLAIN</code> statements</li>
</ul>


<h4 class="task">
    6. List all in table
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all rows of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>All fields should be printed</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    7. First add
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that inserts a new row in the table <code>first_table</code> (database <code>hbtn_0c_0</code>) in your MySQL server.</p><ul>
<li>New row:

<ul>
<li><code>id</code> = <code>89</code></li>
<li><code>name</code> = <code>Holberton School</code></li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    8. Count 89
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that displays the number of records with <code>id = 89</code> in the table <code>first_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    9. Full creation
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates a table <code>second_table</code> in the database <code>hbtn_0c_0</code> in your MySQL server and add multiples rows.</p><ul>
<li><code>second_table</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
<li><code>score</code> INT</li>
</ul></li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
<li>If the table <code>second_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> and <code>SHOW</code> statements</li>
<li>Your script should create these records:

<ul>
<li><code>id</code> = 1, <code>name</code> = “John”, <code>score</code> = 10</li>
<li><code>id</code> = 2, <code>name</code> = “Alex”, <code>score</code> = 3</li>
<li><code>id</code> = 3, <code>name</code> = “Bob”, <code>score</code> = 14</li>
<li><code>id</code> = 4, <code>name</code> = “George”, <code>score</code> = 8</li>
</ul></li>
</ul>


<h4 class="task">
    10. List by best
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first) </li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    11. Select the best
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first)</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    12. Cheating is bad
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that updates the score of Bob to <code>10</code>.</p><ul>
<li>You are not allowed to use Bob’s id value, only the <code>name</code> field</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    13. Score too low
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    14. Average
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>The result column name should be <code>average</code></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    15. Number by score
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>The result should display:

<ul>
<li>the <code>score</code></li>
<li>the number of records for this <code>score</code> with the label <code>number</code></li>
</ul></li>
<li>The list should be sorted by the number of records (descending)</li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul>


<h4 class="task">
    16. Say my name
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><ul>
<li>Don’t list rows without a <code>name</code> value</li>
<li>Results should display the score and the name (in this order)</li>
<li>Records should be listed by descending score </li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul><p>In this example, new data have been added to the table <code>second_table</code>.</p>


<h4 class="task">
    17. Go to UTF8
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that converts <code>hbtn_0c_0</code> database to UTF8 (<code>utf8mb4</code>, collate <code>utf8mb4_unicode_ci</code>) in your MySQL server.</p><p>You need to convert all of the following to <code>UTF8</code>:</p><ul>
<li>Database <code>hbtn_0c_0</code></li>
<li>Table <code>first_table</code></li>
<li>Field <code>name</code> in <code>first_table</code></li>
</ul>


<h4 class="task">
    18. Temperatures #0
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Import in <code>hbtn_0c_0</code> database this table dump: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" target="_blank" title="download">download</a></p><p>Write a script that displays the average temperature by city ordered by temperature (descending)</p>


<h4 class="task">
    19. Temperatures #1
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Import in <code>hbtn_0c_0</code> database this table dump: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" target="_blank" title="download">download</a> (same as <code>Temperatures #0</code>)</p><p>Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)</p>


<h4 class="task">
    20. Temperatures #2
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Import in <code>hbtn_0c_0</code> database this table dump: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" target="_blank" title="download">download</a> (same as <code>Temperatures #0</code>)</p><p>Write a script that displays the max temperature of each state (ordered by State name).</p>

