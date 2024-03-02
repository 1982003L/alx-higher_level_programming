#!/usr/bin/python3


if __name__ == '__main__':
    from urllib.request import urlopen
    import sys
    url = sys.argv[1]
    with urlopen(url) as response:
        response_headers = response.info()
        print(response_headers.get('X-Request-Id'))
