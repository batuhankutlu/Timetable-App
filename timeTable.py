from random import choice


def takeFrequencyDict():
    freqs = dict()
    with open("Frequency.txt", "r") as file:
        allLines = file.readlines()
        for line in allLines:
            line = line.split(" ")
            freqs[line[0]] = line[1].rstrip("\n")
    return freqs


def isSuitable(activity, frequency):
    file = open("log.txt", "a")
    file.close()
    counter = 0
    ind = -1
    with open("log.txt", "r") as file:
        lines = file.readlines()
        if len(lines) != 0:
            for obj in zip(lines, range(len(lines))):
                line = obj[0]
                i = obj[1]
                if line.rstrip("\n") == activity:
                    counter += 1
                    ind = i
            if int(frequency) == counter:
                return False
            else:
                if (len(lines) - ind) < 3 and ind != -1:
                    return False
                else:
                    return True
        else:
            return True


def randomActivity(freq=dict()):
    activities = [*freq]
    activity = choice(activities)
    if isSuitable(activity, freq[activity]):
        return activity
    else:
        return randomActivity(freq)


def justDoIt(frequencyDict=dict()):
    activity = randomActivity(frequencyDict)
    with open("log.txt", "a") as file:
        file.write(activity + "\n")

    return activity


freqs = takeFrequencyDict()

try:
    print(justDoIt(freqs))
except RecursionError:
    print("All activities are done!")
