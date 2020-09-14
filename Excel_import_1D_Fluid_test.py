import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
# from IPython.display import HTML
import pandas as pd
import os
import xlwings as xw


def all():
  #現在のディレクトリに移動
  os.chdir('C:\Work\Python\Python_fluid_Excel')

  #パラメータファイルのインポート
  df_import_file = pd.read_excel('param.xlsm', index_col=0, header=1)
  df_import_file = df_import_file.drop(df_import_file.index[4:])
  param_ = df_import_file.to_dict()
  param = param_['数値']


  #初期状態の設定(初期条件）
  nx = int(param['nx']) #★
  xmax = param['xmax'] #★
  dx = xmax / (nx-1)
  nt = 40
  c = param['c'] #★
  alpha = param['alpha'] #★
  dt = alpha * (dx/c) 


  x = np.linspace(0,xmax,nx)

  un = []
  u = np.ones(nx)
  u[int(.5 / dx):int(1 / dx + 1)] = 2

  fig = plt.figure(figsize=(8,4))
  ims=[]

  #計算実行
  for n in range(nt): 
      un = u.copy()
      if (nt%1==0):
        im = plt.plot(x,u, "r")
        ims.append(im)
      for i in range(1, nx):
          u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

  plt.grid()
  plt.ylim([-0.1,3])
  plt.xlabel("x")
  plt.ylabel("u(m/s)")   
  anim = animation.ArtistAnimation(fig, ims)
  # rc('animation', html='jshtml')
  #ani.save('anim.mp4', writer="ffmpeg")
  # plt.close()
  # anim
  anim.save('anim.gif', writer='pillow')
  plt.show()