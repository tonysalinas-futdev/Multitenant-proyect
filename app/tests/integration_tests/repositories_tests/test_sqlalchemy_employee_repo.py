import pytest
from app.infraestructure.repositories.sqlalchemy_employee_repo import SqlAlchemyEmployeeRepo
from app.infraestructure.repositories.sqlalchemy_employee_repo import validate_salaries


def test_validate_salaries_happy_path():
    assert validate_salaries(5.0,10.0)==True
    assert validate_salaries(1.99,2.00)

def test_validate_salaries_failed():
    with pytest.raises(ValueError,match="El valor mínimo no puede ser mayor que el máximo"):
        validate_salaries(4.0,3.0)

    with pytest.raises(ValueError,match="Ese valor no está permitido"):
        validate_salaries("4.0","3.0")

@pytest.mark.asyncio
async def test_get_employees_by_name(save_employees_in_db,get_employee_repo:SqlAlchemyEmployeeRepo):
    """
    En este test vamos a asegurarnos de obtener a los empleados que contengan el nombre Juan en el suyo, solo existen dos así que nos aseguraremos de solo obtener a esos, además también probaremos con un nombre que no existe en la base de datos
    """
    employees_contain_juan=await get_employee_repo.filter_by_name("Juan")
    missing_name=await get_employee_repo.filter_by_name("María")

    assert all("Juan" in empl.employee_name for empl in employees_contain_juan)
    assert len(employees_contain_juan)==2
    assert len(missing_name)==0

@pytest.mark.asyncio
async def test_filter_employees_by_salary(save_employees_in_db,get_employee_repo:SqlAlchemyEmployeeRepo):
    """
    En esta primera parte comprobaremos que efectivamente solo dos empleados cobran más de 1500 y que los obtuvimos correctamente
    """
    salaries_gt_1500=await get_employee_repo.filter_by_salary(min_salary=1500)
    assert len(salaries_gt_1500)==2 #Se esperan dos
    assert any(empl.employee_name=="Juan Carlos Chao Salinas" for empl in salaries_gt_1500)
    assert any(empl.employee_name=="Juan Antonio Gonzalez" for empl in salaries_gt_1500)

    """
    Aquí vamos a comprobar que solo uno tiene un salario entre 1500 y 4000 y que su nombre es el correcto
    """

    salarys_between_1500_and_4000=await get_employee_repo.filter_by_salary(min_salary=1500, max_salary=4000)
    assert len(salarys_between_1500_and_4000)==1 #Espera 1
    assert salarys_between_1500_and_4000[0].employee_name=="Juan Carlos Chao Salinas" #Espera Juan Carlos Chao Salinas

    """
    Por último comprobaremos que no hay nadie con un salario menor a 1500
    """

    salaries_lt_1500=await get_employee_repo.filter_by_salary(max_salary=1500)
    assert len(salaries_lt_1500)==0