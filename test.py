import json
import sys

import webhook2message as msg


def runTest(name):
    print(f'test {name} began')
    with open(f'tests/{name}.json') as testFile:
        tests = json.load(testFile)
    for test in tests:
        for fmt in test['formats']:
            message = msg.message(test['name'], test['event'], fmt['format'])
            if message != fmt['message']:
                raise Exception(f'''event-name: <{test["name"]}>

event-json: "{test["event"]}"

format: "{fmt["format"]}"

expected message: "{fmt["message"]}"

generated message: "{message}"''')
    print(f'test {name} passed')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        from os import listdir
        from os.path import isfile, join
        tests = [f[:-5]
                 for f in listdir('tests') if isfile(join('tests', f)) and f[-5:] == '.json']
    else:
        tests = sys.argv[1:]
    for test in tests:
        runTest(test)
