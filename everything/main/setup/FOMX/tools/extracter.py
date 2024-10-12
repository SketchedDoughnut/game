'''
This is an extracter for the FOMX system.
Its job is to extract files from a .zip
It was written by ChatGPT, and is not commented since it is already
partly commented, and I think its self explanatory.
--------------------------------------------------------------------------------------------------------------------------------
This files adheres to the commenting guidelines (kinda) :D
'''

# importing the zipfile module 
from zipfile import ZipFile 
def extract(zip_path: str, location: str):  
    # loading the temp.zip and creating a zip object 
    with ZipFile(zip_path, 'r') as zObject: 
    
        # Extracting all the members of the zip  
        # into a specific location. 
        zObject.extractall( 
            path=location) 