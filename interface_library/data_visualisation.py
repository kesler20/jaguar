import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.sparse import data
from sklearn import linear_model
from matplotlib import colors, pyplot as plt
from matplotlib import cm
data2 = pd.read_excel(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython\Lab 2 Results.xlsx')
print(data2)
data1 = [0.762371,0.765725,0.765725,0.7601490]
data = [data1.append(0) for i in range(11 - 3)]
data = pd.DataFrame(data1) + 2
'''
3D SCATTER PLOT
    plt.scatter(data2['Compression Force'], data2['Tensile Strength'])
    plt.show()

    X = data2['Compression Force']
    Y = data2['Tablet Mass']
    Z = data2['Tensile Strength']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X,Y,Z,'r')
    plt.show()
'''
def CURVATURE_GRAPH():
    X = []
    for value in range(1,len(data2['Turret Speed'])):
        x = [data2['Compression Force'][value],data2['Tablet Mass'][value]]
        X.append(x)
    print(X)
    Y = data2['Turret Speed']
    print(Y)

    import pandas as pd
    df1=pd.DataFrame(X,columns=['Price','AdSpends'])
    df1['Sales']=pd.Series(Y)
    df1 = df1.fillna(df1['Sales'].mean())
    df1 = df1.fillna(0)
    print(df1)

    ## Apply multiple Linear Regression
    import matplotlib.pyplot as plt
    import statsmodels.formula.api as smf
    model = smf.ols(formula='Sales ~ Price + AdSpends', data=df1)
    results_formula = model.fit()
    results_formula.params



    ## Prepare the data for Visualization

    x_surf, y_surf = np.meshgrid(np.linspace(df1.Price.min(), df1.Price.max(), len(df1)),np.linspace(df1.AdSpends.min(), df1.AdSpends.max(), len(df1)))
    onlyX = pd.DataFrame({'Price': x_surf.ravel(), 'AdSpends': y_surf.ravel()})
    fittedY=results_formula.predict(exog=onlyX)



    ## convert the predicted result in an array
    fittedY=np.array(fittedY)

    # Visualize the Data for Multiple Linear Regression
    X = []
    for value in range(1,len(data2['Turret Speed'])):
        x = [data2['Compression Force'][value],data2['Tablet Mass'][value]]
        X.append(x)
    print(X)
    Y = -data2['Turret Speed'] + 96
    print(Y)

    import pandas as pd
    df2=pd.DataFrame(X,columns=['Price1','AdSpends1'])
    df2['Sales']=pd.Series(Y)
    df2 = df2.fillna(df2['Sales'].mean())
    df2 = df2.fillna(2.099186)
    print(df2)

    ## Apply multiple Linear Regression
    import matplotlib.pyplot as plt
    import statsmodels.formula.api as smf
    model = smf.ols(formula='Sales ~ Price1 + AdSpends1', data=df2)
    results_formula = model.fit()
    results_formula.params



    ## Prepare the data for Visualization

    x_surf1, y_surf1 = np.meshgrid(np.linspace(df2.Price1.min(), df2.Price1.max(), len(df2)),np.linspace(df2.AdSpends1.min(), df2.AdSpends1.max(), len(df2)))
    onlyX = pd.DataFrame({'Price1': x_surf.ravel(), 'AdSpends1': y_surf.ravel()})
    fittedY1=results_formula.predict(exog=onlyX)



    ## convert the predicted result in an array
    fittedY1=np.array(fittedY1)

    # Visualize the Data for Multiple Linear Regression

    fig = plt.figure(figsize = [12,8])
    ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(df2['Price1'],df2['AdSpends1'],df2['Sales'],c='green', marker='o', alpha=0.5)
    #ax.scatter(df1['Price'],df1['AdSpends'],df1['Sales'],c='red', marker='o', alpha=0.5)
    ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='b', alpha=0.3)
    ax.plot_surface(x_surf1,y_surf1,fittedY1.reshape(x_surf1.shape), color='b', alpha=0.3)
    ax.set_xlabel('Compression Force')
    ax.set_ylabel('Tablet Mass')
    ax.set_zlabel('Turret Speed')
    plt.show()

