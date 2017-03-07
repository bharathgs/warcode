"""You are going to be given a word.
Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
 If the word's length is even, return the middle 2 characters."""


def get_middle(s):
        if len(s) > 2:
            if len(s) % 2 == 0:
                x = round(len(s)/2)
                return s[int(x-1):int(x+1)]
            else:
                return s[int(len(s)/2)]
            pass
        else:
            return s


'''we can also simply do this -
    def get_middle(s):
        return s[(len(s)-1)/2:len(s)/2+1]

        or
    def get_middle(s):
        index, odd = divmod(len(s), 2)
        return s[index] if odd else s[index - 1:index + 1]

        '''



