## Tests

### The JSON Files

The tests are stored as JSON files, the tests for each event are stored in separate files, the structure of each file is:

```json
[
    {
        "name": <string: event-name>,
        "event": <object: webhook event>,
        "formats": [
            {
                "format": <string: format>,
                "message": <string: the corresponding message to the event and the format>
            },
            ...<other formats>...
        ]
    },
    ...<other events>...
]
```

### Run tests

Just run [test.py](../test.py).

You can run it without arguments to run all tests, or use the names of the events as arguments to run those tests.
