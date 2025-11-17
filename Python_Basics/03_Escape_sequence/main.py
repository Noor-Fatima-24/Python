# Day 3: Exploring Escape sequence in Python

print("Welcome to Day 3 of my Python learning journey!")

# escape sequences are special characters used inside strings to represent things that are hard or impossible to type directly

# Escape Sequence Examples

print("Hello\nWorld")          # \n = New line
print("Python\tProgramming")   # \t = Tab space
print('It\'s a sunny day!')    # \' = Single quote
print("He said, \"Its NOOR!\"")  # \" = Double quote
print("This is a backslash: \\")      # \\ = Backslash
print("12345\rABCD")           # \r = Carriage return
print("Python\b3")             # \b = Backspace
print("Hello\fWorld")          # \f = Form feed (page break)
print("Hello\vPython")         # \v = Vertical tab
print("\a")                    # \a = Bell (alert sound)
print("\110\145\154\154\157")  # \ooo = Octal values (Hello)
print("\x48\x65\x6c\x6c\x6f")  # \xhh = Hex values (Hello)
print("\N{COPYRIGHT SIGN}")
print("\u2764")                   # ❤
print("\U0001F600")               # 😀


# | **Escape Sequence** | **Meaning / Use**                                  | **Example**                        | **Output**                   |
# | ------------------- | -------------------------------------------------- | ---------------------------------- | ---------------------------- |
# | `\\`                | Backslash itself                                   | `print("This is a backslash: \\")` | This is a backslash: \       |
# | `\'`                | Single quote                                       | `print('It\'s OK')`                | It's OK                      |
# | `\"`                | Double quote                                       | `print("He said, \"Hi!\"")`        | He said, "Hi!"               |
# | `\n`                | New line                                           | `print("Hello\nWorld")`            | Hello<br>World               |
# | `\t`                | Horizontal tab                                     | `print("Name:\tVelora")`           | Name: Velora                 |
# | `\r`                | Carriage return (moves cursor to start of line)    | `print("Hello\rWorld")`            | World                        |
# | `\b`                | Backspace (removes one character)                  | `print("Helloo\b")`                | Hello                        |
# | `\f`                | Form feed (new page – rarely used)                 | `print("Hello\fWorld")`            | Hello (form feed) World      |
# | `\a`                | Bell/alert (produces a beep sound on some systems) | `print("\a")`                      | 🔔 (beep sound if supported) |
# | `\v`                | Vertical tab                                       | `print("Hello\vWorld")`            | Hello (vertical tab) World   |
# | `\ooo`              | Octal value                                        | `print("\110\145\154\154\157")`    | Hello                        |
# | `\xhh`              | Hexadecimal value                                  | `print("\x48\x65\x6C\x6C\x6F")`    | Hello                        |
# | `\N{name}`          | Unicode character by name                          | `print("\N{COPYRIGHT SIGN}")`      | ©                            |
# | `\uXXXX`            | Unicode (16-bit)                                   | `print("\u2764")`                  | ❤                            |
# | `\UXXXXXXXX`        | Unicode (32-bit)                                   | `print("\U0001F600")`              | 😀                           |

