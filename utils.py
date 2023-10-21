from datetime import datetime

def bytes2file(bytes_obj,file_name=None):

    if file_name is None:
        file_name = f'{datetime.now()}.jpg' # naming conventions etc need to be changed.
        
    with open(f"./{file_name}","wb") as write_file:
        bytes_data = bytes_obj.getvalue()
        
        write_file.write(bytes_data)