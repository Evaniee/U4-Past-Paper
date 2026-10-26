COMMISSION_RATE = 500
COMMISSION_BONUS = 0.15

class Employee:

    def __init__(self, name, id_number, properties_sold):
        self.name: str = name
        self.id_number: int = id_number
        self.properties_sold: int = properties_sold

    def get_sales_commission(self, apply_bonus: bool):
        commission = self.properties_sold * COMMISSION_RATE
        if apply_bonus:
            commission += self.get_bonus_commission()
        return commission

    def get_bonus_commission(self):
        return self.get_sales_commission(apply_bonus = False) * COMMISSION_BONUS

    def __str__(self):
        return f"{self.name} ({self.id_number}) has sold {self.properties_sold} properties."

def get_int(prompt: str, min: int | None = None, max: int | None = None):
    if (min is not None and max is not None) and min > max:
        raise ValueError(f'Error: Minimum must be below maximum ({min} > {max})!')
    valid = False
    while not valid:
        try:
            retv = int(input(prompt))
            if (min is not None and max is not None) and (retv < min or retv > max):
                print(f'Error: Input must be between {min} and {max}!')
            elif min is not None and retv < min:
                print(f'Error: Input must be above {min} ({retv} < {max})')
            elif max is not None and retv > max:
                print(f'Error: Input must be below {max} ({retv} > {max})')
            else:
                valid = True
        except TypeError as error:
            print('Error: `Input must be an integer.')
    return retv

def get_str(prompt: str):
    valid = False
    while not valid:
        retv = input(prompt).strip()
        if retv is None or len(retv) == 0:
            print(f'Error: Input cannot be blank')
        else:
            valid = True
    return retv

if __name__ == '__main__':
    total_commission: int = 0
    total_propeties_sold: int = 0

    number_of_employees = get_int('How many employees are working this week: ', min=2, max=5)
    employees = []

    # Get Employee Info
    for i in range(0, number_of_employees, 1):
        name = get_str(f"Enter employee {i + 1}'s name: ")
        id_number = get_int(f"Enter employee {i + 1}'s id number: ", min=1, max=None)
        properties_sold = get_int(f"Enter how many properties employee {i + 1} has sold this week: ", min=0, max=None)
        employees.append(Employee(name, id_number, properties_sold))

    employees = sorted(employees, key=lambda employee: employee.properties_sold, reverse=True)
    for i in range(0, number_of_employees, 1):
        commission = employees[i].get_sales_commission(apply_bonus = (i == 0))
        print(employees[i], end='')
        print(f' Comission owed: £{commission:.2f}.')
        total_commission += commission
        total_propeties_sold += employees[i].properties_sold
    print(f'Total sales commission: £{total_commission:.2f}')
    print(f'Total properties sold this week: {total_propeties_sold}')
    print(f'Congratulations to {employees[0].name} ({employees[0].id_number}) who sold {employees[0].properties_sold} properties this week, and earned a bonus of £{employees[0].get_bonus_commission():.2f} on top of their £{employees[0].get_sales_commission(False):.2f} commision for a total of £{employees[0].get_sales_commission(True):.2f}')