from queues import deque

d = deque(["A", "B", "C", "D"])

decrypted = "AAABBBCCCDDD"


def decrypt(encrypted: str) -> str:
    decrypted = ""
    for char in encrypted:
        while d.peek_right() != char:
            d.push_right(d.pop_left())
        d.push_right(d.pop_left())
        decrypted += d.peek_left()
        d.push_left(d.pop_right())
    return decrypted


def encrypt(decrypted: str) -> str:
    encrypted = ""
    for char in decrypted:
        while d.peek_left() != char:
            d.push_left(d.pop_right())
        d.push_left(d.pop_right())
        encrypted += d.peek_right()
        d.push_right(d.pop_left())
    return encrypted


print(decrypted)
print(encrypt(decrypted))
print(decrypt(encrypt(decrypted)))
