from registration import registration_router, RegisterModel, LoginModel
from database.userservice import add_new_user, login_user_db, delete_user_db

#zapros na registratsiyu polzovatelya
@registration_router.post('/register-user')
def register_user(data: RegisterModel):
    #perevod klassa na parametri dlya funksii
    register_data = data.model_dump()
    result = add_new_user(**register_data)

    return {'status': 1, 'message': result}

#zapros na vxod v akkaunt
@registration_router.post('/login')
def login_user(data: LoginModel):
    #perevod klassa na parametri dlya funksii
    login_data = data.model_dump()
    result = login_user_db(**login_data)

    return {'status': 1, 'message': result}

#zapros na udaleniya polzovatelya iz bazi
@registration_router.delete('/delete')
def delete_user(user_id: int):
    result = delete_user_db(user_id)

    return {'status': 1, 'message': result}