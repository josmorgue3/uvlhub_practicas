from app.modules.profile.repositories import UserProfileRepository
from core.services.BaseService import BaseService

class UserProfileService(BaseService):
    def __init__(self):
        super().__init__(UserProfileRepository())

    def update_profile(self, user_profile_id, form):
        if form.validate():
            updated_instance = self.update(user_profile_id, **form.data)
            return updated_instance, None
        return None, form.errors

    def get(self, user_id):
        return self.repository.get_by_id(user_id)  # Este método debe estar en el repositorio

    def search_users(self, query):
        # Realiza una búsqueda de usuarios por nombre o apellido
        return self.repository.search_by_name_or_surname(query)
