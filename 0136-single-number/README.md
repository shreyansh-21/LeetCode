<h2><a href="https://leetcode.com/problems/single-number">136. Single Number</a></h2><h3>Easy</h3><hr><p>Given a <strong>non-empty</strong>&nbsp;array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
	<li>Each element in the array appears twice except for one element which appears only once.</li>
</ul>
<h3>First Solution (Your first code):</h3>
<pre><code>
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Initialize odd with the number of even numbers between low and high.
        odd = (high - low) // 2
        
# If either low or high is odd, increment odd by 1.
if low % 2 == 1 or high % 2 == 1:
            odd += 1
        
 # Return the number of odd numbers between low and high.
 return odd
</code></pre>

<h4>Explanation:</h4>

<ol>
    <li><strong>Line 5</strong>: <code>odd = (high - low) // 2</code>
        <ul>
            <li>Pehle <code>high - low</code> ka difference find kiya jaata hai, jo range ka size bataata hai. Phir, is difference ko 2 se divide karke yeh count kiya jaata hai ki kitni pairs of odd-even numbers hain.</li>
            <li>Example: Agar <code>low = 3</code> aur <code>high = 7</code>, toh <code>high - low = 4</code> aur <code>(high - low) // 2 = 2</code>. Matlab 4 ke beech 2 numbers hain jo even-odd pair banate hain (<code>3, 4</code>) aur (<code>5, 6</code>).</li>
        </ul>
    </li>

 <li><strong>Line 7</strong>: <code>if low % 2 == 1 or high % 2 == 1:</code>
        <ul>
            <li>Agar <code>low</code> ya <code>high</code> odd hai, toh is condition ko satisfy karte hain. Agar kisi bhi extreme number mein odd number hai, toh total odd numbers ko 1 increment karna padta hai, kyunki ek aur odd number add ho jata hai.</li>
            <li>Example: Agar range <code>low = 3</code> aur <code>high = 7</code> ho, toh total odd numbers <code>3, 5, aur 7</code> hain, jo 3 numbers hain.</li>
        </ul>
    </li>
