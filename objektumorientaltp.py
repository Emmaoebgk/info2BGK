


def pin_code_generator(n=4):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pins = []


    for char0 in chars:
        for char1 in chars:
            for char2 in chars:
                for char3 in chars:
                    pins.append(char0 + char1 + char2 + char3)
    return pins

if __name__ == '__main__':
    pincodes = pin_code_generator()
    print(pincodes)