import hashlib

def part1(code):
    password = ""
    index = 0
    while len(password) < 8:
        md5 = hashlib.md5((code + str(index)).encode('utf-8')).hexdigest()
        if md5[:5] == "00000":
            password += md5[5]
            print(password)
        index += 1
    return password


def part2(code):
    password = ["_"] * 8
    index = 0
    while "_" in password:
        md5 = hashlib.md5((code + str(index)).encode('utf-8')).hexdigest()
        if md5[:5] == "00000" and md5[5] in "01234567":
            pos = int(md5[5])
            if password[pos] == "_":
                password[pos] = md5[6]
                print("".join(password))
        index += 1
    return "".join(password)
