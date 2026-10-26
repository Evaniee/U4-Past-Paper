COMMISSION_RATE = 500
COMMISSION_BONUS = 0.15

class Employee:

    def __init__(self, name: str, id_number: int, properties_sold: int):
        """Represents an employee

        Args:
            name (str): Name of the employee
            id_number (int): ID number of the employee
            properties_sold (int): Number of properties the employee has sold this week
        """
        self.name: str = name
        self.id_number: int = id_number
        self.properties_sold: int = properties_sold

    def get_sales_commission(self, apply_bonus: bool) -> int:
        """Get the sales commission owed to the employee

        Args:
            apply_bonus (bool): Should the commision bonus be applied?
        Returns:
            int: Sales commission owed to employee
        """
        commission = self.properties_sold * COMMISSION_RATE
        if apply_bonus:
            commission += self.get_bonus_commission()
        return commission

    def get_bonus_commission(self) -> int:
        """Get the bonus sales commission owed to the employee

        Returns:
            int: The bonus sales commission owed to the employee
        """
        return self.get_sales_commission(apply_bonus = False) * COMMISSION_BONUS

    def __str__(self):
        return f"{self.name} ({self.id_number}) has sold {self.properties_sold} properties."

def get_int(prompt: str, min: int | None = None, max: int | None = None) -> int:
    """Get an integer between two optional boundaries

    Args:
        prompt (str): Prompt to ask user for input
        min (int | None, optional): Minimum accepted value (inclusive). Defaults to None.
        max (int | None, optional): Maximum accepted value (inclusive). Defaults to None.

    Raises:
        ValueError: Raised if minimum is above maximum

    Returns:
        int: An integer between two optional boundaries
    """
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

def get_str(prompt: str) -> str:
    """Get a non-empty string
    Args:
        prompt (str): Prompt to ask user for input

    Returns:
        str: A non-empty string
    """
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

    # Get every employee's info into a list, sorted in descending order by number of properties sold
    number_of_employees = get_int('How many employees are working this week: ', min=2, max=5)
    employees = []
    for i in range(0, number_of_employees, 1):
        name = get_str(f"Enter employee {i + 1}'s name: ")
        id_number = get_int(f"Enter employee {i + 1}'s id number: ", min=1, max=None)
        properties_sold = get_int(f"Enter how many properties employee {i + 1} has sold this week: ", min=0, max=None)
        employees.append(Employee(name, id_number, properties_sold))
    employees = sorted(employees, key=lambda employee: employee.properties_sold, reverse=True)

    # Display every employee's information
    for i in range(0, number_of_employees, 1):
        commission = employees[i].get_sales_commission(apply_bonus = (i == 0))
        print(employees[i], end='')
        print(f' Comission owed: £{commission:.2f}.')
        total_commission += commission
        total_propeties_sold += employees[i].properties_sold

    # Display totals
    print(f'Total sales commission: £{total_commission:.2f}')
    print(f'Total properties sold this week: {total_propeties_sold}')
    
    # Congratulate best employee
    print(f'Congratulations to {employees[0].name} ({employees[0].id_number}) who sold {employees[0].properties_sold} properties this week, and earned a bonus of £{employees[0].get_bonus_commission():.2f} on top of their £{employees[0].get_sales_commission(False):.2f} commision for a total of £{employees[0].get_sales_commission(True):.2f}')