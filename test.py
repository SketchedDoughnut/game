
# try:
#     1 + 'msg'
# except Exception as e:
#     print('show error')
#     print('------------------')
#     print(e.with_traceback())


class Log:
    def __init__(self):
        print('------------------')
        print('Crash logger set up.')
        self.logging('null', '/workspaces/development/everything/full-redo/full-redo.py', 0)

    def split_path(self, path):
        n_string = ''
        n_list = []
        for letter in path:
            if letter != '/' or letter != '\\':
                n_string += letter
                print('appending')
                print(n_string)
            else:
                n_list.append(n_string)
                n_string = ''
        return n_list

    
    def logging(self, Exception: str, wDir: str, step: int):
        print('------------------')
        print('Crash logging invoked, logging data...')

        print(self.split_path(wDir))

        # # imports 
        # import os

        # # promote by step to everything/
        # n_path = wDir
        # for __ in range(step):
        #     n_path = os.path.dirname(n_path)
        #     print(n_path)


obj = Log()