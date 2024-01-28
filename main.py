from typing import Optional, Annotated, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

from api import users, courses, sections

app = FastAPI(
    title='Fake Student API',
    description='API for managing students and courses',
    version='0.0.1',
    contact={
        'name': 'oyekanmi akande',
        'email': 'oyekanmiakande@gmail.com'
    },
    license_info={
        'name': 'MIT'
    }
)


app.include_router(users.router)
app.include_router(sections.router)
