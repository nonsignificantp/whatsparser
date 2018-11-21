# WhatsParser
## From WhatsApp chats to pandas data frame made easy

WhatsParser is a tool for parsing `.txt` chat files rendered by the WhatsApp messaging App. Is intended to make the shift from WhatsApp data to pandas dataframe as rapid as possible. Reading and parsing the `.txt` file is as simple as:

```python
from whatsparser import WhatsParser

messages = WhatsParser('./chat.txt')
```

Once the file has been parsed, all messages are stored as dictionaries with three keys: _datetime_, _author_ and _content_. You can access each of this dictionaries by indexing:

```Python
len(messages) # Get how many messages there are
>> 3590

messages[35] # Get a message
>> {'datetime': datetime.datetime(2017, 9, 15, 19, 10, 2),
    'author': 'Agustin Rodriguez',
    'content': 'Hi! this is a Whatsapp message'}
```

The datetime key stores a datetime object, all the others have string as values.

### Pandas dataframe

Converting all messages into a pandas DataFrame so you can use your favorite tools for data analysis is as easy as:

```Python
df = messages.to_dataframe() # Returns a pandas dataframe
```

## Looping

WhatsParser also offer the posibility of iterate through the object using various functions. When iterating over `messages` a copy is made of all messages stored and iteration and changes ocurrs over this copy. It is possible to change the data store inside `messages` by assigning the results of the iteration to `messages.data`.

### Filter messages

```Python
def find_long_messages(message):
  if len(message['content']) > 100:
    return True
  return False

messages.data = list(filter(find_long_messages, messages))
# Now, messages contains only those messages with a length greater than 100 characters.
```

### List comprehension

```Python
from emoji import get_emoji_regexp

def remove_emojis(message):
  message['content'] = get_emoji_regexp().sub(r'', message['content'])
  return message

messages.data = [remove_emojis(message) for message in messages]
# All messages got their emojis remove from the text
```

### Map function

```Python
def remove_emojis(message):
  message['content'] = get_emoji_regexp().sub(r'', message['content'])
  return message

messages.data = list(map(remove_emojis, messages))
```

### For loop

It is possible to change the content of the WhatsParser object on the fly using a for loop iterating through `messages.data`. If no changes to the object are required, you can yous iterate through `messages`:

Iterate over `messages.data` to make changes on the fly, if no just use `messages`.

```Python
# For changing data
for message in messages.data:
  message['content'] = 'NEW CONTENT'

# Without changing the data
for message in messages:
  print(message['author'])

```
