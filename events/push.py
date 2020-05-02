import json
import events.formatter as fmt


def message(e):
    commits = e['commits']
    forced = bool(e['forced'])
    compareUrl = e['compare']
    repoName = e['repository']['full_name']
    repoUrl = e['repository']['html_url']
    pusherName = e['pusher']['name']
    ref = e['ref']
    if ref[:11] == 'refs/heads/':
        branch = ref[11:]
        ref = fmt.link(
            branch, '{}/tree/{}'.format(repoUrl, branch))
    elif ref[:10] == 'refs/tags/':
        tag = ref[10:]
        ref = fmt.link(tag, '{}/releases/tag/{}'.format(repoUrl, tag))
    message = fmt.paragraph('{} {}pushed {} to {}:{}:'.format(
        pusherName, 'forced-' if forced else '', fmt.link('{} commit{}'.format(len(commits), 's' if len(commits) >= 2 else ''), compareUrl), fmt.link(repoName, repoUrl), ref))
    for commit in commits:
        shortSHA = commit['id'][:7]
        url = commit['url']
        author = commit['author']['name']
        commitMessage = commit['message']
        message += '{} - {} by.{}{}'.format(
            fmt.link(shortSHA, url), commitMessage, author, fmt.br())
    return message
