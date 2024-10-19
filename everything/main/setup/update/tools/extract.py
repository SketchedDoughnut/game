'''
This files job is to extract things from a .zip file
I believe it was written by ChatGPT? I forgor...
Thank you AI if it was, though I try not to use you too much :D
NOTE: As it is from AI, I am not going to mess with the comments, and I will just
leave in the ones that the AI made.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines :D
'''

# importing the zipfile module 
from zipfile import ZipFile 
def extract(zip_path, location):  
    # loading the temp.zip and creating a zip object 
    with ZipFile(zip_path, 'r') as zObject: 
    
        # Extracting all the members of the zip  
        # into a specific location. 
        zObject.extractall( 
            path=location) 