from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.auth.deps import get_current_user
from app.infrastructure.db.deps import get_db
from app.schemas.category import CategoryResponse
from app.usecases.category_usecase import CategoryUsecase


router = APIRouter(tags=["Categories"])
prefix = "/categories"


@router.get(prefix, response_model=list[CategoryResponse])
def get_categories(
    db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    usecase = CategoryUsecase(db)
    return usecase.get_categories(current_user.id)
