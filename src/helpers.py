from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from models import GroupTypes


class GroupIterator:

    GROUPS_TIME_DELTAS = {
        GroupTypes.HOUR: timedelta(hours=1),
        GroupTypes.DAY: timedelta(days=1),
        GroupTypes.MONTH: relativedelta(months=1)
    }

    def __init__(
            self,
            iso_start_date: str,
            iso_end_date: str,
            group_type: GroupTypes | str
    ) -> None:

        if group_type not in GroupTypes.values():
            raise ValueError('Invalid group_type specified')

        self.start_date = datetime.fromisoformat(iso_start_date)
        self.end_date = datetime.fromisoformat(iso_end_date)
        self.group_type = group_type
        self.current_date = self.start_date

    def __iter__(self):
        return self

    def __next__(self):

        if self.current_date > self.end_date:
            raise StopIteration

        start = self.current_date
        self.current_date += self.GROUPS_TIME_DELTAS[self.group_type]

        if start == self.end_date:
            return start, start
        return start, self.current_date
