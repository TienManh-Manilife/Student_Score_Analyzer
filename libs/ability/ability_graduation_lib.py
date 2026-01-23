from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.regression.regression_lib import get_R2, get_a_b_of_linear_regression, get_rmse

# Trả về dự đoán nhờ hồi quy
def predict_of_score_through_linear_regression(mssv, time):
    a, b = get_a_b_of_linear_regression(mssv)
    return a*time + b

# Dự đoán khoảng điểm
def predict_period_of_score_to_write(mssv):
    hs_score = 1
    hs_time = 0.9
    arr = get_arr_all_time_of_a_student(mssv)
    thesis_time = np.mean(arr) + hs_time*np.std(arr) # Làm khóa luận sẽ có nhiều thời gian hơn so trung bình
    predict_score = predict_of_score_through_linear_regression(mssv, thesis_time)
    low_score = predict_score - hs_score*get_rmse(mssv)
    high_score = predict_score + hs_score*get_rmse(mssv)
    return round(low_score, 2), round(high_score, 2)

def get_range(a, b):
    arr = [4, 5, 5.5, 6.5, 7, 8, 8.5, 9]
    ans_arr = [a] + [x for x in arr if a < x < b] + [b]
    percent = [round((ans_arr[i+1] - ans_arr[i]) * 100 / (b - a), 2) for i in range(len(ans_arr)-1)]
    return ans_arr, percent


def get_evaluation_to_write(mssv):
    low, high = predict_period_of_score_to_write(mssv)
    output = f"Dự đoán khả năng làm khóa luận / đồ án của sinh viên {get_name_student(mssv)} {mssv}\n"
    output += f"Khoảng điểm dự đoán: {low} - {high}\n"
    ans_arr, percent = get_range(low, high)
    for p in percent:
        output += f"Tỉ lệ đạt {change_score_to_word(ans_arr[percent.index(p)])}: {p}\n"
    return output