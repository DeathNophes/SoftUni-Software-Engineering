version = input()
version_int = version.replace(".", "")
next_version = int(version_int) + 1
print(".".join(str(next_version)))