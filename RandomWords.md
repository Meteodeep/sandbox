<code> >>> from random_words import RandomWords
>>> rw = RandomWords()
>>> word = rw.random_word()
>>> print word
factors

>>> word = rw.random_word('y')
>>> print word
yards

>>> words = rw.random_words(count=10)
>>> print words
['runs', 'experience', 'comments', 'freedom', 'permit', 'honks', 'pins', 'texts', 'grant', 'fathers']

>>> words = rw.random_words(letter='r', count=5)
>>> print words
['raincoat', 'reactance', 'room', 'relocation', 'rudders']

>>> words = rw.random_words(letter=None, count=2)
>>> print words
['tides', 'eights'] </code>
