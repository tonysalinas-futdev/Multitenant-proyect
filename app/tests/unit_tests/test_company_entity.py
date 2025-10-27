from app.core.domain.entities.company import Company
from app.core.domain.entities.company import Employee, EmployeeInfo
import pytest
from app.infraestructure.database.models import Status
def test_create_valid_company():
    company=Company(id=1, company_name="Helados SA", contact_email="example@gmail.com",country="Cuba")

    assert company.contact_email=="example@gmail.com"
    assert company.company_name=="Helados SA"

@pytest.mark.parametrize("id, company_name, contact_email, country ",
        ([1,None,"example@gmail.com","Cuba"],
         [2,"Helados SA","@gmail.com","Canadá"]
)
            )
def test_create_invalid_company(id, company_name, contact_email, country):
    """
    Probaremos a crear una empresa primero sin mandar nombre y luego con un email con un formato inválido
    
    """
    with pytest.raises(ValueError):
        Company(id=id, company_name=company_name, contact_email=contact_email, country=country)

def test_add_employee_to_company(return_company):
    
    employee=Employee(1,"Pedro","Buen empleado","pedro@gmail.com","Senior Backend","No se",1,Status.ACTIVE)
    return_company.add_employee_to_company(employee)

    assert len(return_company.employees)==1
    assert return_company.employees[0]==employee

def test_add_employee_to_company_failed(return_company):
    employee=Employee(1,"Pedro García López","Buen empleado","pedro@gmail.com","Senior Backend","No se",1,Status.ACTIVE)
    

    employee2=Employee(1,"Pedro García López","Mal empleado","lopez@gmail.com","Senior Frontend","No tiene",1,Status.ACTIVE)

    employee3=Employee(1,"Gonzalo Garcia Perez","Buen empleado","pedro@gmail.com","Senior DevOps","No tiene",1,Status.ACTIVE)

    return_company.add_employee_to_company(employee)
    
    with pytest.raises(ValueError,match="Ya existe un empleado registrado con ese correo o nombre"):
        return_company.add_employee_to_company(employee2)

    with pytest.raises(ValueError,match="Ya existe un empleado registrado con ese correo o nombre"):
        return_company.add_employee_to_company(employee3)