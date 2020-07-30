import os
import sys
import requests

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

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
