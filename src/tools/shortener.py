import pyshorteners # pip install pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

def main():
    long_url = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(long_url)
    print(f"Shortened URL: {shortened_url}")

if __name__ == "__main__":
    main()
