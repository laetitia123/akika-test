from channels.generic.websocket import AsyncWebsocketConsumer
import json


class DashConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # self.groupname = 'dashboard'
        await self.connect()

        # await self.accept()

    async def disconnect(self, close_code):

        await self.disconnect()

    async def receive(self, text_data):

        print('>>>>', text_data)

        pass

    # async def deprocessing(self, event):
    #     valOther = event['value']
    #     await self.send(text_data=json.dumps({'value': valOther}))
