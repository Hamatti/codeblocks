# &lt;code&gt;blocks


This repository contains a helper script that I use to convert a input code into a HTML `<pre><code>` block with class names matching my blog's needs and converts special characters to HTML entities.

I use Ghost as a headless CMS for my blog and manually creating code snippets is a pain so I wrote this thing to assist me.

## Usage

```
python codeblock.py [language] < [code_input]
```

The script reads the code snippet from standard input and outputs the converted one into standard output. `[language]` is used to create class names `class="language-[language]"` to `pre` and `code` elements. I use them to trigger Prism.js.

## Example

`example.py`

```
def greeting(name):
  return f'Hello <{name}>'
```

running `python codeblock.py python < example.py` outputs

```
<pre class="language-python"><code class="language-python">def greeting(name):
  return f'Hello &lt;{name}&rt;'</code></pre>
```
