class Solution:
    def today(self, date, days):
        month = int(date[:2])
        day = int(date[3:])

        total = day
        for i in range(month - 1):
            total += days[i]

        return total

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        start = max(self.today(arriveAlice, days), self.today(arriveBob, days))
        end = min(self.today(leaveAlice, days), self.today(leaveBob, days))

        if start > end:
            return 0

        return end - start + 1


        