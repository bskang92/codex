import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm
import numpy as np

"""화려한 3D 피라미드 예제.
기존 단순 선 기반 피라미드 대신 컬러 그라데이션과 투명도를 적용한 3D 모델을 그립니다."""

# 피라미드 높이 (정육면체 한 변 길이와 동일한 스케일)
height = 1.0

# 밑면 정사각형 좌표 (시계방향)
base = np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0]
])

# 꼭짓점 좌표
apex = np.array([0.5, 0.5, height])

# 각 면을 정의 (네 면과 밑면)
faces = [
    [base[0], base[1], apex],
    [base[1], base[2], apex],
    [base[2], base[3], apex],
    [base[3], base[0], apex],
    [base[0], base[1], base[2], base[3]]
]

# 그라데이션 색상 지정
colors = cm.plasma(np.linspace(0.2, 0.9, len(faces)))

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")
poly = Poly3DCollection(faces, facecolors=colors, edgecolors='k', linewidths=1, alpha=0.95)
ax.add_collection3d(poly)

# 보기 각도 및 축 설정
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, height)
ax.axis('off')
ax.view_init(elev=25, azim=30)
plt.tight_layout()
plt.show()
