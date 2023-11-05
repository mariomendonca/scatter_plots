from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt


def map_target_array(iris_class):
    if iris_class == "Iris-setosa":
        return 0
    elif iris_class == "Iris-virginica":
        return 1
    elif iris_class == "Iris-versicolor":
        return 2


iris = fetch_ucirepo(id=53)

sepal_length = iris.data.features["sepal length"]
sepal_width = iris.data.features["sepal width"]
petal_length = iris.data.features["petal length"]
targets = iris.data.targets["class"]
numbered_targets = list(map(map_target_array, targets))
colors = ["r", "g", "b"]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_title("Iris 3d plot (Sepal length vs Sepal width vs Petal Length)")
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')

ax.scatter(sepal_length, sepal_width, petal_length, s=10, c=[colors[i] for i in numbered_targets])
plt.show()
