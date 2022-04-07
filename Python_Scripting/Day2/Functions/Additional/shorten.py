def shorten(text, length=25, indicator="..."):
    """Returns text or a truncated copy with the indicator added
    text is any string; length is the maximum length of the returned
    string (including any indicator); indicator is the string added at
    the end to indicate that the text has been shortened
    >>> shorten("Second Variety")
    'Second Variety'
    >>> shorten("Voices from the Street", 17)
    'Voices from th...'
    >>> shorten("Radio Free Albemuth", 10, "*")
    'Radio Fre*'
    """
    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text


text = shorten("The Silkie") # returns:  'The Silkie'
text = shorten(length=7, text="The Silkie")  #  returns:  'The  ...'
text = shorten("The Silkie", indicator="&", length=7) #  returns:  'The  Si&' 
text = shorten("The Silkie", 7, "&")  #  returns:  'The  Si&'

print(text)