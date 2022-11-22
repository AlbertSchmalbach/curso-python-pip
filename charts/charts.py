import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [235, 48, 108]

    fig, ax = plt.subplot()
    ax.pie(values, label= labels)
    plt.savefig('pie.png')
    plt.close()