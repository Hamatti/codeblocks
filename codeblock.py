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
    for character, encoded in ENTITIES.items():
        line = line.replace(character, encoded)
    codeblock = f'{codeblock}{line}'

codeblock = f'{codeblock}</code></pre>'

print(codeblock)
