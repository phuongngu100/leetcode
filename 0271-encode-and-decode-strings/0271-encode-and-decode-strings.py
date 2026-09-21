class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        print(''.join(res))
        return ''.join(res)
        # 5#Hello5#World

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i= 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # 5#Hello5#World
            # Move past '#' ----- now i = 2 means H and j + 5 is char 5 so to o in Hello
            i = j+ 1
            j = i + length
            res.append(s[i:j])

            i = j # set i to j
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))