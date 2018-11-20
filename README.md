A tool for parsing `.txt` chat files rendered by the WhatsApp messaging App.

Reading the `.txt` file is as simple as:

```python
from whatsparser import WhatsParser

messages = WhatsParser('./chat.txt')
```

With the file already parsed you can:

```Python
# Access to individual instances of messanges
messages[35]
>> '2017-09-15 19:10:02 - Agustin Rodriguez: Hi! this is a Whatsapp message'

# Acces to the three properties of a message
messages[35].datetime
>> datetime.datetime(2017, 9, 15, 19, 10, 2) # Returns a datetime object
messages[35].author
>> 'Agustin Rodriguez'
messages[35].content
>> 'Hi! this is a Whatsapp message'
```

Convert all messages into a pandas DataFrame so you can use your favorite tools for data analysis

```Python
df = messages.to_dataframe() # Returns a pandas dataframe
```
