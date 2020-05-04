from webhook2message import _partials, _push


def message(eventName, eventJson, messageFormat):
    _partials.setFormat(messageFormat)

    if eventName == 'push':
        return _push.message(eventJson)
    else:
        raise Exception(f'The event "{eventName}" is unsupported')
