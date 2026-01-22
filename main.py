from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.ability.ability_graduation_lib import *
from tui.app.analyzer import AnalyzerApp

if __name__ == "__main__":
    # AnalyzerApp().run()
    for mssv in get_all_MSSV():
        a, b = predict_period_of_score_to_write(mssv)
        print(a, b)