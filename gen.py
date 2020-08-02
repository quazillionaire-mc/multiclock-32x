def numStr(x, n):
        if x < 10:
            return "0"*(n-1) + str(x)
        if x < 100:
            return "0"*(n-2) + str(x)
        elif x < 1000:
            return "0"*(n-3) + str(x)
        else:
            return str(x)

def main():
    n = 0
    a = 0
    hr0 = 1
    hr1 = 2
    min0 = 0
    min1 = 0
    day = True

    while n < 1440:
        str = '{\n'
        str = str + '\t"parent": "item/clock",\n'
        str = str + '\t"textures": {\n'
        str = str + '\t\t"analog": "item/clock_analog_' + numStr(a, 2) + '",\n'
        str = str + '\t\t"hr0": "item/clock_digit_' + numStr(hr0, 1) + ('d' if day else 'n') + '",\n'
        str = str + '\t\t"hr1": "item/clock_digit_' + numStr(hr1, 1) + ('d' if day else 'n') + '",\n'
        str = str + '\t\t"sep": "item/clock_digit_sep' + ('d' if day else 'n') + '",\n'
        str = str + '\t\t"min0": "item/clock_digit_' + numStr(min0, 1) + ('d' if day else 'n') + '",\n'
        str = str + '\t\t"min1": "item/clock_digit_' + numStr(min1, 1) + ('d' if day else 'n') + '"\n'
        str = str + '\t}\n'
        str = str + '}'

        f = open("assets/minecraft/models/item/clock_" + numStr(n, 4) + ".json","w+")
        f.write(str)
        f.close()

        # print(str(n) + ' ' + str(a) + ' ' + str(hr0) + str(hr1) + ":" + str(min0) + str(min1) + ' ' + ('d' if day else 'n'))

        n = n + 1

        if n % 30 == 0:
            a = a + 1

        if min1 == 9:
            min1 = 0
            if min0 == 5:
                min0 = 0
                if hr1 == 9:
                    hr1 = 0
                    hr0 = hr0 + 1
                else:
                    hr1 = hr1 + 1
                if hr0 == 2 and hr1 == 4:
                    hr0 = 0
                    hr1 = 0
            else:
                min0 = min0 + 1
        else:
            min1 = min1 + 1
        
        if n == 345:
            day = False
        if n == 1065:
            day = True

if __name__ == "__main__":
    main()