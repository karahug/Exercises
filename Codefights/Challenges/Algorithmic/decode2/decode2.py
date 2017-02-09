l = 'z'+string.ascii_lowercase[:25]
decode2 = lambda m: ''.join([l[(l.find(x)**2)%26] for x in m])