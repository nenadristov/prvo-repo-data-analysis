from database import sesija, Employee, Product, Sale


def insert_employee(sesija, full_name, email, age, position, salary, years_in_company):
    emp1 = Employee(full_name=full_name,
                    email=email,
                    age=age,
                    position=position,
                    salary=salary,
                    years_in_company=years_in_company)    
    sesija.add(emp1)
    sesija.commit()
    print(f"Vraboteniot {full_name} e vnesen")
    return emp1

def insert_product(sesija, name, price):
    prod1 = Product(name=name, price=price)
    sesija.add(prod1)
    sesija.commit()
    print(f"Produktot {name} e dodaden")
    return prod1

def insert_sale(sesija, employee_id, product_id):
    sale1 = Sale(employee_id=employee_id, product_id=product_id)
    sesija.add(sale1)
    sesija.commit()
    print("Prodazbata e zabelezana")
    return sale1

print("Novi promeni vo nov branch")
ime = input("NVesete go vaseto ime: ")
print(f"Zdravo {ime}")





