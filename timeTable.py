from random import choice,shuffle

WORK_TIME = [
    "Lecture",
    "Project",
    "Language"
    ]
FREE_TIME = [
    "Game",
    "Serie",
    "Film",
    "Anime",
    "Cartoon",
    "YouTube",
    "Stream",
    "Guitar",
    "Comic",
    "Book"
    ]


def takeFrequencyDict():

    freqs = dict()

    with open("Frequency.txt", "r") as file:
        allLines = file.readlines()
        for line in allLines:
            line = line.split(" ")
            freqs[line[0]] = line[1].rstrip("\n")
    return freqs


def takeContentDict(frequencyList=None):

    content = dict()

    if frequencyList is not None:

        for activity in [*frequencyList]:

            contentsOfThatActivity = []
            try:
                with open(activity + ".txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        contentsOfThatActivity.append(line.rstrip("\n"))
            except FileNotFoundError:
                continue

            content[activity] = contentsOfThatActivity

    return content


def createActivityList(frequencyList=None):
    activityList = []
    if frequencyList is not None:
        for listElement in zip(frequencyList.keys(), frequencyList.values()):
            activity, frequency = listElement
            for i in range(int(frequency)):
                activityList.append(activity)
    return activityList


def setLines(lines=[]):
    newList = []
    lines = lines[::-1]
    while len(lines) != 0:
        line = lines.pop()
        newList.append(line.rstrip("\n"))

    return newList


def isSuitableActivity(activity):
    file = open("log.txt", "a")
    file.close()

    with open("log.txt", "r") as file:
        lines = file.readlines()
        lines = lines[::-1]
        if len(lines) == 0:
            return True

        lines = setLines(lines)

        if (lines[0] in WORK_TIME and activity in WORK_TIME) or (lines[0] in FREE_TIME and activity in FREE_TIME):
            return False
        else:
            threshold = -1
            if len(lines) >= 3:
                threshold = 3
            else:
                threshold = len(lines)

            for i in range(threshold):
                if lines[i] == activity:
                    return False
    return True


def isSuitableContent(content, activity, contentDict):
    lengthOfContents = len(contentDict[activity])

    if lengthOfContents == 1:
        return True

    isLogFull = False

    file = open(activity + "-log.txt", "a")
    file.close()
    lines = []

    with open(activity + "-log.txt", "r") as file:
        lines = file.readlines()
        if len(lines) == lengthOfContents:
            isLogFull = True

    if isLogFull:
        file = open(activity + "-log.txt", "w")
        file.close()
        return True
        
    else:
        lines = lines[::-1]
        lines = setLines(lines)

        treshold = 0

        if len(lines) > 2:
            treshold = 3
        else:
            treshold = len(lines)

        for i in range(treshold):
            if lines[i] == content:
                return False

        return True


def takeAContent(activity, contentDict):
    content = choice(contentDict[activity])

    if isSuitableContent(content, activity, contentDict):
        with open(activity + "-log.txt", "a") as file:
            file.write(content + "\n")
        return content
    else:
        return takeAContent(activity, contentDict)


def takeAnActivity(activityList=None):
    activity = choice(activityList)
    if isSuitableActivity(activity):
        with open("log.txt", "a") as file:
            file.write(activity + "\n")

        return activity
    else:
        return takeAnActivity(activityList)


freqs = takeFrequencyDict()
contentDict = takeContentDict(freqs)
activityList = createActivityList(freqs)
shuffle(activityList)


activity = takeAnActivity(activityList)
content = takeAContent(activity, contentDict)
print(activity + " - " + content)
