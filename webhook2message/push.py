import webhook2message.partials as p


def message(e):
    commits = e['commits']
    forced = e['forced']
    compareUrl = e['compare']
    pusherName = e['pusher']['name']
    forcedPush = 'forced-' if forced else ''
    compare = p.link(
        f'{len(commits)} commit{"s" if len(commits) >= 2 else ""}', compareUrl)
    repo = p.repo(e['repository'])
    ref = p.ref(e['ref'], e['repository'])
    message = p.paragraph(
        f'{pusherName} {forcedPush}pushed {compare} to {repo}:{ref}:')
    for commit in commits:
        message += p.commit(commit) + p.br()
    return message
