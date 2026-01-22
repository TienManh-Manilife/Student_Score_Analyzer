from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.regression.regression_lib import get_R2, get_a_b_of_linear_regression, get_rmse

# Lấy khoảng thời gian để làm
def get_period_of_time_to_write(mssv):
    hs = 0.1
    times = get_arr_all_time_of_a_student(mssv)
    mean_time = np.mean(times)
    std = np.std(times)
    return mean_time - hs*std, 2, mean_time + hs*std, 2

# Trả về dự đoán nhờ hồi quy
def predict_of_score_through_linear_regression(mssv, time):
    a, b = get_a_b_of_linear_regression(mssv)
    return a*time + b

# Dự đoán khoảng điểm
def predict_period_of_score_to_write(mssv):
    hs = 0.5
    mean_time = np.mean(get_arr_all_time_of_a_student(mssv))
    predict_score = predict_of_score_through_linear_regression(mssv, mean_time)
    low_score = predict_score - hs*get_rmse(mssv)
    high_score = predict_score + hs*get_rmse(mssv)
    return round(low_score, 2), round(high_score, 2)