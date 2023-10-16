from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from database import Base, engine

from user_posts import posts_router
from profile import profile_router
from registration import registration_router
from post_photo import photo_router
from comments import comment_router

#sozdat bazu dannix
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')
app.mount(path='/gallery', app=StaticFiles(directory='media'))


#registratsiya komponentov
app.include_router(posts_router)
app.include_router(profile_router)
app.include_router(registration_router)
app.include_router(photo_router)
app.include_router(comment_router)