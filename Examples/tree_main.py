import os 
import time 
from importlib import reload

import tree 

breaker: bool = True 

mtime_map: dict = {}

def main() -> None:
    with tree.Branch("root", limit=12) as b:
        # print(b.branch)
        
        for i in range(13):
            if b.add_branch(i):
                print(str(i), "branch added")
            else:
                print(str(i), "Unable to added branch")
        
        # for b in b.branches:
        #     print(b)
        # print(b)
        
        print("iterating over b")
        for i in b:
            print(i, end=", ")
        
        # b.add_branch = 2
        # print(b[0])


# while breaker:
#     try:
#         for root, dirs, files in os.walk("."):
            
#             for f in files:
#                 path: str = os.path.join(root, f)
#                 print(mtime_map)
#                 # if path is present id mtime_map,
#                 if path in mtime_map:
#                     # then compare with previous time
#                     # if both time are same
#                     if mtime_map[path] == os.path.getmtime(path):
#                         time.sleep(.5)
#                     else:
#                         # if current time and previous time are different
#                         # then reload the tree module
#                         reload(tree)
#                         main()
#                 else:
#                     # if not present
#                     # then register path: key, mtime: file mtime
#                     print(r'Creating mtime map...')
#                     mtime_map[path] = os.path.getmtime(path)
#     except KeyboardInterrupt:
#         print("Exiting")    
            
            
main()
 