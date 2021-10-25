import random


class Chromosome:
    """ Class, representing a chromosome.
    Each chromosome is 10 bits long: 1 bit for sign, 2 bits for integer part
    and 7 bits for fractional part.

    Since numbers not larger than 127 can be
    encoded with 7 bits and in my chromosome representation the fractional
    part is encoded "as it is" than the binary representation of fractional
    part can not be larger than 0b01100011. """

    def __init__(self, x=None):
        """ The chromosome can be created randomly (if no parameter was
        given) or from a 10 bit integer number (x) by rules, described
        above. """
        if x is None:
            self.sign = random.randint(0, 1)
            self.integer_part = random.randint(0, 3)
            self.fractional_part = random.randint(0, 99)

        else:
            self.sign = (x & 512) >> 9
            self.integer_part = (x & 384) >> 7
            self.fractional_part = x & 127

            if self.integer_part > 99:
                self.integer_part = 99

    def __str__(self):
        return str(round(self.get_float_representation(), 2))

    def get_binary_representation(self):
        binary_representation = (self.sign << 9) + \
                                (self.integer_part << 7) + \
                                self.fractional_part
        return binary_representation

    def get_float_representation(self):
        if self.sign == 1:
            return -1 * (self.integer_part + self.fractional_part * (10 ** (-2)))
        else:
            return self.integer_part + self.fractional_part * (10 ** (-2))


# DEBUG SECTION

def main():
    c = Chromosome()
    print(c.get_float_representation())
    print(bin(c.get_binary_representation()))

    d = Chromosome(c.get_binary_representation())
    print(d.get_float_representation())
    print(bin(d.get_binary_representation()))


if __name__ == '__main__':
    main()
