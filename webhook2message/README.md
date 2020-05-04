## webhook2message

This is a module used for generating notification messages for GitHub webhook events.

External programs only need to call `webhook2message.message`.

The message for each webhook event is generated in a separate file.

All formats should be processed in [_partials](_partials.py). It's also recommended to process resuable compoments of the webhook events in [_partials](_partials.py).
