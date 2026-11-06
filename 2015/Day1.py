#part 1 An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
#part 2 find the position of the first character that causes him to enter the basement (floor -1)

def main():
    filefeed = open("Day1Input")
    inputstrn = filefeed.read()
    filefeed.close()
    counterparent(inputstrn)

def counterparent(inputstrn):
    count = 0
    for pos,x in enumerate(inputstrn):
        if x == "(":
            count += 1
        else:
            count -= 1

        if count == -1:
            print(pos)
            return

    print(count)

main()
