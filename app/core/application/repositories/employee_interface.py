from app.core.application.repositories.generic_crud_interface import GenericCRUDInterface


class EmployeeRepositoryInterface(GenericCRUDInterface):
    async def filter_by_salary(self,min_salary:float=None, max_salary:float=None):
        pass

    async def filter_by_name(self,employee_name:str):
        pass