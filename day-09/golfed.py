n=int(input());[print(" "*(n-i-1)+"# "*(i+1)) for i in range(n*2)if i<n]+[print(" "*(n-i-1)+"# "*(i+1)) for i in range(n-2,-1,-1)]
