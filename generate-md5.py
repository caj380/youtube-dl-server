import sys
import hashlib

print(hashlib.md5(sys.argv[1].encode()).hexdigest())
print(hashlib.md5(sys.argv[2].encode()).hexdigest())
