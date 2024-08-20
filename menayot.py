'''
הנושא הוא לחשב לכל יום 
את סך הימים הרצופים ממנו לאחור 
שבהם המחיר היה נמוך או שווה למחיר של אותו יום 
פתרון א' מציע פתרון נאיבי לעבור בשביל כל יום על כל הימים ממנו ולאחור ולחשב את הימים השווים והקטנים
כך זה ייראה
'''

def calculate_consecutive_lower_or_equal_days_naive(prices):
    arr_consecutive_days = [1]*len(prices)
    for i in range(1, len(prices)):
        days = 1
        for j in range(i-1, -1, -1):
            if prices[j] > prices[i]:
                break
            days += 1
        arr_consecutive_days[i] = days
    return arr_consecutive_days


'''
יעילות האלגוריתם הזה היא כמובן לא יעילה במיוחד
סדר הגודל הוא של 
O(n^2)
פתרון אחר מציע להשתמש במחסנית
שתחזיק כל הימים שעדיין לא בא יום שווה או גבוה מהם
והם יישלפו רק כשיבוא אחר גבוה או שווה להם
לצד זאת יהיה במקביל לכל יום את ערך הימים שמצאנו שהוא גדול מהם
כך שכשיבוא גדול ממנו הוא ישתמש בערך שלו ונייתר את הצורך לחפש גם לו
למעשה אפשר להשתמש גם ברשימה בפייתון שתעבוד באותו העקרון של מחסנית
וכך זה ייראה:
'''


def calculate_price_streaks_efficient(prices):

    arr_consecutive_days = [1]*len(prices)  
    stack_list = [0] 
    
    for i in range(1, len(prices)):
        while stack_list and prices[stack_list[-1]] <= prices[i]:
            arr_consecutive_days[i] += arr_consecutive_days[stack_list.pop()]
        stack_list.append(i)
    
    return arr_consecutive_days
