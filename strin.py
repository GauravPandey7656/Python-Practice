from email.quoprimime import quote


quote="A quick brown fox jumps over the lazy dog"
if "quick" not in quote:
    print("Yes")
else:
    print("No")