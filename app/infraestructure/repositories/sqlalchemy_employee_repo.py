from app.infraestructure.repositories.sqlalchemy_generic_crud import SqlAlchemyGenericCrud
from app.core.application.repositories.employee_interface import EmployeeRepositoryInterface

from app.infraestructure.database.models import Employee
from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload
from typing import List

def validate_salaries(min_salary:float,max_salary:float):
    if not isinstance(min_salary, (int,float)) or not isinstance(max_salary,(int,float)):
        raise ValueError("Ese valor no está permitido")
    if min_salary>max_salary:
        raise ValueError("El valor mínimo no puede ser mayor que el máximo")
    
    return True
        
def return_min_salary_query(min_salary:float):
    return select(Employee).where(Employee.salary>min_salary)

def return_max_salary_query(max_salary:float):
    return select(Employee).where(Employee.salary<max_salary)

def return_max_and_min_salary_query(min_salary:float, max_salary:float):
    return   select(Employee).where(
        and_(
                Employee.salary>min_salary,
                
                Employee.salary<max_salary
            ))

class SqlAlchemyEmployeeRepo(EmployeeRepositoryInterface,SqlAlchemyGenericCrud):
    def __init__(self, session):
        super().__init__(session, Employee)

    async def get_by_id(self, object_id:int)->Employee:
        stmt=select(Employee).options(selectinload(Employee.personal_info)).where(Employee.id==object_id)
        result=await self.session.execute(stmt)
        employee=result.scalar_one_or_none()
        return employee
    
    async def filter_by_name(self,employee_name:str)->List[Employee]:
        stmt=select(Employee).where(Employee.employee_name.icontains(employee_name))
        result=await self.session.execute(stmt)
        employees=result.scalars().all()
        return employees
    
    async def filter_by_salary(self, min_salary:float = None, max_salary:float = None)->List[Employee]:
        
        
        if max_salary and min_salary:
            validate_salaries(min_salary,max_salary)
            query=return_max_and_min_salary_query(min_salary,max_salary)
        
        elif max_salary:
            query=return_max_salary_query(max_salary)
        elif min_salary:
            query=return_min_salary_query(min_salary)
        
        result=await self.session.execute(query)

        employees=result.scalars().all()
        return employees

        

        