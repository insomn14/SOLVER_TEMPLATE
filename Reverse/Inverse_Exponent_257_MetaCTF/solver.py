# step 1
x = '&e"3&Ew*'
y = ['|'] * 24
for c in range(0,8):
    y[c] = (chr(0x98 - ord(x[c])))

print(''.join(y))

# Step 2

# You can find the following values through a system of linear equations starting from the last value going back to the first.
chunk2 = [72, 126, 81, 90, 115, 73, 48, 79]
number2 = y
for z in range(0, len(chunk2)):
    # reverses the encryption
    if (chunk2[z] - 0x1F) > 0x40:
        print('yes2')
        number2[z + 8] = chr(chunk2[z] - 0x1F)
    else:
        if (chunk2[z] + 0x1F) > 0x60:
            print('yes')
            number2[z + 8] = chr(chunk2[z] + 0x1F)
        else:
            number2[z + 8] = chr(chunk2[z])
print(''.join(number2))
# Step 3
x = 0xaace63feba9e1c71ef460e6dbf1b1fbabfd7e2e35401440ac57e93bd9ba41c4fbd5d437b1dfab11fe7a1c6c2035982a71765fc9a7b32ccef695dffb71babe15733f5bb29f76aae5f80fff

# converts to base 257
def toStr(n,base):
   if n < base:
      return [n]
   else:
      return toStr(n//base,base) + [n%base]

z = toStr(x,257)

print(z)

z = z[::-1]

a = 0
for num in range(0, len(z)):
    a += z[num] * (257 ** num)

print(a)
print(z.index(8))

f = [55, 62, 39, 74, 55, 30, 45, 70]  # indices of values
h = []
for item in f:
    h.append(chr(item + 40))
print(''.join(number2)  + ''.join(h))
