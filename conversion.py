def convert_to_binary(decimal):
    return bin(decimal)[2:].zfill(8)

def find_class(ip):
    first_octet = int(ip.split(".")[0])
    if first_octet < 128:
        return "Class A"
    elif first_octet < 192:
        return "Class B"
    elif first_octet < 224:
        return "Class C"
    elif first_octet < 240:
        return "Class D"
    else:
        return "Class E"

ip = input("Enter an IP address in decimal notation (4 octets separated by '.'): ")

binary = ".".join([convert_to_binary(int(octet)) for octet in ip.split(".")])

print("Binary representation:", binary)
print("Class:", find_class(ip))
