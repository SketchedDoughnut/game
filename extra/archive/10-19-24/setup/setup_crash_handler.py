'''
This is the crash handler baseplate used throughout SDA.
This is propagated (distributed) to multiple places upon build, when
the propagator is called in the devtools. This makes it so we can have only one
copy that we have to edit, but its edits get applied to every crash handler. Propagation can 
also be done by the FOMX system. 
Its job is to handle crashes, and log them for proper debugging / passing on to others. It doesn't have any
inherent traceback security features, but it is assumed that any error logs would be submited in a secure way.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# builtin modules
import os
import sys
import time

# a class for tools that edit file paths
# this is very helpful, yes yes
class Path_tools:
    def __init__(self) -> None:
        pass

    # this function converts the slashes in paths
    # specifically, it converts / to \\ and \\ to /
    # this depends on the mode inputted (either "/" or "\\")
    def convert_path(self, path: str, mode: str) -> str:
        n_string = ''
        for letter in path:
            if mode == '/':
                if letter == '\\': n_string += '/'
                else: n_string += letter
            elif mode == '\\':
                if letter == '/': n_string += '\\'
                else: n_string += letter
        return n_string

    # this is a function that promotes the path. In order words, 
    # it elevates the path. I am not sure how it works, it just does.
    # It keeps running until the end of the path is everything/
    def promote_path(self, path: str) -> list[list, str]: 
        forward_slash_path = self.convert_path(path, '/')
        path_list = [] 
        carry_over = ''
        new_path = ''
        for letter in forward_slash_path: 
            if letter == '/':
                path_list.append(carry_over)
                carry_over = ''
                continue
            carry_over += letter
        path_list.append(carry_over)
        while path_list[-1] != 'everything':
            path_list.pop()
        for folder in path_list: 
            new_path += folder
            new_path += '/'
        new_path.removesuffix('/')
        return [path_list, new_path]

        









# this is the main crash handler. IT is designed to be completely self-sufficient
# This means that it is not dependent on any files (besides builtin modules), which makes it
# more redundant and work better.
class Crash_handler:
    def __init__(self, wDir: str = 'will autofill', error: str = 'error', mode: str = 'run'):

        # establish working directory
        # make an instance of the path tools class
        # transfer the error over into a self variable
        wDir = os.path.dirname(os.path.abspath(__file__))
        self.error = error
        self.path_tools = Path_tools()

        # if the mode is run, then 
        # get a tiemstamp, get a path to dump the log into
        # this path will be at the very top, in everything/crash/dumps
        # then it dumps the crash log, then exits on user input
        if mode == 'run':
            print('------------------')
            print('Crash Handler setting up...')
            self.current_time = self.get_time()
            print('Acquired time...')
            forward_slash_path = self.path_tools.convert_path(wDir, '/')
            logged_path = self.log_data(forward_slash_path)
            print('Data acquired, dumped...')
            print('------------------')
            print('Crash documented to:', f'{logged_path}')
            print('------------------')
            input('Enter anything to exit: ')
            sys.exit()

    # this function gets the current timestamp
    # it also formats it to make it prettier, then returns
    def get_time(self) -> str: 
        s = (time.ctime(time.time()))
        s = s.replace(':', '-')
        s = s.split()
        for __ in range(2):
            s.pop(0)
        n_string = ''
        for num in s:
            n_string += num
            if s.index(num) != len(s) -1:
                n_string += '_'
        return n_string
    
    # this function is responsible for loggin gdata
    # it promotes the filepath, locates where to log data,
    # then logs the data in a file with a matching timestamp. 
    # it also returns the path once done
    def log_data(self, path: str, do_log: bool = True) -> str:
        everything_path_list = self.path_tools.promote_path(path)
        everything_path = everything_path_list[1]
        log_path = everything_path + 'crash/dumps'
        timed_path = log_path + f'/crash_log_{self.current_time}.log'
        backslash_timed_path = self.path_tools.convert_path(timed_path, '\\')
        if do_log:
            f = open(backslash_timed_path, mode='w')
            f.write(self.error)
            f.close()
        return backslash_timed_path