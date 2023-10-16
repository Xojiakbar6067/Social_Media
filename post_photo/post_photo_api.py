from fastapi import UploadFile

from post_photo import photo_router
from database.postservice import upload_post_photo_db

#zapros na zagruzku fotografii k postu
@photo_router.post('/post-photo')
async def post_photo_upload(post_id, photo_path):
    with open(f'/media/{photo_path.filename}', 'wb') as file:
        front_photo = await photo_path.read()
        file.write(front_photo)

        result = upload_post_photo_db(post_id, f'/gallery/{photo_path.filename}')

        return {'status': 1, 'message': result}