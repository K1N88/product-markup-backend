from fastapi import APIRouter, HTTPException, Depends

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.user import current_superuser


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
    dependencies=[Depends(current_superuser)],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
    dependencies=[Depends(current_superuser)],
)


@router.delete(
    '/users/{id}',
    tags=['users'],
    deprecated=True,
    dependencies=[Depends(current_superuser)],
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        status_code=405,
        detail="Удаление пользователей запрещено!"
    )
