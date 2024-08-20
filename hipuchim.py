'''
הנושא הוא חיפוש היפוכים בין שני משתמשים שמתבקשים לדרג העדפות 
לצורך החישוב נתייחס למערך הבחירות של אחד המשתמשים כבחירת הייחוס 
פתרון א' שהוצע: 
לעבור על כל המערך ולחפש את ההיפוכים על ידי בדיקה לכל איבר כמה איברים קטנים יותר יש לימינו
האלגוריתם יעבור על כל המערך בלולאה בתוך לולאה ויחפש כמה פעמים מתקיים התנאי
 i<j אבל arr[i] > arr[j]
 כלומר למרות שהמיקום קטן ושמאלי יותר הערך גדול יותר 
 והנה מבנה הפונקציה:
'''


def count_inversions_simple(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


'''
כפי שכבר צויין היעילות של פונקציה זו היא סדר גודל של 
O(n^2)
פתרון ב' שהוצע יעיל יותר
הוא מציע לערוך מיון מיזוג
תהליך שמחלק את המערך לחלקים עד שמתקבל חלקים ממויינים על ידי שהם נהיים ערך יחיד
ואחר כך חיבור באופן של מיון 
ולהוסיף מונה שיספור כל פעם שמעבירים ערך מהמערך השמאלי את כל הערכים הימניים שהוא מדלג עליהם
ולמיון מיזוג יש סיבוכיות יעילה בהרבה
סדר גודל של 
O(n log n)
כך זה ייראה
'''


def count_inversions_merge_sort(arr):

    inversions = divide_and_merge_and_count(arr)[1]
    return inversions


def divide_and_merge_and_count(arr):
    if len(arr)<=1:
        return arr, 0
    
    midle = len(arr)//2
    left, inversions_left = divide_and_merge_and_count(arr[:midle])
    right, inversions_right = divide_and_merge_and_count(arr[midle:])

    merged = []
    inversions = 0    
    i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions + inversions_left + inversions_right


'''
למען האמת מאחר וככל הנראה מדובר במערך שיש בו את כל המספרים מ 1 עד המספר הגדול ביותר
אפשר להשתמש בחלק המיון ללא חלק המיזוג כלל
אלא שהמיון יתבצע על כל המספרים שהם גדולים מהחצי לבין כל המספרים שקטנים מהחצי 
ותוך כדי הלולאה נספור את כל ההיפוכים שיש בין אלו שגדולים מהחצי  לבין אלו שקטנים
כך נקבל בכל ריצה את סך ההיפוכים שמתקיים בין הגדולים והקטנים 
ונשמר כאן הערך של סיבוכיות 
O(n log n)
כך זה ייראה: 
'''



def divide_and_count(arr, midle = None):
    
    if len(arr)<=1:
        return 0
    
    if not midle:
        midle = len(arr)//2
    inversions = 0
    big = 0
    left = []
    right = []
    
    for i in range(len(arr)):
        if arr[i] > midle:
            big += 1
            right.append(arr[i])
        else:
            inversions += big
            left.append(arr[i])
    
    
    inversions += divide_and_count(left,  midle - len(arr)//2)
    inversions += divide_and_count(right, midle + len(arr)//2)
   
    return inversions

