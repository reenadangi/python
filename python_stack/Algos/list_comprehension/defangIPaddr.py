ip="123.23.11.128"
ip2=''.join([c if c!='.' else '[.]' for c in ip])
print(ip2)
