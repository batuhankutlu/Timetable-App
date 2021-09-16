from sys import stderr
from json import load, dump
from json.decoder import JSONDecodeError
from random import choice, shuffle


class Content():
    def __init__(self, __name="N/A", __frequency=0):
        self.__name = __name
        self.__frequency = __frequency
        self.__point = self.__frequency

    def getName(self):
        return self.__name

    def getPoint(self):
        return self.__point

    def incrementPoint(self):
        self.__point += 1

    def decrementPoint(self):
        if self.__point > 0:
            self.__point -= 1
            
    def destroyPoint(self):
        self.__point = 0


class Activity():
    def __init__(self, __name="N/A", __type="N/A", __frequency=0, __contents=[]):
        self.__name = __name
        self.__type = __type
        self.__frequency = __frequency
        self.__contents = __contents
        self.__point = self.__frequency
        self.__contentWRTPoints = []

    def findAndGetContent(self, __content="N/A"):
        for __contentInObj in self.__contents:
            if __contentInObj.getName() == __content:
                return __contentInObj

    def getFrequency(self):
        return self.__frequency

    def getName(self):
        return self.__name

    def getContentList(self):
        return self.__contents

    def getPoint(self):
        return self.__point

    def incrementPoint(self):
        self.__point += 1

    def decrementPoint(self):
        if self.__point > 0:
            self.__point -= 1

    def destroyPoint(self):
        self.__point = 0

    def getType(self):
        return self.__type

    def setContentsWRTPoints(self, __contentList):
        self.__contentWRTPoints = __contentList

    def getContentsWRTPoints(self):
        return self.__contentWRTPoints


class Log():
    def __init__(self, __activity=Activity(), __content=Content()) -> None:
        self.__activity = __activity
        self.__content = __content

    def getActivity(self):
        return self.__activity

    def getContent(self):
        return self.__content


def __takeLog(__activity, __content, __logList):
    with open("Log.json", "w") as __file:
        __logDict = {"Log": []}
        for __log in __logList:
            __logDict["Log"].append({"Activity": __log.getActivity(
            ).getName(), "Content": __log.getContent().getName()})
        __logDict["Log"].append(
            {"Activity": __activity.getName(), "Content": __content.getName()})

        dump(__logDict, __file)


def __fillActivities():
    __activityList = []
    try:
        __jsonFile = open("Activities.json")
        __data = load(__jsonFile)
        for __item in __data["Activities"]:
            __contentsList = []
            for __content in __item["Contents"]:
                __contentsList.append(
                    Content(__content["Name"], __content["Frequency"]))
            __activityList.append(
                Activity(__item["Name"], __item["Type"], __item["Frequency"], __contentsList))
    except FileNotFoundError:
        stderr("I think, you forgot to write an Activities.json file.\nPlease try to write it and turn back to program")
        exit(-1)

    return __activityList


def __calculateLengthLimit(__activityList):
    sum = 0
    for __activity in __activityList:
        sum += __activity.getFrequency()
    return sum ** 2


def __createLog(__activityList=[]):
    __fil = open("Log.json", "a")
    __fil.close()

    __jsonFile = open("log.json")
    try:
        __data = load(__jsonFile)
    except JSONDecodeError:
        __jsonFile.close()
        __data = {"Log": []}
    __lengthLimit = __calculateLengthLimit(__activityList)
    if len(__data["Log"]) > __lengthLimit:
        __file = open("Log.json", "w")
        __file.close()
        __file.open("Log.json")
        __data2 = {"Log": []}
        __data2["Log"].append(__data["Log"][::-1][0])
        dump(__data2,__file)
        __data = __data2

    __logList = []
    for __item in __data["Log"]:
        for __activity in __activityList:
            if __activity.getName() == __item["Activity"]:
                break
        __content = __activity.findAndGetContent(__item["Content"])

        __logList.append(Log(__activity, __content))

    return __logList


def __getActivityAndLog():
    __activityList = __fillActivities()

    return (__activityList, __createLog(__activityList))


def __createActivityAndContentListWRTPoints(__activityList):
    __newList = []
    for __activity in __activityList:
        __newContentList = []
        for __i in range(__activity.getPoint()):
            __newList.append(__activity)
        for __content in __activity.getContentList():
            for __j in range(__content.getPoint()):
                __newContentList.append(__content)

        __activity.setContentsWRTPoints(__newContentList)
    return __newList


def __calculatePoints(__activityList, __LogList):
    for __activity in __activityList:
        for __log1,ind in zip(__LogList[::-1],range(len(__LogList[::-1]))):
            if __activity.getName() == __log1.getActivity().getName():
                if ind > 5:
                    __activity.incrementPoint()
                elif ind < 3:
                    __activity.destroyPoint()
                else:
                    __activity.decrementPoint()
            else:
                if __activity.getType() == __log1.getActivity().getType():
                    __activity.incrementPoint()
                else:
                    pass


def __chooseAnActivity(__activityList, __logList):
    if len(__logList) != 0:
        __typeOfActivity = __logList[len(__logList)-1].getActivity().getType()
    else:
        __typeOfActivity = ""
    __newActivityList = []
    for __activity in __activityList:
        if __activity.getType() != __typeOfActivity:
            __newActivityList.append(__activity)
    __activity = choice(__newActivityList)

    return __activity


def __chooseAContent(__activity):
    shuffle(__activity.getContentsWRTPoints())
    return choice(__activity.getContentsWRTPoints())


__activityAndLogTuple = __getActivityAndLog()

__activityList = __activityAndLogTuple[0]
__LogList = __activityAndLogTuple[1]

__calculatePoints(__activityList, __LogList)

__activityWRTPoints = __createActivityAndContentListWRTPoints(__activityList)

shuffle(__activityWRTPoints)

__chosenActivity = __chooseAnActivity(__activityWRTPoints, __LogList)
__chosenContent = __chooseAContent(__chosenActivity)
print(__chosenActivity.getName() + "-->" + __chosenContent.getName())
__takeLog(__chosenActivity, __chosenContent, __LogList)
