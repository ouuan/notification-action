import sys
import json

import webhook2message as msg

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print('python main.py <event-name> <event-json> <format>')
        raise Exception(
            f'The number of arguments is {len(sys.argv) - 1}, expected 3')

    eventName = sys.argv[1]
    eventJson = json.loads(sys.argv[2])
    messageFormat = sys.argv[3]

    print(msg.message(eventName, eventJson, messageFormat))
