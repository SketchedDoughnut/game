# this file propogates the one template copy of the crash handler to every other crash handler
raw_crash_file_list = [
    r'everything\main\top\container\game_data\src\rhythm\rhythm.py',
    r'everything\main\top\container\game_data\src\flappy\flappy.py',
    r'everything\main\top\container\game_data\src\conways-game\main.py',
    r'everything\main\top\container\index.py'
]

compiled_crash_file_list = [
    r'everything\main\setup\fiesta-modern.py',
    r'everything\main\setup\fiesta.py'
]

crash_source = r'everything\gitignore\dev\crash_handler.py'

f = open(crash_source, 'r')
crash_source_content = f.read()
f.close()
print('Getting contents of source...')

for file in raw_crash_file_list:
    f = open(file, 'w')
    f.write(crash_source_content)
    f.close()
    print('Propogating to raw file:', file)

for file in compiled_crash_file_list:
    f = open(file, 'w')
    f.write(crash_source_content)
    f.close()
    print('Propogating to compiled file:', file)