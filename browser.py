import os
import sys
import requests

tabs = []
# write your code here
while True:
    text = input()
    dots = [pos for pos, char in enumerate(text) if char == '.']
    if len(dots) > 0:
        end_dot_index = dots[-1]
        filename = text[:end_dot_index]

    args = sys.argv
    directory = args[1]

    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        pass

    if text[:8].lower() != "https://" and text != "exit" and text != "back":
        text = "https://" + text

    if len(dots) == 0 and text != "back" and text != "exit":
        print("This URL contains an error")

    elif text == 'back':
        if len(tabs) > 1:
            tabs.pop()
            print(tabs.pop())
        else:
            print("Error: No websites visited")

    elif text == 'exit':
        break
    else:
        site = requests.get(text)
        print(site.text)
        tabs.append(site.text)
        with open(directory + "/" + filename + ".txt", 'w') as f:
            f.write(str(site.text))
