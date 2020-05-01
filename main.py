import sys
import json

import events.push

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print('python main.py <format> <event-type> <event-json>')
        raise Exception(
            'The number of arguments is {}, expected 3'.format(len(sys.argv) - 1))

    messageFormat = sys.argv[1]
    eventType = sys.argv[2]
    eventJson = json.loads(sys.argv[3])

    if eventType == 'push':
        print(events.push.message(eventJson, messageFormat))
    else:
        raise Exception('The event type {} is unsupported'.format(eventType))
