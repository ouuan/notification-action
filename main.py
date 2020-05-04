import sys
import json

import webhook2message.partials as p
import webhook2message.push as push

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print('python main.py <event-name> <event-json> <format>')
        raise Exception(
            f'The number of arguments is {len(sys.argv) - 1}, expected 3')

    eventName = sys.argv[1]
    eventJson = json.loads(sys.argv[2])
    messageFormat = sys.argv[3]

    p.setFormat(messageFormat)

    if eventName == 'push':
        print(push.message(eventJson))
    else:
        raise Exception(f'The event "{eventName}" is unsupported')
