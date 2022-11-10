# a class that implement CHAIN OF RESPONSIBILITY pattern in python to apply a list of filters to a string.
""" Here is the explanation for the code above:
1. We have an abstract class Filter which has a method apply() which takes a text as an argument and returns the text.
2. It also has a method set_next() which takes the next filter in the chain.
3. The next filter is stored in the instance variable next.
4. The class Capitalize inherits from Filter and overrides the apply() method to return the text with the first letter capitalized.
5. The class Lowercase inherits from Filter and overrides the apply() method to return the text in lowercase.
6. The class Uppercase inherits from Filter and overrides the apply() method to return the text in uppercase.
7. The class Space inherits from Filter and overrides the apply() method to return the text without any spaces.
8. The class Reverse inherits from Filter and overrides the apply() method to return the text in reverse.
9. The class FilterChain is used to create a chain of filters.
10. It has a method add_filter() which takes a filter and adds it to the list of filters.
11. It also has a method apply() which takes a text and applies all the filters in the chain to the text and returns the text.
12. The apply() method calls the apply() method of the first filter in the chain and passes the text to it.
13. The first filter in the chain then calls the apply() method of the next filter in the chain and passes the text to it.
14. This keeps on happening until there are no more filters in the chain and the text is returned.
15. The final text is returned by the apply() method of the last filter in the chain. 

This is an example for calling this function: 

if __name__ == "__main__":

    filter_chain = FilterChain()
    filter_chain.add_filter(Lowercase())
    filter_chain.add_filter(Space())
    filter_chain.add_filter(Reverse())
    filter_chain.add_filter(Capitalize())
    filter_chain.add_filter(Uppercase())

    print(filter_chain.apply("Hello world!")) """


class Filter:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next

    def apply(self, text):
        if self.next:
            return self.next.apply(text)
        return text

class Capitalize(Filter):
    def apply(self, text):
        return text.capitalize()

class Lowercase(Filter):
    def apply(self, text):
        return text.lower()

class Uppercase(Filter):

    def apply(self, text):
        return text.upper()

class Space(Filter):
    def apply(self, text):
        return text.replace(" ", "")

class Reverse(Filter):

    def apply(self, text):
        return text[::-1]

class FilterChain:


    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        self.filters.append(filter)

    def apply(self, text):
        for filter in self.filters:
            text = filter.apply(text)
        return text

if __name__ == "__main__":

    filter_chain = FilterChain()
    filter_chain.add_filter(Lowercase())
    filter_chain.add_filter(Space())
    filter_chain.add_filter(Reverse())
    filter_chain.add_filter(Capitalize())
    filter_chain.add_filter(Uppercase())

    print(filter_chain.apply("Hello world!")) 