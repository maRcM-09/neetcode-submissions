class StringIterator:

    def __init__(self, compressedString: str):
        self.chars = []
        self.nums = []
        i = 0
        while i < len(compressedString):
            # Current position contains the character
            self.chars.append(compressedString[i])
            i += 1
            # Read the entire number after the character
            count = 0
            while i < len(compressedString) and compressedString[i].isdigit():
                count = count * 10 + int(compressedString[i])
                i += 1
            self.nums.append(count)
        self.index = 0
        self.char_counter = 1
    def next(self) -> str:
        to_return = self.chars[self.index%len(self.chars)]
        if self.nums[self.index] == self.char_counter:
            self.index += 1
            self.char_counter = 1
        else:
            self.char_counter += 1
        return to_return

    def hasNext(self) -> bool:
        return self.index < len(self.chars)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
