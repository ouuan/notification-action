import webhook2message._partials as p


def message(e):
    action = e['action']
    pr = e['pull_request']
    if action == 'opened':
        return 'New pull request ' + p.paragraph(p.prHead(pr)) + p.prBody(pr)
    else:
        raise Exception(
            f'The action {action} in the pull_request event is not supported.')
