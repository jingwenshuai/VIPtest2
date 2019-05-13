#coding=utf-8
#__author__= 'jws'

# with open('C:\D\VIPtest2\day2\data.txt','r+') as f:
#     for line in f.readlines():
#         print(line.strip())

def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i + 1]:
                bubbleList[i], bubblelist[i + 1] = bubblelist[i + 1], bubblelist[i]
        listLength -= 1
    print(bubbleList)


if __name__ == '__main__':
    li = [3, 4, 1, 2, 5, 8, 0]
    bubble(li)