import webhook2message.partials as p


def message(e):
    commits = e['commits']
    forced = e['forced']
    compareUrl = e['compare']
    pusherName = e['pusher']['name']
    message = p.paragraph('{} {}pushed {} to {}:{}:'.format(
        pusherName, 'forced-' if forced else '', p.link('{} commit{}'.format(len(commits), 's' if len(commits) >= 2 else ''), compareUrl), p.repo(e['repository']), p.ref(e['ref'], e['repository'])))
    for commit in commits:
        message += p.commit(commit) + p.br()
    return message
