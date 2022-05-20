from queues import deque

d = deque(["A", "B", "C", "D"])

decrypted = "AAABBBCCCDDD"


def decrypt(encrypted: str) -> str:
    decrypted = ""
    for char in encrypted:
        while d.peekright() != char:
            d.pushright(d.popleft())
        # if d.peekright() == char:
        d.pushright(d.popleft())
        decrypted += d.peekleft()
        d.pushleft(d.popright())
    return decrypted


def encrypt(decrypted: str) -> str:
    encrypted = ""
    for char in decrypted:
        while d.peekleft() != char:
            d.pushleft(d.popright())
        d.pushleft(d.popright())
        encrypted += d.peekright()
        d.pushright(d.popleft())
    return encrypted


print(decrypted)
print(encrypt(decrypted))
print(decrypt(encrypt(decrypted)))
