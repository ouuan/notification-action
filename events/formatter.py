_messageFormat = 'plaintext'


def _unsupported(partial):
    global _messageFormat
    raise Exception(
        'The partial "{}" is not supported in format "{}".'.format(partial, _messageFormat))


def setFormat(fmt):
    global _messageFormat
    if fmt not in ['plaintext', 'markdown']:
        raise Exception('The format "{}" is unsupported.'.format(fmt))
    _messageFormat = fmt


def link(title, url):
    global _messageFormat
    if (_messageFormat == 'plaintext'):
        return title
    elif (_messageFormat == 'markdown'):
        return '[{}]({})'.format(title, url)
    else:
        _unsupported('link')


def paragraph(text):
    global _messageFormat
    if (_messageFormat == 'plaintext'):
        return text + '\n\n'
    elif (_messageFormat == 'markdown'):
        return text + '\n\n'
    else:
        _unsupported('paragraph')


def br():
    global _messageFormat
    if (_messageFormat == 'plaintext'):
        return '\n'
    elif (_messageFormat == 'markdown'):
        return '  \n'
    else:
        _unsupported('br')
