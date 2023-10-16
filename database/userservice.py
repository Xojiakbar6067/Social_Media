from database.models import User
from database import get_db

#poluchit vsex polzovateley
def get_all_users_db():

    db = next(get_db())

    all_users = db.query(User).all()

    return all_users

#poluchit opredelennogo polzovatelya
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    return False

#dobavit polzovatelya
def add_new_user(name, surname, email, password, city, birthday, reg_date):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return 'takoy polzovatel uje zaregistrirovan'
    else:
        new_user = User(name=name, surname=surname, email=email, password=password, city=city, birthday=birthday, reg_date=reg_date)

        db.add(new_user)
        db.commit()

        return 'polzovatel uspeshno dobavlen'

# proverka parolya
def login_user_db(email, password):
    db = next(get_db())

    user = db.query(User).filter_by(email=email, password=password).first()

    if user:
        return user
    return 'oshibka avtorizatsii'

#izmenit informatsiyu o polzovatele
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)

    if exact_user:
        if edit_info == 'city':
            exact_user.city = new_info

        elif edit_info == 'email':
            exact_user.email = new_info

        elif edit_info == 'password':
            exact_user.password = new_info

        elif edit_info == 'name':
            exact_user.name = new_info

        db.commit()
        return 'dannie uspeshno izmeneni'
    return 'polzovatel ne nayden'

#udalit polzovatelya
def delete_user_db(user_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        db.delete(user)
        db.commit()

        return 'polzovatel uspeshno udalen'
    return 'polzovatel ne nayden'

#dobavit foto profila
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()

        return 'foto profilya dobavlen'
    return 'polzovatel ne nayden'

#udalin foto profilya
def delete_profile_photo_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = None
        db.commit()

        return 'foto profilya udalen'
    return 'polzovatel ne nayden'
