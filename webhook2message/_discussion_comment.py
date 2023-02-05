import webhook2message._partials as p


def message(e):
    action = e['action']
    comment = e['comment']
    discussion = e['discussion']
    repo = e['repository']

    title =  p.link(f"{repo['name']}#{discussion['number']} {discussion['title']}", comment['html_url'])

    if action == 'created':
        return p.paragraph(f"New {'reply' if comment['parent_id'] else 'comment'} on {title} by {p.user(comment['user'])}") + comment['body']
    else:
        raise Exception(
            f'The action {action} in the discussion_comment event is not supported.')
