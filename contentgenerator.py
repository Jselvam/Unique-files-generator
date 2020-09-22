import random
import string


class ContentGenerator:
    """
    Generate all type of file content here
    """

    def __init__(self):
        self.special_characters = '@_!#$%^&*?|~:'

    def getCharString(self, lowercase=True,
                      uppercase=True,
                      digits=True,
                      specialChar=True):
        """ Get all english characters
        @:param lowercase bool
        @:param uppercase bool
        @:param digits bool
        @:param specialChar bool
        @:returns string"""

        letters = ''
        if lowercase:
            letters += string.ascii_lowercase
        if uppercase:
            letters += string.ascii_uppercase
        if digits:
            letters += string.digits
        if specialChar:
            letters += self.special_characters

        return letters

    def getRandomNumber(self, range=10000):
        """ get random number with range
        @:param range int
        @:returns int"""

        random_num = random.randrange(range)
        return random_num

    def getRandomString(self, length=None, enletters=None):
        """ get Random string with specific length
        @:param length int
        @:param enletters string
        @:returns string """

        if length is None:
            length = self.getRandomNumber()
        if enletters is None:
            enletters = self.getCharString()
        result_str = ''.join(random.choice(enletters) for i in range(length))

        return result_str


if __name__ == '__main__':
    util = ContentGenerator()
    enchar = util.getCharString(specialChar=False)
    random_str = util.getRandomString(10, enchar)
    print(random_str)
