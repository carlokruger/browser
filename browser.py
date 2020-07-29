import os
import sys

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

    args = sys.argv
    direc = args[1]

    if not os.path.exists(direc):
        os.mkdir(direc)
    else:
        pass

    if text == 'exit':
        break

    elif text == 'bloomberg':
        if os.path.isfile(direc + '/bloomberg.txt'):
            with open(direc + "/bloomberg.txt", "r") as bloom:
                print(bloom.read())
        else:
            print("Error: File does not exist")

    elif text == 'nytimes':
        if os.path.isfile(direc + '/nytimes.txt'):
            with open(direc + "/nytimes.txt", "r") as ny:
                print(ny.read())
        else:
            print("Error: File does not exist")

    elif text == 'bloomberg.com':
        print(bloomberg_com)
        tabs.append(bloomberg_com)
        with open(direc + '/bloomberg.txt', 'w') as b:
            b.write(bloomberg_com)

    elif text == 'nytimes.com':
        print(nytimes_com)
        tabs.append(nytimes_com)
        with open(direc + '/nytimes.txt', 'w') as n:
            n.write(nytimes_com)

    elif text == 'back':
        if len(tabs) > 1:
            tabs.pop()
            print(tabs.pop())
        else:
            print("Error: No websites visited")

    elif text != 'bloomberg.com' and text != 'nytimes.com':
        print("Error: URL does not exist")

    elif len(dots) == 0 and text != "back" and text != "exit":
        print("This URL contains an error")

