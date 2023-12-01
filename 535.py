class Codec:

    def __init__(self):
        self.encode_url = {}
        self.decode_url = {}
        self.base = "http://tinyurl/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_url:
            shortened = self.base + str(len(self.encode_url) + 1)
            self.encode_url[longUrl] = shortened
            self.decode_url[shortened] = longUrl 
        return self.encode_url[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_url[shortUrl]




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))