import numpy as np
import matplotlib.pyplot as plt
import csv

# 1. 创建文件对象
f = open('random_points.csv', 'w', encoding='utf-8', newline='')
# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

r = []#生成两个空列表
b = []
d = np.zeros((100, 2))
print(d)
Mean = 0
STD = 5
for i in range(100):
    x = np.random.uniform(1, 10) #1-10之间抽样随机数
    d[i, 0] = x
    r.append(x)
  #  noise=np.random.normal(Mean,STD)
    y=(3*x+2)+np.random.normal(Mean, STD)
    b.append(y)
    d[i, 1] = y
    plt.plot(x, y, marker='o')
    # 3. 写入csv文件内容
    csv_writer.writerow([d[i, 0], d[i, 1]])
print(r, b)
print(d.size)
print(d.shape)
# 4. 关闭文件
f.close()

# 5. 定义损失函数（基于y = wx + b）
def compute_error_for_line_given_points(b, w, points): # points是一个元组，每个元素都是一个二值列表[x,y],比如([1,134], [2,321]...)
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points)) #len(points)就是点的个数

# 6. 定义单次梯度下降函数
def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((w_current * x) + b_current)) #因为马上还要求和所以先除以N
        w_gradient += -(2/N) * x * (y - ((w_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_w = w_current - (learningRate * w_gradient)
    return [new_b, new_w]

# 7. 循环记录梯度下降函数
def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations): #points点集, starting_b初始值b, starting_m初始值m, learning_rate学习率, num_iterations迭代次数
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]

# 8. 主函数逻辑
def run():
    points = np.genfromtxt("random_points.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0 #initial y_intercept guess
    initial_m = 0 #initial slope guess
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}"
          .format(initial_b, initial_m,
                  compute_error_for_line_given_points(initial_b, initial_m, points)
                  )
          )
    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}"
          .format(num_iterations, b, m,
                  compute_error_for_line_given_points(b, m, points)
                  )
          )
    a_x = 0
    b_x = 10
    a_y = m * a_x + b
    b_y = m * b_x + b
    plt.plot([a_x, b_x], [a_y, b_y])
    plt.show()

if __name__ == "__main__":
    run()

