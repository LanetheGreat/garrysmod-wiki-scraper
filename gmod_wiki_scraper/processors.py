''' Custom process classes for item data input/output modification. '''

from textwrap import TextWrapper


# Output only processor (Multi in/1 out)
class Join(object):
    ''' Calls .join on the supplied text for all it's input values. '''

    def __init__(self, text):
        self.text = str(text)

    def __call__(self, values):
        return self.text.join(map(str, values))


# Input/Output processor (Multi in/Multi out)
class Prefix(object):
    ''' Adds a prefix text before each input value. '''

    def __init__(self, prefix=''):
        self.prefix = prefix

    def __call__(self, values):
        for value in values:
            yield self.prefix + str(value)


# Output processor (Multi in/1 out)
class PrefixOne(object):
    ''' Adds a prefix text before it's final output. '''

    def __init__(self, prefix=''):
        self.prefix = prefix

    def __call__(self, text):
        return self.prefix + str(text)


# Input/Output processor (Multi in/Multi out)
class Split(object):
    ''' Splits each input value by a separator, at most maxsplit times. '''

    def __init__(self, sep=None, maxsplit=-1):
        self.sep = sep
        self.maxsplit = maxsplit

    def __call__(self, values):
        for value in values:
            yield from str(value).split(self.sep, self.maxsplit)


# Input/Output processor (Multi in/Multi out)
class Suffix(object):
    ''' Adds a suffix text after each input value. '''

    def __init__(self, suffix=''):
        self.suffix = suffix

    def __call__(self, values):
        for value in values:
            yield str(value) + self.suffix


# Input/Output processor (Multi in/1 out)
class SuffixOne(object):
    ''' Adds a suffix text after it's final output. '''

    def __init__(self, suffix=''):
        self.suffix = suffix

    def __call__(self, text):
        return str(text) + self.suffix


# Output only processor (1 in/1 out)
class TextWrap(object):
    ''' Wrapper callable class for TextWrap.TextWrapper's wrap function. '''

    def __init__(self, width=70, **kwargs):
        self.wrapper = TextWrapper(width=width, **kwargs)

    def __call__(self, text):
        return self.wrapper.wrap(text)
