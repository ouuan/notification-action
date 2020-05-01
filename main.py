import sys
import json

def pushMessage(e):
    commits = e['commits']
    forced = bool(e['forced'])
    compareUrl = e['compare']
    repoName = e['repository']['full_name']
    repoUrl = e['repository']['html_url']
    pusherName = e['pusher']['name']
    ref = e['ref']
    if ref[:11] == 'refs/heads/':
        ref = '[{0}]({1}/tree/{0})'.format(ref[11:], repoUrl)
    elif ref[:10] == 'refs/tags/':
        ref = '[{0}]({1}/releases/tag/{0})'.format(ref[10:], repoUrl)
    message = '{} {}pushed [{} commit{}]({}) to [{}]({}):{}:\n\n'.format(pusherName, 'forced-' if forced else '', len(commits), 's' if len(commits) >= 2 else '', compareUrl, repoName, repoUrl, ref)
    for commit in commits:
        shortSHA = commit['id'][:7]
        url = commit['url']
        author = commit['author']['name']
        commitMessage = commit['message']
        message += '[{}]({}) - {} by.{}  \n'.format(shortSHA, url, commitMessage, author)
    return message

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print('python main.py <event type> <event json>')
        raise Exception('The number of arguments is {}, expected 2'.format(len(sys.argv) - 1))

    eventType = sys.argv[1]
    eventJson = json.loads(sys.argv[2])

    if eventType == 'push':
        print(pushMessage(eventJson))
    else:
        raise Exception('The event type {} is unsupported'.format(eventType))
