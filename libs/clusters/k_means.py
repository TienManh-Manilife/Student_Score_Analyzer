from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.draw.draw_chart import set_figure
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def set_x_y():
    HocKy = np.array([])
    scores = []
    mssv = get_all_MSSV()
    for hk in range(1, 8):
        for ms in mssv:
            gpa = get_gpa_10(ms, hk)
            scores.append(gpa)
            HocKy = np.append(HocKy, hk)
    return HocKy, np.array(scores)

def k_means_clustering(x, y, clusters=4):
    x = np.column_stack((x, y))
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    kmeans = KMeans(n_clusters=clusters, random_state=42)
    labels = kmeans.fit_predict(x_scaled)
    return labels

def draw_chart_k_means():
    x, y = set_x_y()
    k = 9
    labels = k_means_clustering(x, y, clusters=k)

    plt.figure(figsize=(15, 7))

    for cluster_id in range(k):
        mask = labels == cluster_id
        plt.scatter(
            x[mask],
            y[mask],
            label=f"Cụm {cluster_id}",
            alpha=0.7
        )

    plt.xlabel("Học kỳ")
    plt.ylabel("GPA")
    set_figure(plt.gcf(), f"Phân cụm GPA theo học kỳ (k={k})")
    plt.legend(title="Nhóm sinh viên")
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.savefig("./resources/outputimages/k_means_clustering_gpa_hocky.png")
    plt.show()
