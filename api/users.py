from typing import Optional, List
from pydantic import BaseModel
import fastapi


router = fastapi.APIRouter()


users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]
    


@router.get("/users", response_model=List[User])
def get_users():
    return users


@router.post("/users")
def create_users(user: User):
    users.append(user)
    return "success"

@router.get('/users/{id}')
def get_user(id: int):
    return users[id]