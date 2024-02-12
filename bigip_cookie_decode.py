import sys

def decode_data(data_input):
    # Find the index of "rd" and the first and second "o"
    rd_index = data_input.find("rd")
    first_o_index = data_input.find("o", rd_index)
    second_o_index = data_input.find("o", first_o_index + 1)

    if rd_index == -1 or first_o_index == -1 or second_o_index == -1:
        raise ValueError("Invalid data input format.")

    # Extract the first part between "rd" and the first "o"
    first_part = data_input[rd_index + 2: first_o_index]

    # Extract the second part as a hexadecimal value and convert it to an IP address
    hex_value = data_input[first_o_index + 1: second_o_index]
    ip_address = hex_to_ip(hex_value)

    # Extract the third part after the second "o"
    third_part = int(data_input[second_o_index + 1:])

    return first_part, ip_address, third_part


def hex_to_ip(hex_value):
    # Convert hexadecimal to decimal
    decimal_value = int(hex_value, 16)

    # Convert decimal to IP address
    ip_address = '.'.join(str((decimal_value >> (8 * i)) & 0xFF) for i in range(3, -1, -1))

    return ip_address


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <data_input>")
        sys.exit(1)

    data_input = sys.argv[1]

    try:
        first_part, ip_address, third_part = decode_data(data_input)
        print("***F5 BIG-IP Non-Default Route Domains Cookie Decoder***")        
        print("[*] Route Domain:", first_part)
        print("[*] IP Address:", ip_address)
        print("[*] Port:", third_part)
    except ValueError as e:
        print(e)
