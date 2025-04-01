from pydantic import BaseModel, ConfigDict, EmailStr, Field
from enum import Enum

class TypeChurch(str, Enum):
    area = 'area'
    congregacao = 'congregacao'

class RoleUser(str, Enum):
    Superadmin = 'Superadmin'
    Professor = 'Professor'
    Admin = 'Admin'
    Aluno = 'Aluno'
class ChurchSchema(BaseModel):
    nome: str
    numero_area: str 
    endereco:  str
    pastor: str
    superintendente: str
    tipo: TypeChurch

class ChurchPublic(BaseModel):
    nome: str
    numero_area: str = Field(alias="numeroDaArea") 
    endereco:  str
    pastor: str
    superintendente: str
    tipo: TypeChurch
    model_config = ConfigDict(from_attributes=True)

class ChurchList(BaseModel):
    churchs: list[ChurchPublic]

class UserSchema(BaseModel):
    nome: str 
    telefone: str 
    email: EmailStr
    senha: str
    roleTipo: RoleUser
class UserPublic(BaseModel):
    nome: str 
    telefone: str 
    email: EmailStr
    roleTipo: RoleUser

class Token(BaseModel):
    access_token: str
    token_type: str