import webhook2message._partials as p


def message(e):
    action = e['action']
    comment = e['comment']
    discussion = e['discussion']
    if action == 'created':
        return p.paragraph(f"New comment on {p.link(discussion['title'], comment['html_url'])} by {p.link(comment['user']['login'], comment['user']['html_url'])}") + comment['body']
    else:
        raise Exception(
            f'The action {action} in the pull_request event is not supported.')
