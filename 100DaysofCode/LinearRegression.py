import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\gouar\Downloads\Salary_Data.csv")

# loss function

def loss_function(m,b,points):
    total_losses = 0
    for i in range(len(points)):
        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary
        total_losses += (y - (m * x + b)) ** 2
    print(total_losses / float(len(points)))

# gradient descent

def gradient_descent(m_now,b_now,points,L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)
    for i in range(n):

         x = points.iloc[i].YearsExperience
         y = points.iloc[i].Salary

         m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
         b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m,b

m = 0
b = 0
L = 0.0001
epochs = 1000

for i in range(epochs):
    m,b = gradient_descent(m,b,data,L)
    print(m,b)

plt.scatter(data.YearsExperience,data.Salary, color="black")
plt.plot(list(range(0, 10)), [m * x + b for x in range(0, 10)], color="red")
plt.show()
