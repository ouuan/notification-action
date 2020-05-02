import sys
import json

import events.formatter
import events.push

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print('python main.py <event-name> <event-json> <format>')
        raise Exception(
            'The number of arguments is {}, expected 3'.format(len(sys.argv) - 1))

    eventName = sys.argv[1]
    eventJson = json.loads(sys.argv[2])
    messageFormat = sys.argv[3]

    events.formatter.setFormat(messageFormat)

    if eventName == 'push':
        print(events.push.message(eventJson))
    else:
        raise Exception('The event "{}" is unsupported'.format(eventName))
