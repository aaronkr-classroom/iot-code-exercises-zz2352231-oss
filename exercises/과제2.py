class SayDays:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        self.month_days = [31, 29 if self.is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def days(self):
        """1월 1일 기준으로 몇째 날인지 계산"""
        return sum(self.month_days[:self.month - 1]) + self.day

    def days_left(self):
        """12월 31일 기준으로 남은 일수 계산"""
        total_year_days = 366 if self.is_leap else 365
        return total_year_days - self.days()

    def weekday(self):
        """Zeller의 공식을 이용한 요일 숫자 반환 (0: 토요일, 1: 일요일, ... 6: 금요일)"""
        y = self.year
        m = self.month
        d = self.day

        if m < 3:
            m += 12
            y -= 1
        
        K = y % 100
        J = y // 100
        
        h = (d + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
        return h

    def weekday_name(self):
        """요일 숫자를 한글 이름으로 변환"""
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]

while True:
    try:
        user_input = input("\n날짜를 입력하세요 (예: 2024 12 25, 종료하려면 'q' 입력): ")
        if user_input.lower() == 'q':
            break
            
        y, m, d = map(int, user_input.split())
        
        sd = SayDays(y, m, d)
        
        print(f"[{y}년 {m}월 {d}일 정보]")
        print(f"- 올해의 {sd.days()}번째 날입니다.")
        print(f"- 올해 마지막까지 {sd.days_left()}일 남았습니다.")
        print(f"- 요일 숫자: {sd.weekday()}")
        print(f"- 요일 이름: {sd.weekday_name()}")
        
    except ValueError:
        print("숫자 세 개를 공백으로 구분하여 입력해주세요 ")