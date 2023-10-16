from fastapi import APIRouter

profile_router = APIRouter(prefix='/profile', tags=['Profil polzovatelya'])

from profile import profile_api