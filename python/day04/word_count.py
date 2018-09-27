import sys
import time

start = time.time()

f = open('the_little_prince.txt')
text = f.read()
print(len(text))
for t in text:
      print(t)

end = time.time()
print("Elapsed time:", str((end - start)))      