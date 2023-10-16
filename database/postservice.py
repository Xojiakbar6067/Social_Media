from database import get_db
from database.models import UserPost, PostPhoto

#poluchit vse publikatsii
def get_all_posts_db():
    db = next(get_db())

    all_posts = db.query(UserPost).all()

    return all_posts

#poluchit opredelennuyu publikatsiyu
def get_exact_post_db(post_id):
    db = next(get_db())

    #zapros v bazu dannix na polucheniya opredelennogo posta po ego id
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        return exact_post
    return 'publikatsiya ne nayden'

#dobavit publikatsii
def add_new_post_db(user_id, post_text, publish_date):
    db = next(get_db())

    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=publish_date)

    db.add(new_post)
    db.commit()

    return new_post.post_id

#izmenit tekst publikatsii
def edit_post_text_db(post_id, new_post):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.post_text = new_post
        db.commit()

        return 'tekst k publikatsii izmenen'

    return 'post ne nayden'

#udalit publikatsiyu
def delete_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        db.delete(exact_post)
        db.commit()
        return 'post uspeshno udalen'
    return 'post ne nayden'


#zagruzit fotografiyu k opredelennogo posta
def upload_post_photo_db(post_id, photo_path):
    db = next(get_db())
    new_photo = PostPhoto(post_id=post_id, photo_path=photo_path)

    db.add(new_photo)
    db.commit()

    return 'foto dobavlen k publikatsii'

#dobavit layk k publikatsii
def like_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes += 1
        db.commit()

        return True

    return 'post ne nayden'

#ubrat layk
def unlike_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes -= 1
        db.commit()

        return True

    return 'post ne nayden'