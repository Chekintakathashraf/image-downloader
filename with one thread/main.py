import os
import time
import threading
from image_downloader import ImageDownloaderByURL

if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Thread name: {threading.current_thread().name} - ID: {threading.get_ident()}")

    # Ensure the 'images' directory exists
    os.makedirs("images", exist_ok=True)

    urls = [
        "https://images.unsplash.com/photo-1518791841217-8f162f1e1131",
        "https://images.unsplash.com/photo-1523475496153-3df05c3a5da5",
        "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        "https://images.unsplash.com/photo-1513151233558-d860c5398176",
        "https://images.unsplash.com/photo-1532009877282-3340270e0529",
        "https://images.unsplash.com/photo-1524578271613-245ff8fe06b6",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
        "https://images.unsplash.com/photo-1531256379411-cf0c74c912f3"
    ]

    threads = []
    for url in urls:
        thread = ImageDownloaderByURL(url)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    finish = time.perf_counter()
    print(f"\nFinished in {round(finish - start, 2)} seconds")