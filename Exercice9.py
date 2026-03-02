#QUESTION 9
#Write a function that checks if the passed parameter is a valid URL or not.
#Do some research as to what is a valid URL. Please also explain your reasoning.
#Use only the concepts that we learned in class.

def is_valid_url(url):

    url = url.strip()

    # 1) No spaces (a simple quick fail)
    if " " in url:
        return False

    # 2) Must start with http:// or https://
    if url.find("http://") == 0:
        rest = url[7:]   # remove "http://"
    elif url.find("https://") == 0:
        rest = url[8:]   # remove "https://"
    else:
        return False

    # 3) Extract host: everything up to the first "/" (or whole rest if no "/")
    slash_index = rest.find("/")
    if slash_index == -1:
        host = rest
    else:
        host = rest[:slash_index]

    # 4) Host must not be empty and should contain a dot (example.com)
    if len(host) == 0:
        return False
    if "." not in host:
        return False

    # 5) Very simple character check for the host (letters/digits/dot/hyphen)
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    for ch in host:
        if ch not in allowed:
            return False

    # Avoid hosts like ".com" or "example."
    if host[0] == "." or host[-1] == ".":
        return False

    return True



