def titleToNumber(columnTitle: str) -> int:
    col_num = 0
    for i in columnTitle:
        col_num = col_num * 26 + (ord(i) - 64)
    return col_num


print(titleToNumber("AA"))
