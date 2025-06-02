import matplotlib.pyplot as plt
import numpy as np

# 피라미드 높이
height = 5

# 각 층의 좌표를 저장
for i in range(height):
    x = [height - i - 1, height + i]        # 좌측, 우측 x좌표
    y = [i, i]                              # y좌표(아래에서 위로)
    plt.plot(x, y, color='black', linewidth=2)

# 삼각형 외곽선
plt.plot([0, height, 2*height], [0, height, 0], color='red', linewidth=2)

plt.axis('off')
plt.gca().set_aspect('equal')
plt.show()