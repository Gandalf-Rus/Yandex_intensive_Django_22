class MagicalSilence:
    def __init__(self, country, audibility_threshold, muffl_magic):
        self.country = country
        self.audibility_threshold = audibility_threshold
        self.muffl_magic = muffl_magic

    def __gt__(self, other):
        if self.audibility_threshold > other.audibility_threshold:
            if self.muffl_magic > other.muffl_magic:
                if self.country > other.country:
                    return True
        return False

    def __lt__(self, other):
        if not self.__gt__(other):
            return True
        return False

    def __eq__(self, other):
        if self.audibility_threshold == other.audibility_threshold:
            if self.muffl_magic == other.muffl_magic:
                if self.country == other.country:
                    return True
        return False

    def __ne__(self, other):
        if not self.__eq__(other):
            return True
        return False

    def __ge__(self, other):
        if self.__gt__(other) or self.__eq__(other):
            return True
        return False

    def __le__(self, other):
        if self.__lt__(other) or self.__eq__(other):
            return True
        return False

    def __mul__(self, other):
        country = self.country + other.country
        audibility_threshold = min([self.audibility_threshold, other.audibility_threshold])
        muffl_magic = sum([self.muffl_magic, other.muffl_magic]) // 2
        return MagicalSilence(country, audibility_threshold, muffl_magic)

    def __iadd__(self, number):
        self.muffl_magic += number
        if (self.audibility_threshold - number // 3) > 1:
            self.audibility_threshold = self.audibility_threshold - number // 3
        return self

    def __truediv__(self, number):
        list_of_MS = []
        all_magic = self.muffl_magic
        for i in range(number):
            audibility_threshold = self.audibility_threshold * number
            magic = 0
            if all_magic >= 1:
                all_magic -= 1
                magic = 1
            list_of_MS.append(MagicalSilence(self.country, audibility_threshold, magic))
        return list_of_MS

    def __call__(self, number):
        return (self.audibility_threshold + len(self.country)) * self.muffl_magic // number

    def __str__(self):
        return f"Silence in {self.country}, low {self.audibility_threshold}, magic {self.muffl_magic}."

    def __repr__(self):
        return f"MagicalSilence('{self.country}', {self.audibility_threshold}, {self.muffl_magic})"

    def add_magic(self, number):
        self.muffl_magic += number
        if self.muffl_magic < 1:
              self.muffl_magic = 1


# ms = MagicalSilence("Fog", 25, 2)
# ms1 = MagicalSilence("Hills", 16, 9)
# print(ms >= ms1, ms != ms1, ms < ms1)
# print(ms, ms1, sep="\n")
# print()
# res = ms / 3
# res[0] += 5
# print(ms, ms1, res, sep="\n")
# print(ms(13), res[0](5))
