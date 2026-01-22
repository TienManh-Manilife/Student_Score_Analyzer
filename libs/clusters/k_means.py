from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.draw.draw_chart import set_figure
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def set_x_y():
    mssv = get_all_MSSV()
    lophoc = get_all_MLH()
    time = []
    scores = []
    for MSSV in mssv:
        for MLH in lophoc:
            get_time = get_time_of_a_Lophoc_by_MSSV(MLH, MSSV)
            get_score = get_score_a_subject_by_MLH_of_a_student(MSSV, MLH)
            if get_time is not None and get_score is not None:
                time.append(get_time)
                scores.append(get_score)
            else:
                continue
    return np.array(time), np.array(scores)

def k_means_clustering(x, y, clusters=9):
    X = np.column_stack((x, y))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=clusters, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    return labels, centroids


def draw_chart_k_means():
    x, y = set_x_y()
    k = 3
    labels, centroids = k_means_clustering(x, y, clusters=k)
    plt.figure(figsize=(15, 7))
    for cluster_id in range(k):
        mask = labels == cluster_id
        cx, cy = centroids[cluster_id]
        plt.scatter(
            x[mask],
            y[mask],
            label=f"Nhóm {cluster_id + 1}",
            alpha=0.7
        )
    plt.xlabel("Thời gian học (giờ)")
    plt.ylabel("Điểm trung bình từng môn học")
    set_figure(
        plt.gcf(),
        f"Phân cụm điểm trung bình theo thời gian học (k={k})"
    )
    plt.legend(title="Nhóm sinh viên")
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.savefig("./resources/outputimages/draw_chart_k_means.png")
    plt.show()
