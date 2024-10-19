'''
This is the elevator baseplate used throughout SDA.
Its job is simple, it merely elevates the current directory up until
the end of the path is everything/.
It uses a modified version of the path tools from the crash handler. Due to this, 
some of the comments are merely commented over to save some time.
Thats all!
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''
# builtin modules
import os

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
                if letter == '\\':
                    n_string += '/'
                else:
                    n_string += letter
            elif mode == '\\':
                if letter == '/':
                    n_string += '\\'
                else:
                    n_string += letter
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

        










class Elevatorr:
    def __init__(self):
        self.raw_wDir = os.path.dirname(os.path.abspath(__file__))
        self.path_tools = Path_tools()
        self.wDir = self.path_tools.convert_path(self.raw_wDir, '/')
        self.elevated_universe = self.elevate_path(self.wDir)
        self.elevated_everything = (self.elevated_universe.removesuffix('/universe')) + '/everything'
        self.elevated = (self.elevated_universe.removesuffix('/universe'))

    def elevate_path(self, path) -> str:
        elevated_list = self.path_tools.promote_path(path)
        elevated: str = elevated_list[1]
        elevated = elevated.removesuffix('/')
        elevated = os.path.dirname(elevated)
        elevated += '/universe'
        return elevated
    
Elevator = Elevatorr()