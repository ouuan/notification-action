import webhook2message._partials as p


def message(e):
    action = e['action']
    comment = e['comment']
    discussion = e['discussion']
    repo = e['repository']
    title_repo =  p.link(f"{repo['name']}#{discussion['number']}", discussion['html_url'])
    title_comment = p.link(discussion['title'], comment['html_url'])
    if action == 'created':
        return p.paragraph(f"New comment on {title_repo} {title_comment} by {p.link(comment['user']['login'], comment['user']['html_url'])}") + comment['body']
    else:
        raise Exception(
            f'The action {action} in the discussion_comment event is not supported.')
