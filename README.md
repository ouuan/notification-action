# Notification Messages

GitHub Actions for generating notification messages for various GitHub webhook events :bell:

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/657169ad6bcc4e449e4a66efad58d630)](https://www.codacy.com/manual/ouuan/notification-action?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ouuan/notification-action&amp;utm_campaign=Badge_Grade)
[![GitHub Actions Status](https://github.com/ouuan/notification-action/workflows/CI%20Test/badge.svg)](https://github.com/ouuan/notification-action/actions?query=workflow%3A"CI+Test")

## Get Started

```yaml
name: Notification
on: [push]
jobs:
  notification:
    runs-on: ubuntu-latest
    steps:
    - name: "Get the message"
      uses: ouuan/notification-action@master
      id: get-message
      with:
      	format: markdown
    - name: "Output the message"
      run: echo '${{ steps.get-message.outputs.message }}'
```

## Demo

### Plain Text

```plaintext
ouuan forced-pushed 1 commit to ouuan/notification-action:master:

49b264e - feat: Add format option by.ouuan
```

### Markdown

> ouuan pushed [2 commits](https://github.com/ouuan/notification-action/compare/49b264ec0ff0...fdf637251330) to [ouuan/notification-action](https://github.com/ouuan/notification-action):[master](https://github.com/ouuan/notification-action/tree/master):
>
> [f7e4c1c](https://github.com/ouuan/notification-action/commit/f7e4c1cdb2b2a92277f25fab8bcc827e466aa89a) - refactor: Fix Codacy issue by.ouuan  
> [fdf6372](https://github.com/ouuan/notification-action/commit/fdf6372513306d995930ea62eaf151564f8103b4) - refactor: Change the order of inputs by.ouuan 

## Inputs

**Tips**: You don't have to manually set `event-name` and `event-json`, just use the default values.

|    Name    |                         Description                          |            Default            |
| :--------: | :----------------------------------------------------------: | :---------------------------: |
|   format   | The output format. Possible values: "markdown", "plaintext". |          `plaintext`          |
| event-name |                The name of the webhook event.                |  `${{ github.event_name }}`   |
| event-json |             The webhook event converted to JSON.             | `${{ toJSON(github.event) }}` |

## Outputs

**Tips**: You can use `steps.<step id>.outputs.message` to get the output. See [GitHub Help](https://help.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#steps-context) for more information.

|  Name   |        Description        |
| :-----: | :-----------------------: |
| message | The notification message. |

## Supported webhook events

|                                                Name                                                | PlainText | Markdown |
| :------------------------------------------------------------------------------------------------: | :-------: | :------: |
| [push](https://help.github.com/en/actions/reference/events-that-trigger-workflows#push-event-push) |     √     |    √     |

## Example usage

You can use this with other GitHub Actions like [appleboy/telegram-action](https://github.com/appleboy/telegram-action):

```yaml
name: telegram message
on: [push]
jobs:
  notification:
    runs-on: ubuntu-latest
    steps:
    - name: "Get the message"
      uses: ouuan/notification-action@master
      id: get-message
    - name: "Send the message"
      uses: appleboy/telegram-action@master
      with:
        to: ${{ secrets.TELEGRAM_TO }}
        token: ${{ secrets.TELEGRAM_TOKEN }}
        args: ${{ steps.get-message.outputs.message }}
```
