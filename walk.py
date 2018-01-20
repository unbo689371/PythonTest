import os

for root, dirs, files in os.walk("/tmp/"):
    print root
    for f in files:
        print os.path.join(root, f)