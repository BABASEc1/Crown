import os,platform
os.system('git pull')
os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
os.system("clear")
print('\033[1;32m [•] JOIN FB GROUP')
os.system('xdg-open https://facebook.com/groups/240526195427860/')
os.system("clear")
bit = platform.architecture()[0]
if bit == '64bit':
    from Crown import Crown
    Crown()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
