file = open("server_log.txt",'r')
content = file.read()
lines = content.splitlines()
words = content.split()

print(f"Total Lines: {len(lines)}")
print(f"Total Words: {len(words)}")
print(f"Total Characters: {len(content)}")
