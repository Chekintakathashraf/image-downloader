import os
import requests
import uuid
import threading

class ImageDownloaderByURL(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            print(f"Thread name: {threading.current_thread().name} - ID: {threading.get_ident()}")
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()  
            
            
            image_name = f"images/{str(uuid.uuid4())}.jpg"
            with open(image_name, "wb") as image_file:
                image_file.write(response.content)
                print(f"Image downloaded: {image_name}")
        except Exception as e:
            print(f"Failed to download {self.url}: {e}")
