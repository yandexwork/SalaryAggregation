from models import Salary, Response
from database import MongoDatabase
from helpers import GroupIterator


class SalaryService:

    def __init__(self):
        self.database: MongoDatabase = MongoDatabase()
        self.response: Response = Response()

    async def get_salary_information(
            self, _from: str, to: str, group_type:str
    ) -> Response:

        for group_start_date, group_end_date in GroupIterator(_from, to, group_type):
            group_label, total_value = group_start_date.isoformat(), 0

            salaries = self.database.get_salaries(group_end_date, group_end_date)
            async for salary in salaries:
                salary = Salary(**salary)
                total_value += salary.value

            self.response.add(group_label, total_value)

        return self.response


salary_service = SalaryService()
