from database.models import PostComment
from database import get_db

#poluchit vse komentarii opredelennogo posta
def get_exact_post_comment_db(post_id):
    db = next(get_db())

    exact_post_comment = db.query(PostComment).filter_by(post_id).all()

    return exact_post_comment

#dobavit komentariy
def add_new_comment_db(post_id, user_id, comment_text, publish_date):
    db = next(get_db())

    new_comment = PostComment(post_id=post_id, user_id=user_id, comment_text=comment_text, publish_date=publish_date)

    db.add(new_comment)
    db.commit()

    return 'comentariy dobavlen'

#izmenit komentariy
def change_exact_comment_db(comment_id, new_comment_text):
    db = next(get_db())

    exact_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        exact_comment.comment_text = new_comment_text
        db.commit()

        return 'tekst v komentariy izmenen'
    return 'komentariy ne nayden'

#udalit komentariy
def delete_exact_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'komentariy uspeshno udalen'
    return 'komentariy ne nayden'