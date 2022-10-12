def ReadFileToList(fileName):
    with open(fileName, "r") as file:
        result = file.read()
    return result


def FindCopies(my_list, listItem):
    counter = my_list.count(listItem)
    return counter


def ZipFile(my_list):
    statistics = {}
    for i in my_list:
        copiesNumber = FindCopies(my_list, i)
        statistics[i] = copiesNumber
    return statistics


text = ReadFileToList('C:/Users/ariel/OneDrive/Рабочий стол/homework_5_python/homework/text.txt')
zipText = ZipFile(text)
print(zipText)
print(type(zipText))
