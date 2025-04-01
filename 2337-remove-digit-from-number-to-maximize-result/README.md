<h2><a href="https://leetcode.com/problems/remove-digit-from-number-to-maximize-result">Remove Digit From Number to Maximize Result</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><p>You are given a string <code>number</code> representing a <strong>positive integer</strong> and a character <code>digit</code>.</p>

<p>Return <em>the resulting string after removing <strong>exactly one occurrence</strong> of </em><code>digit</code><em> from </em><code>number</code><em> such that the value of the resulting string in <strong>decimal</strong> form is <strong>maximized</strong></em>. The test cases are generated such that <code>digit</code> occurs at least once in <code>number</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> number = &quot;123&quot;, digit = &quot;3&quot;
<strong>Output:</strong> &quot;12&quot;
<strong>Explanation:</strong> There is only one &#39;3&#39; in &quot;123&quot;. After removing &#39;3&#39;, the result is &quot;12&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> number = &quot;1231&quot;, digit = &quot;1&quot;
<strong>Output:</strong> &quot;231&quot;
<strong>Explanation:</strong> We can remove the first &#39;1&#39; to get &quot;231&quot; or remove the second &#39;1&#39; to get &quot;123&quot;.
Since 231 &gt; 123, we return &quot;231&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> number = &quot;551&quot;, digit = &quot;5&quot;
<strong>Output:</strong> &quot;51&quot;
<strong>Explanation:</strong> We can remove either the first or second &#39;5&#39; from &quot;551&quot;.
Both result in the string &quot;51&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= number.length &lt;= 100</code></li>
	<li><code>number</code> consists of digits from <code>&#39;1&#39;</code> to <code>&#39;9&#39;</code>.</li>
	<li><code>digit</code> is a digit from <code>&#39;1&#39;</code> to <code>&#39;9&#39;</code>.</li>
	<li><code>digit</code> occurs at least once in <code>number</code>.</li>
</ul>


<h1>Explanation of the Line</h1>
<pre>
result = max(result, int(number[0:i] + number[i+1:len(number)]))
</pre>
<p>This line performs the following operations:</p>
<ul>
  <li><code>number[0:i]</code> - Extracts the substring from the start (index <code>0</code>) to index <code>i</code> (excluding <code>i</code>).</li>
  <li><code>number[i+1:len(number)]</code> - Extracts the substring from index <code>i+1</code> to the end, effectively removing <code>number[i]</code>.</li>
  <li><code>number[0:i] + number[i+1:len(number)]</code> - Concatenates the two substrings, effectively removing the character at index <code>i</code>.</li>
  <li><code>int(...)</code> - Converts the resulting string into an integer.</li>
  <li><code>max(result, ...)</code> - Keeps track of the maximum number obtained after removing an occurrence of <code>digit</code>.</li>
</ul>

<h3>Example</h3>
<p>For <code>number = "1231"</code> and <code>digit = "1"</code>:</p>
<ul>
  <li>Removing the first <code>"1"</code>: <code>number[0:0] + number[1:4]</code> → <code>"" + "231"</code> → <code>"231"</code></li>
  <li>Removing the last <code>"1"</code>: <code>number[0:3] + number[4:4]</code> → <code>"123" + ""</code> → <code>"123"</code></li>
</ul>
<p>The function returns <code>"231"</code>, as <code>231 &gt; 123</code>.</p>
