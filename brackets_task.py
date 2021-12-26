"""
Write a function that will check if all open brackets are closed in the correct order
in a string of any length, among any characters.
The method must accept the string and return `True` if all brackets are closed in the correct order,
otherwise `False`. Here are some examples:

1. ([{}]) - True.
2. ab3(#$%[pop]cvfs){kek} - True.
3. (["{]} - False
4. lol(kek{4eburek])}[ - False
"""

str1 = "([{}])"                     # True
str2 = "ab3(#$%[pop]cvfs){kek}"     # True
str3 = "(['{]}"                     # False
str4 = "lol(kek{4eburek])}["        # False
str5 = "{[]{()}}"                   # True
str6 = "((ea)t [olo] a)"            # True
str7 = "((ea][olo))"                # False
str8 = "([( asa]) mas)"             # False
str9 = "(af[obd] {er}) [sw(hj)]"    # True


def brackets(string: str = '') -> bool:
    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    checklist = []
    for i in string:
        if i in open_brackets:
            checklist.append(i)
        elif i in close_brackets:
            index_bracket = close_brackets.index(i)
            if len(checklist) > 0 and open_brackets[index_bracket] == checklist[len(checklist) - 1]:
                checklist.pop()
            else:
                return False
    return True if len(checklist) == 0 else False


print(brackets(str1))
print(brackets(str2))
print(brackets(str3))
print(brackets(str4))
print(brackets(str5))
print(brackets(str6))
print(brackets(str7))
print(brackets(str8))
print(brackets(str9))
