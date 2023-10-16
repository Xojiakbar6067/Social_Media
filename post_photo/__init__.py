from fastapi import APIRouter, UploadFile

photo_router = APIRouter(prefix='/photo', tags=['Fotografii polzovatelya'])

#Dobavit foto k publikatsii
# @photo_router.post('/upload-photo')
# async def upload_photo_api(post_id: int, photo_file: UploadFile):
#     #sohroneniya fotografii v lokalnuyu papku
#     new_photo = open('media/image.jpg', 'wb')
#     from_file_read = await photo_file.read()
#     new_photo.write(from_file_read)
#     new_photo.close()
#
#     return {'message': 'foto dobavleno'}


#poluchit primuyu silku na foto
# @photo_router.get('/get-photo')
# async def get_photo_url():
#     pass
from post_photo import post_photo_api