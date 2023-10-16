from fastapi import APIRouter

comment_router = APIRouter(prefix='/comments', tags=['Kommentarriy k publikatsiyam'])

from comments import comments_api