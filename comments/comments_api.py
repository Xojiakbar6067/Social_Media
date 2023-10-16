from fastapi import Body

from datetime import datetime

from comments import comment_router
from database.commentservice import get_exact_post_comment_db, add_new_comment_db, delete_exact_comment_db, change_exact_comment_db

#zapros na polucheniya comentariy k postu
@comment_router.get('/post-comment')
async def exact_post_comment(post_id: int):
    result = get_exact_post_comment_db(post_id)

    return {'status': 1, 'message': result}

#zapros na dobavleniya komentariy
@comment_router.post('/add-post-comment')
async def add_post_comment(post_id: int = Body(...), user_id: int = Body(...), comment_tex: str = Body(...)):
    result = add_new_comment_db(post_id=post_id, user_id=user_id, comment_text=comment_tex)

    return {'status': 1, 'message': result}

#zapros na izmeneniya komentarii
@comment_router.put('post-comment')
async def change_post_comment(comment_id: int = Body(...), new_comment_text: str = Body(...)):
    result = change_exact_comment_db(comment_id=comment_id, new_comment_text=new_comment_text)

    if result:
        return {'status': 1, 'message': result}
    else:
        return {'status': 0, 'message': 'komentariy ne nayden'}

#udaleniya opredelennogo komentariya
@comment_router.delete('/post-comment')
async def delete_post_comment(comment_id: int):
    result = delete_exact_comment_db(comment_id)

    return {'status': 1, 'message': result}