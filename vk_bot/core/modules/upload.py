import time
import os
import requests
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


class Upload:
    def uploadphoto(self, photo):
        response = self.upload.photo_messages(photos=photo)[0]
        return f"photo{response['owner_id']}_{response['id']}"

    def uploaddoc(self, document, peer_id):
        response = self.upload.document_message(
            doc=document, peer_id=peer_id)['doc']
        return f"doc{response['owner_id']}_{response['id']}"

    def dowloadfile(self, url, name):
        gif = False
        with open(name, "wb") as files:
            response = requests.get(url).content
            files.write(response)
        if url[-3:] == "gif":
            gif = True
        return gif

    def dowloadupload(self, url):
        name = f"photo{time.time()}.png"
        try:
            files = self.dowloadfile(url, name)
            if files == False:
                response = self.uploadphoto(name)
            else:
                response = self.uploaddoc(name, self.peer_id)
        finally:
            os.remove(name)
        return response

    def multithreadwoload(self, url):
        pool = ThreadPoolExecutor(4)
        futures = []
        photos = []
        for url in url:
            futures.append(pool.submit(self.dowloadupload, url))
        for x in as_completed(futures):
            photos.append(x.result())
        return ",".join(photos)
