from fastapi import UploadFile, Body

from profile import profile_router
from database.userservice import get_exact_user_db, get_all_users_db, edit_user_info_db, upload_profile_photo_db, delete_profile_photo_db

#zapros na polucheniya informatsii o polucheniya ob opredelennom polzovatele
@profile_router.get('/exact-user')
async def exact_user_info(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'status': 1, 'messge': result}

    else:
        return {'status': 0, 'message': 'polzovatel ne nayden'}



@profile_router.get('/all_user')
async def all_user_info():
    result = get_all_users_db()

    return {'status': 1, 'message': result}

@profile_router.post('/profile-photo')
async def upload_profile_photo(user_id: int, photo: UploadFile):
    with open(f'media/{photo.filename}', 'wb') as file:
        front_photo = await photo.read()
        file.write(front_photo)

        result = upload_profile_photo_db(user_id, f'/gallery/{photo.filename}')

        return {'status': 1, 'message': result}

#zapros na udaleniya fotografii polzovatela
@profile_router.delete('/profile-photo')
async def delete_profile_photo(user_id: int):
    result = delete_profile_photo_db(user_id)

    return {'status': 1, 'message': result}

@profile_router.put('/edit-user')
async def edit_user(user_id: int = Body(...), new_info: str = Body(...), edit_info: str = Body(...)):
    result = edit_user_info_db(user_id=user_id, edit_info=edit_info, new_info=new_info)

    return {'status': 1, 'message': result}