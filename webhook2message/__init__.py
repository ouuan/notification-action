from webhook2message import _partials


def message(eventName, eventJson, messageFormat):
    """Generate the notification message for a webhook event.

    `eventName` is the name of the webhook event.

    `eventJson` is the webhook in JSON format.

    `messageFormat` is the format of the message.
    """

    _partials.setFormat(messageFormat)

    if eventName == 'push':
        from webhook2message import _push
        return _push.message(eventJson)
    elif eventName == 'pull_request':
        from webhook2message import _pull_request
        return _pull_request.message(eventJson)
    elif eventName == 'discussion_comment':
        from webhook2message import _discussion_comment
        return _discussion_comment.message(eventJson)
    else:
        raise Exception(f'The event "{eventName}" is unsupported')
