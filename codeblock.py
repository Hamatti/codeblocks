import sys

try:
    language = sys.argv[1]
except IndexError:
    print('Usage: codeblock.py [language] < [input file]')
    sys.exit(1)

ENTITIES = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;'
}

codeblock = f'<pre class="language-{language}"><code class="language-{language}">'

for line in sys.stdin:
    if line.strip() == '':
        # This includes a zero-width space (U+200B) before the line break
        # because my blog's code blocks break if there are empty lines.
        line = '​\n'
    for character, encoded in ENTITIES.items():
        line = line.replace(character, encoded)
    codeblock = f'{codeblock}{line}'

codeblock = f'{codeblock}</code></pre>'

print(codeblock)
