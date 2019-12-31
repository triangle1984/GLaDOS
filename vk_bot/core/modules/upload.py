import time
import os
import requests
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from vk_bot.config import *


class Upload:
    def uploadphoto(self, photo):
        try:
            response = self.upload.photo_messages(photos=photo)[0]
        finally:
            os.remove(photo)
        return f"photo{response['owner_id']}_{response['id']}"

    def uploaddoc(self, document, peer_id):
        try:
            response = self.upload.document_message(
                doc=document, peer_id=peer_id)['doc']
        finally:
            os.remove(document)
        return f"doc{response['owner_id']}_{response['id']}"

    def audiomessage(self, name):
        try:
            audio = self.upload.audio_message(
                name, peer_id=self.peer_id, group_id=group_idd)['audio_message']
        finally:
            os.remove(name)
        return f"audio_message{audio['owner_id']}_{audio['id']}"

    def dowloadfile(self, url, expansion="png"):
        name = f"photo{time.time_ns()}.{expansion}"
        with open(name, "wb") as files:
            response = requests.get(url).content
            files.write(response)
        return {"name": name, "expansion": url[-3:]}

    def dowloadupload(self, url):
        files = self.dowloadfile(url)
        if files['expansion'] == "gif":
            response = self.uploaddoc(files['name'], self.peer_id)
        else:
            response = self.uploadphoto(files['name'])
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
