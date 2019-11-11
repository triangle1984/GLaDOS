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

    def dowloadfile(self, url):
        name = f"photo{time.time()}.png"
        gif = False
        with open(name, "wb") as files:
            response = requests.get(url).content
            files.write(response)
        if url[-3:] == "gif":
            gif = True
        return (gif, name)

    def dowloadupload(self, url):
        try:
            files = self.dowloadfile(url)
            if files[0] == False:
                response = self.uploadphoto(files[1])
            else:
                response = self.uploaddoc(files[1], self.peer_id)
        finally:
            os.remove(files[1])
        return response

    def multithreadwoload(self, url):
        pool = ThreadPoolExecutor(6)
        futures = []
        photos = []
        for url in url:
            futures.append(pool.submit(self.dowloadupload, url))
        for x in as_completed(futures):
            photos.append(x.result())
        return ",".join(photos)
