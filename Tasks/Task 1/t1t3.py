def self_concat_quantity(s: str):
    ans = 0
    buffer_str = str()


    for ind, char in enumerate(s):
        if char in buffer_str:
            cur_buf = buffer_str
            while char in cur_buf:
                buf_ind = cur_buf.index(char)
                # make buffer start with current char
                while not cur_buf.startswith(char):
                    cur_buf = cur_buf[buf_ind:]
                # compare buffer with slice of original string
                if cur_buf == s[ind:ind+len(cur_buf)] :
                    ans += 1
                # remove first left occurence of current char
                cur_buf = cur_buf[buf_ind+1:]
        buffer_str += char

    return ans


print(self_concat_quantity("abc_abcabc_abc"))