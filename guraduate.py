import numpy as np #���l�v�Z���C�u����
import pandas as pd #�f�[�^��̓��C�u����
#�O���t�`��
#%matplotlib inline
from matplotlib import pylab as plt
#�O���t�����ɂ���
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=15,6
#�f�[�^�ǂݍ���
filepath='ScoreData.csv'
data=pd.read_csv(filepath)
data.head()#�s���ׂĂ�Ԃ�(�����̐����̐������s��Ԃ����Ƃ���)
print(data.head())