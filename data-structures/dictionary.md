[Home](https://python.cinhtau.net/)

## Dictionary

A useful data type built into Python is the dictionary.

- Dictionaries are `associative memories` or `associative arrays`.
- Dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.

## Storing Data in Dictionaries

This section handles how to add data to dictionaries.

## Accessing Data in Dictionaries


## Updating Dictionaries

This section describe how to update in dictionaries.

### Merge two Dictionaries

There are several possibilities to merge two dictionaries to a new one.

Copy the contents of each dictionary into a new dictionary.

```python
context = {}
context.update(defaults)
context.update(user)
```

Copy data into the new dictionary and update it with the remaining dictionary.

```python
context = defaults.copy()
context.update(user)
```

Create a new dictionary using the constructor with existing data. Update with the remaining dictionaries.

```python
context = dict(defaults)
context.update(user)
```

## Removing Data from Dictionaries

### Remove key

Remove key from dictionary

```python
my_dict.pop('key', None)
```
