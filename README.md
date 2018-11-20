A tool for parsing `.txt` chat files rendered by the WhatsApp messaging App.

Reading the `.txt` file is as simple as:

```python
from whatsparser import WhatsParser

messages = WhatsParser('./chat.txt')
```

With the file already parsed you can access to individual messages:

```Python
messages[35]
>> '2017-09-15 19:10:02 - Agustin Rodriguez: Hi! this is a Whatsapp message'
```

Get the datetime, author or content from each message:

```Python
messages[35].datetime # Returns a datetime object
>> datetime.datetime(2017, 9, 15, 19, 10, 2)

messages[35].author
>> 'Agustin Rodriguez'

messages[35].content
>> 'Hi! this is a Whatsapp message'

messages[35].size # Returns the length of the content as an integer
>> 30

```

Convert all messages into a pandas DataFrame so you can use your favorite tools for data analysis

```Python
df = messages.to_dataframe() # Returns a pandas dataframe
```

### Filter messages

```Python
def find_long_messages(message):
  if message.size > 100:
    return True
  return False

filter(find_long_messages, messages)
```

### Map function

```Python
from emoji import get_emoji_regexp

def remove_emojis(message):
  message.content = get_emoji_regexp().sub(r'', message.content)
  return message

map(remove_emojis, messages)
```

### For loop

```Python
for message in messages:
  print(f"Sender: {message.author} | Size of message: {message.size}")
```
