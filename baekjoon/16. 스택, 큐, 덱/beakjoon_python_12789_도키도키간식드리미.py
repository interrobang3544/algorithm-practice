n = int(input())
waitingQueue = list(map(int, input().split()))
waitingStack = []
turn = 1

while waitingQueue:
    if waitingQueue[0] == turn:
        waitingQueue.pop(0)
        turn += 1
    else:
        waitingStack.append(waitingQueue.pop(0))

    while waitingStack:
        if waitingStack[-1] == turn:
            waitingStack.pop()
            turn += 1
        else:
            break

if len(waitingStack) == 0:
    print("Nice")
else:
    print("Sad")
