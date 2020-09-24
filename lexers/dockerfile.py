import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Comment, Generic, Keyword, String, Text

__all__ = ['DockerfileLexer']

class DockerfileLexer(RegexLexer):

    name = 'Dockerfile'
    aliases = ['']
    filenames = ['*']

    # Text: black
    # String.Simple: brown
    # Keyword: blue
    # Generic.Underline: underline

    tokens = {
        'root': [
            (r'^(FROM)(\s)([\w\d\-/]+?)(:.*?)$', bygroups(Keyword, Text, Generic.Underline, Text)),
            (r'(ADD|AS|CMD|COPY|ENTRYPOINT|ENV|LABEL|RUN|USER|VOLUME|WORKDIR)', Keyword),
            (r'".*?"', String.Simple),
            (r'.', Text)
        ]
    }
