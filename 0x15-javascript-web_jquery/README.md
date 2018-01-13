<h1 class="gap">0x15. Javascript - Web JQuery</h1>


<h4 class="task">
    0. No jQuery
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):</p><ul>
<li>You must use <code>document.querySelector</code> to select the HTML tag</li>
<li>You can’t use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    1. With jQuery
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):</p><ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    2. Click and turn red
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:</p><ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    3. Add `.red` class
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that adds the class <code>red</code> to the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:</p><ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    4. Toggle classes
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that toggles the class of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#toggle_header</code>:</p><ul>
<li>The <code>HEADER</code> tag must always have one class: <code>red</code> or <code>green</code>, never both in the same time, never empty.</li>
<li>If the current class is <code>red</code>, when the user click on <code>DIV#toggle_header</code>, the class must be updated to <code>green</code> ; and the reverse.</li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    5. List of elements
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that adds a <code>LI</code> element to a list when the user clicks on the tag <code>DIV#add_item</code>:</p><ul>
<li>The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code></li>
<li>The new element must be added to <code>UL.my_list</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    6. Change the text
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that updates the text of the HTML tag <code>HEADER</code> to “New Header!!!” when the user clicks on <code>DIV#update_header</code></p><ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    7. Star wars character
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that fetches and replaces the <code>name</code> of this URL: <code>https://swapi.co/api/people/5/?format=json</code></p><ul>
<li>The name must be displayed in the HTML tag <code>DIV#character</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    8. Star Wars movies
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that fetches and lists all movies <code>title</code> by using this URL: <code>https://swapi.co/api/films/?format=json</code></p><ul>
<li>All movie titles must be list in the HTML tag <code>UL#list_movies</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    9. Wind speed
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Javascript script that fetches and prints the San Francisco wind speed by using this URL: <code>https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&amp;format=json</code></p><ul>
<li>The wind speed must be display in the HTML tag <code>DIV#sf_wind_speed</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API
You script must be work when it imported from the <code>HEAD</code> tag</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    10. No jQuery - document loaded
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):</p><ul>
<li>You must use <code>document.querySelector</code> to select the HTML tag</li>
<li>You can’t use the jQuery API</li>
<li>You script must be work when it imported from the <code>HEAD</code> tag</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    11. List, add, remove
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a Javascript script that adds, removes and clears <code>LI</code> elements from a list when the user clicks:</p><ul>
<li>The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code></li>
<li>The new element must be added to <code>UL.my_list</code></li>
<li>When the user clicks on <code>DIV#add_item</code>: a new element is added to the list</li>
<li>When the user clicks on <code>DIV#remove_item</code>: a last element is removed to the list</li>
<li>When the user clicks on <code>DIV#clear_list</code>: all elements of the list are removed</li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
<li>You script must be work when it imported from the <code>HEAD</code> tag</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    12. Search wind speed
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a Javascript script that fetches and prints the wind speed by using this URL: <code>https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&amp;format=json</code></p><ul>
<li>The wind speed must be display in the HTML tag <code>DIV#wind_speed</code></li>
<li>The city name must be the value of the tag <code>INPUT#city_search</code></li>
<li>The wind speed must be fetch when the user clicks on <code>INPUT#btn_search</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
<li>You script must be work when it imported from the <code>HEAD</code> tag</li>
</ul><p>Please test with this HTML file in your browser:</p>


<h4 class="task">
    13. And press ENTER
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a Javascript script that fetches and prints the wind speed by using this URL: <code>https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&amp;format=json</code></p><ul>
<li>The wind speed must be display in the HTML tag <code>DIV#wind_speed</code></li>
<li>The city name must be the value of the tag <code>INPUT#city_search</code></li>
<li>The wind speed must be fetch when the user clicks on <code>INPUT#btn_search</code> OR press <code>ENTER</code> when the focus is on <code>INPUT#city_search</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
<li>You script must be work when it imported from the <code>HEAD</code> tag</li>
</ul><p>Please test with this HTML file in your browser:</p>

