import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Comment, Generic, Keyword, String, Text

__all__ = ['JsonLexer']

class JsonLexer(RegexLexer):

    name = 'JSON'
    aliases = ['json']
    filenames = ['*.json']

    # Text: black
    # String: brown
    # String.Json: blue
    # Comment.Simple: green

    tokens = {
        'root': [
            (r'^(\s*)(".*")(:\s)(".*")(,?)$', bygroups(Text, String.Json, Text, String, Text)),
            (r'^(\s*)(".*")(:\s)(\d+)(,?)$', bygroups(Text, String.Json, Text, Comment.Single, Text)),
            (r'^(\s*)(".*")(:\s)(true|false|null)(,?)$', bygroups(Text, String.Json, Text, Comment.Single, Text)),
            (r'^(\s*)(".*")(:\s[{\[])$', bygroups(Text, String.Json, Text)),
            (r'^(\s*)([}\]])(,?)$', bygroups(Text, Text, Text)),
            (r'^(\s*)(".*")(,?)$', bygroups(Text, String, Text)),
            (r'^(\s*)(\d+)(,?)$', bygroups(Text, String, Comment.Single)),
            (r'^(\s*)(true|false|null)(,?)$', bygroups(Text, String, Comment.Single)),
            (r'.', Text)
        ]
    }
