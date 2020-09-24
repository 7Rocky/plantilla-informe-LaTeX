import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Comment, Keyword, String, Text

__all__ = ['YamlLexer']

class YamlLexer(RegexLexer):

    name = 'YAML'
    aliases = ['yaml']
    filenames = ['*.yaml']

    # Text: black
    # String.Simple: brown
    # Keyword: blue
    # Comment.Single: green

    tokens = {
        'root': [
            (r'---', Text),
            # - foo: 1
            (r'^(\s*?-\s)(.*?)(:\s)(\d+?)$', bygroups(Text, String.Simple, Text, Comment.Single)),
            # - key: value1234
            (r'^(\s*?-\s)(.*?)(:\s)([\w\d]+?)$', bygroups(Text, String.Simple, Text, Keyword)),
            # - ip: 192.168.1.10
            (r"^(\s*?-\s)(.*?)(:\s)([\w\-/\.]+?)$", bygroups(Text, String.Simple, Text, Keyword)),
            # - items:
            (r'^(\s*?-\s)(.*?)(:)$', bygroups(Text, String.Simple, Text)),
            # - item
            (r'^(\s*?-\s)(.*?)$', bygroups(Text, Keyword)),
            # length: 10
            (r'^(\s*?)(.*?)(:\s)(\d+?)$', bygroups(Text, String.Simple, Text, Comment.Single)),
            # foo: '125cc'
            (r"^(\s*?)(.*?)(:\s)('[\w\d:=\$\d\.\(\)\*]+?')$", bygroups(Text, String.Simple, Text, Keyword)),
            # foo: bar
            (r"^(\s*?)(.*?)(:\s)([\w\-/:=\$\d\.\(\)\*]+?)$", bygroups(Text, String.Simple, Text, Keyword)),
            # foo: 'bar'
            (r"^(\s*?)(.*?)(:\s)('[\w\-/:=\$\d\.\(\)\*]+?')$", bygroups(Text, String.Simple, Text, Keyword)),
            # attributes:
            (r'^(\s*?)(.*?)(:)$', bygroups(Text, String.Simple, Text))
        ]
    }
