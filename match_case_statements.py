# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

# switch => match
# default => _
# break 문은 사용 X
def grades(grade):
    match grade:
        case "a" | "A":
            return "You did perfect"
        case "b" | "B":
            return "You did good"
        case "c" | "C":
            return "You did ok"
        case "d" | "D":
            return "You did bad"
        case "f" | "F":
            return "You failed"
        case _:
            return "Not a valid grade"

print(grades("A"))
print(grades("b"))
print(grades("C"))
print(grades("d"))
print(grades("F"))
print(grades("pizza"))
