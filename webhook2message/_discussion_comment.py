import webhook2message._partials as p


def message(e):
    action = e['action']
    comment = e['comment']
    discussion = e['discussion']
    repo = e['repository']

    comment_link = p.link('New comment', comment['html_url'])
    repo_title =  p.link(f"{repo['name']}#{discussion['number']}", discussion['html_url'])
    discussion_title = discussion['title']
    user_link = p.link(comment['user']['login'], comment['user']['html_url'])

    if action == 'created':
        return p.paragraph(f"{comment_link} on {repo_title} {discussion_title} by {user_link}") + comment['body']
    else:
        raise Exception(
            f'The action {action} in the discussion_comment event is not supported.')
