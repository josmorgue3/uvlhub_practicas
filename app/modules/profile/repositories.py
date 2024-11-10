from app.modules.profile.models import UserProfile
from core.repositories.BaseRepository import BaseRepository

class UserProfileRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfile)
        
    def get_by_id(self, user_id):
        # Obtiene el perfil por ID de usuario
        return UserProfile.query.get(user_id)

    def search_by_name_or_surname(self, query):
        # Busca por nombre o apellido que contengan el término de búsqueda
        return UserProfile.query.filter(
            (UserProfile.name.ilike(f'%{query}%')) | (UserProfile.surname.ilike(f'%{query}%'))
        ).all()