def REGRESSION_GRAPH():
    #initialize the response space 
    f = lambda x, y: 1.667 + 0.00107843*x -0.00247436*y -0.00547222
    x0 = np.linspace(0, len(data2['Compression Force']))
    y0 = np.linspace(0, len(data2['Tablet Mass']))
    X1, Y1 = np.meshgrid(x0,y0)
    F = f(X1,Y1)

    Z1 = np.array(data2['Compression Force']/2)
    z2 = np.array(data[0])
    z3 = np.array(data2['Turret Speed']/2)

    y1 = []
    x1 = [y1.append(i) for i in range(12)]
    x1 = np.array(y1)
    y1 = x1

    fig = plt.figure(figsize = [12,8])
    ax = fig.add_subplot(111, projection='3d')
    #ax.plot_surface(X1, Y1, G/2)
    ax.plot_surface(X1, Y1, F/2, cmap=cm.coolwarm)
    plt.scatter(Z1,z3,z2,c='black', marker='o', alpha=0.9)
    ax.set_xlabel('Compression Force')
    ax.set_ylabel('Tablet Mass')
    ax.set_zlabel('Tensile Strength')
    plt.show()

def BOX_PLOT():
    import matplotlib.pyplot as plt
    import numpy as np
    
    data = []
    for r in range(1,len(data2)):
        data.append([data2['Compression Force'][r], data2['Tensile Strength'][r]])
    
    
    fig = plt.figure(figsize =(10, 7))
    
    # Creating axes instance
    ax = fig.add_axes([0, 0, 1, 1])
    ax.boxplot(data)
    plt.axhline(data2['Tensile Strength'].mean(), color='black')
    # show plot
    plt.show()

def MODEL_ACCURACY():
    model = linear_model.LinearRegression()
    regression = model.fit(data2[['Compression Force','Tablet Mass', 'Turret Speed']], data2['Tensile Strength'])
    score = regression.score(data2[['Compression Force','Tablet Mass', 'Turret Speed']], data2['Tensile Strength'])
    print(score)
    print(regression.coef_)
    
    x = np.linspace(data2['Compression Force'].min(),0.005*(data2['Compression Force'].max()))
    y = np.linspace(data2['Tablet Mass'].min(),0.005*(data2['Tablet Mass'].max()))
    z = np.linspace(data2['Turret Speed'].min(), 0.005*(data2['Turret Speed'].max()))
    w = regression.coef_
    Fx = 1.667 + w[0]*x + w[1]*y + w[2]*z
    operating_range = []
    for i in range(len(Fx)):
        response = Fx[i]
        if response > 1.6 and response < 1.7:
            operating_range.append([x[i], y[i], z[i]])
        else:
            pass
    print(operating_range)
    return operating_range

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
path = ''
features = ''

def animate(i):
    graph_data = pd.read_csv(path)
    X = []
    Y = []
    for value in graph_data[features]:
        X.append(value)
    for _ in range(len(X)):
        Y.append(_)
    plt.plot(X, Y)
    
#insert the two lines at the end of the for loop you want to animate
#the path must corresponds to the right path initializing the attribute real_time_plt.path = r'path'
#ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.show()

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
import seaborn as sb 

def heat_plot(x0=0,x1=1,y0=0,y1=1,m_final=169):
    x = np.linspace(x0,x1)
    y = np.linspace(y0,y1)
    x, y = np.meshgrid(x,y)
    m = 1
    f = lambda x,y: (2*(1 - (-1)**m)/(m*np.pi*np.sinh(m*np.pi)))*np.sin(m*np.pi*x)*np.sinh(m*np.pi*y)
    F = f(x,y)
    # check why first response looks a lot better
    # then as you add up series artefacts start showing up
    df = pd.DataFrame(F)
    for m in range(2,m_final):
        f = lambda x,y: (2*(1 - (-1)**m)/(m*np.pi*np.sinh(m*np.pi)))*np.sin(m*np.pi*x)*np.sinh(m*np.pi*y)
        F = f(x,y)
        data = pd.DataFrame(F)
        for i in range(len(df)):
            df[i] += data[i]
        if m == 2:
            print(m)
            F = np.array(df)
            ax = sb.heatmap(F, cmap=cm.hot)
            ax.invert_yaxis()
            ax.plot()
            plt.show()
        elif m == 40:
            print(m)
            F = np.array(df)
            ax = sb.heatmap(F, cmap=cm.hot)
            ax.invert_yaxis()
            ax.plot()
            plt.show()
        elif m == 89:
            print(m)
            F = np.array(df)
            ax = sb.heatmap(F, cmap=cm.hot)
            ax.invert_yaxis()
            ax.plot()
            plt.show()
        elif m == 120:
            print(m)
            F = np.array(df)
            ax = sb.heatmap(F, cmap=cm.hot)
            ax.invert_yaxis()
            ax.plot()
            plt.show()
        elif m == 169:
            print(m)
            F = np.array(df)
            ax = sb.heatmap(F, cmap=cm.hot)
            ax.invert_yaxis()
            ax.plot()
            plt.show()
        else:
            pass

heat_plot()