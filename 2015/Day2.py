#find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.
#1588178

def main():
    filefeed = open("Day2Input")
    processedrow = filefeed.readline()
    areatobuy = 0
    ribbontobuy = 0
    while processedrow != "":
        measurements = processedrow.split("x")
        minarea = 0
        minperimeter = 0
        for i in range(len(measurements)):
            for j in range(i+1, len(measurements)):
                area = int(measurements[i]) * int(measurements[j])
                areatobuy += 2*area
                perimeter = int(measurements[i])*2+int(measurements[j])*2
                if minarea == 0 or area < minarea:
                    minarea = area

                if minperimeter == 0 or perimeter < minperimeter:
                    minperimeter = perimeter

        ribbontobuy += minperimeter
        ribbontobuy += int(measurements[0]) * int(measurements[1]) * int(measurements[2])

        areatobuy += minarea
        processedrow = filefeed.readline()

    print(f"Area to buy: {areatobuy}")
    print(f"Ribbon to buy: {ribbontobuy}")

main()