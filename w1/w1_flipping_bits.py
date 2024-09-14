## https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

""" 
1. Input: list of decimal elements
2. Processing: 
    - Decimal to bytes conversion 
    - Bytes to flips 
    - Flipped bytes to integer 
3. Output: decimals 
"""

def flip_bits(element:int):

    # int to bit converstion 
    bits = ""
    while element > 0: bits = str(element % 2) + bits; element = element // 2; 
    for i in range(32-len(bits)): bits = "".join("0")+bits 
    print(bits)
    print(len(bits))

    # flipping 0 -> 1 and 1 -> 0
    flipped_bits = "".join("0" if b=="1" else "1" for b in bits)
    print(flipped_bits) 

    # flipped_bits to int 
    decimal, length = 0, len(flipped_bits)
    for i in range(length): decimal += int(flipped_bits[i]) * (2 ** (length-i-1))

    return decimal

flip_bits(13)
# Output: 4294967282

