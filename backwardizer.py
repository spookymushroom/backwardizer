def b(m):
    new = ""
    for l in m: new = l+new
    return new

from tkinter import Tk
r = Tk()
r.withdraw()
m = "foo"

while m! = '':
    m=input("Backwardizer> ")
    r.clipboard_clear()
    r.clipboard_append(b(m))

r.destroy()
