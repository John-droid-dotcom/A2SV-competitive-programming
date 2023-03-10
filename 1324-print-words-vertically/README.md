<h2><a href="https://leetcode.com/problems/print-words-vertically/">1324. Print Words Vertically</a></h2><h3>Medium</h3><hr><div><p>Given a string <code data-copier-init="true">s</code>.&nbsp;Return&nbsp;all the words vertically in the same order in which they appear in <code data-copier-init="true">s</code>.<br>
Words are returned as a list of strings, complete with&nbsp;spaces when is necessary. (Trailing spaces are not allowed).<br>
Each word would be put on only one column and that in one column there will be only one word.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "HOW ARE YOU"
<strong>Output:</strong> ["HAY","ORO","WEU"]
<strong>Explanation: </strong>Each word is printed vertically. 
 "HAY"
&nbsp;"ORO"
&nbsp;"WEU"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "TO BE OR NOT TO BE"
<strong>Output:</strong> ["TBONTB","OEROOE","   T"]
<strong>Explanation: </strong>Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "CONTEST IS COMING"
<strong>Output:</strong> ["CIC","OSO","N M","T I","E N","S G","T"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= s.length &lt;= 200</code></li>
	<li><code data-copier-init="true">s</code>&nbsp;contains only upper case English letters.</li>
	<li>It's guaranteed that there is only one&nbsp;space between 2 words.</li>
</ul></div>