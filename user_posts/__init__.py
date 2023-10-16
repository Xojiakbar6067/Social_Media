from fastapi import APIRouter

posts_router = APIRouter(prefix='/post', tags=['Publikatsii'])

from user_posts import user_post_api