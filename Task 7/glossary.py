from collections import OrderedDict

def create_glossary():
    glossary = OrderedDict()
    glossary['function'] = 'A block of code that performs a specific task.'
    glossary['variable'] = 'A reserved memory location to store values.'
    glossary['list'] = 'A collection of items in a particular order.'
    glossary['loop'] = 'A control structure that repeatedly executes a block of code.'
    glossary['dictionary'] = 'A collection of key-value pairs.'
    return glossary

def display_glossary(glossary):
    for term, definition in glossary.items():
        print(f"{term.title()}: {definition}")
