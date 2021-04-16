class Codec:
    def __init__(self):
        self.l2s = dict()
        self.s2l = dict()
        self.chList = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = "".join(choices(self.chList, k=6))
        if code not in self.s2l:
            self.s2l[code] = longUrl
            self.l2s[longUrl] = code
        return 'http://tinyurl.com/' + self.l2s[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.s2l[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
