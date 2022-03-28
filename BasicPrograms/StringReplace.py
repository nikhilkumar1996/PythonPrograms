def replace(name):
    """Basic Program 1: To replace a string in a sentence"""
    sentence = "Hello <<Username>> ,How are you ?"
    change = sentence.replace('<<Username>>', name)  # replace string using inbuilt method Replace(old,new,count)
    return change


if __name__ == '__main__':
    userName = input("Enter Username :")
    print(replace(userName))
