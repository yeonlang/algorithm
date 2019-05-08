def find_message(text):
    ans = ''
    for s in text:
        if s.isupper():
            ans+=s
    return ans


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO","hello"
    assert find_message("hello world!") == "","Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD","Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
