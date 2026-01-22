from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.regression.regression_lib import get_R2, get_a_b_of_linear_regression

def get_percent(mssv):
    return 1 - get_R2(mssv)

def get_period_of_time_to_write(mssv):
    time = get_mean_time_all_HocKy(mssv)
    return round(time*(1-get_percent(mssv)), 2), round(time*(1+get_percent(mssv)), 2)

def predict_of_score_through_linear_regression(mssv, time):
    a, b = get_a_b_of_linear_regression(mssv)
    return round(a*time + b, 2)

def predict_period_of_score_to_write(mssv):
    low_time, high_time = get_period_of_time_to_write(mssv)
    low_score = predict_of_score_through_linear_regression(mssv, low_time)
    high_score = predict_of_score_through_linear_regression(mssv, high_time)
    return low_score, high_score
