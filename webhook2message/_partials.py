_messageFormat = 'plaintext'


def _unsupported(partialName):
    global _messageFormat
    raise Exception(
        f'The partial "{partialName}" is not supported in format "{_messageFormat}".')


def setFormat(messageFormat):
    global _messageFormat
    if messageFormat not in ['plaintext', 'markdown']:
        raise Exception(f'The format "{messageFormat}" is unsupported.')
    _messageFormat = messageFormat


def link(title, url):
    global _messageFormat
    if (_messageFormat == 'plaintext'):
        return title
    elif (_messageFormat == 'markdown'):
        return f'[{title}]({url})'
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
        return link(branch, f'{repoUrl}/tree/{branch}')
    elif ref[:10] == 'refs/tags/':
        tag = ref[10:]
        return link(tag, f'{repoUrl}/releases/tag/{tag}')
    else:
        return ref


def commit(commit):
    shortSHA = commit['id'][:7]
    url = commit['url']
    author = commit['author']['name']
    commitMessage = commit['message']
    return f'{link(shortSHA, url)} - {commitMessage} by.{author}'


def prHead(pr):
    url = pr['html_url']
    number = pr['number']
    title = pr['title']
    repoName = pr['base']['repo']['name']
    userName = pr['user']['login']
    userUrl = pr['user']['html_url']
    return f'{link(f"{repoName}#{number} {title}", url)}{br()}by. {link(userName, userUrl)}'


def prBody(pr):
    return pr['body']
