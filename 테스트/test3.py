def trans(s):
    if ord('1')<=ord(s)<=ord('9'):
        return int(s)
    else:
        return ord(s)-55

print(trans('3'))