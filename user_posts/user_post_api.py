from fastapi import Body

from datetime import datetime

from user_posts import posts_router
from database.postservice import add_new_post_db, delete_post_db, edit_post_text_db, get_exact_post_db, get_all_posts_db, like_post_db, unlike_post_db

#zapros na vivod vsex postov
@posts_router.get('/all-post')
async def all_post_info():
    result = get_all_posts_db()

    return {'status': 1, 'message': result}

#zapros na polucheniya opredelennogo posta
@posts_router.get('/exact-post')
async def exact_post_info(post_id: int):
    result = get_exact_post_db(post_id)

    if result:
        return {'status': 1, 'messge': result}

    else:
        return {'status': 0, 'message': 'polzovatel ne nayden'}

#zapros na udaleniya posta
@posts_router.delete('exact-post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    return {'status': 1, 'message': result}

#zapros na izmeneniya teksta k posta (Body)
@posts_router.put('/change-post-text')
async def change_post_text(post_id: int = Body(...), new_post: str = Body(...)):
    result = edit_post_text_db(post_id=post_id, new_post=new_post)

    return {'status': 1, 'message': result}

#zapros na layk posta
@posts_router.post('/like-post')
async def like_post(post_id: int):
    result = like_post_db(post_id)

    return {'status': 1, 'message': result}

#zapros na udaleniya layka iz posta
@posts_router.put('/unlike-post')
async def unlike_post(post_id: int):
    result = unlike_post_db(post_id)

    return {'status': 1, 'message': result}

#zapros na zagruzku novoga posta (Body)
@posts_router.post('/new-post')
async def new_post(user_id: int = Body(...), post_text: str = Body(), publish_date: datetime = Body(...)):
    result = add_new_post_db(user_id=user_id, post_text=post_text, publish_date=publish_date)

    return {'status': 1, 'message': result}