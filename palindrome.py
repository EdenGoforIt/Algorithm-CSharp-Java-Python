

def palindrome(self, value: str) -> bool:
    qu = []
    st = []

    for c in value:
        if c.isalpha:
            qu.append(c)
            st.append(c)

    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True


print(palindrome("Madam, I'm Adam"))
