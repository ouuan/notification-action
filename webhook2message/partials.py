_messageFormat = 'plaintext'


def _unsupported(partialName):
    global _messageFormat
    raise Exception(
        'The partial "{}" is not supported in format "{}".'.format(partialName, _messageFormat))


def setFormat(messageFormat):
    global _messageFormat
    if messageFormat not in ['plaintext', 'markdown']:
        raise Exception(
            'The format "{}" is unsupported.'.format(messageFormat))
    _messageFormat = messageFormat


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


def repo(repo):
    repoName = repo['name']
    repoUrl = repo['html_url']
    return link(repoName, repoUrl)


def ref(ref, repo):
    repoUrl = repo['html_url']
    if ref[:11] == 'refs/heads/':
        branch = ref[11:]
        return link(branch, '{}/tree/{}'.format(repoUrl, branch))
    elif ref[:10] == 'refs/tags/':
        tag = ref[10:]
        return link(tag, '{}/releases/tag/{}'.format(repoUrl, tag))
    else:
        return ref


def commit(commit):
    shortSHA = commit['id'][:7]
    url = commit['url']
    author = commit['author']['name']
    commitMessage = commit['message']
    return '{} - {} by.{}'.format(link(shortSHA, url), commitMessage, author)
