# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:55:41 2019

@author: lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
data = pd.read_csv('international-airline-passengers.csv')
data['time'] = pd.to_datetime(data['time'])
data = data.set_index('time')
# 画出趋势图
def get_picture(data = data):
    data['passengers'].plot()
    plt.figure(figsize=(100,50))
    plt.show()
# 转化序列
def processing(data=data,long=11):
    """
    依次转化为11列
    """
    data['passengers'] = data['passengers'].astype(float)
    sample = len(data) - long + 1
    print('得到{}个样本'.format(sample))
    data_sample = []
    for i in range(sample):
        data_sample.append(data['passengers'][i:i+long])
    data_sample = np.array(data_sample)
    return data_sample

# 训练LSTM网络
def lstm(input_data= None):
    scaler_x = MinMaxScaler()
    scaler_y = MinMaxScaler()
    x = input_data[:,:-1]
    y = input_data[:,-1]
    x = scaler_x.fit_transform(x)
    y = scaler_y.fit_transform(np.reshape(y,(len(y),1)))
    spilt = int(len(y)*0.8)
    x_train = x[:spilt]
    x_test = x[spilt:]
    y_train = y[:spilt]
    y_test = y[spilt:]
    x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
    x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
#    print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
#    print(x_train[0],y_train[0],x_test[0],y_test[0])
 
    model = Sequential()
    model.add(LSTM(50,input_shape=(x_train.shape[1],1),return_sequences=True))
    model.add(LSTM(100))
    model.add(Dense(1,activation='linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    print('Train...')
    model.fit(x_train, y_train,batch_size=8, nb_epoch=300, validation_split=0.1,validation_data=(x_test, y_test))
    predict = model.predict(x_test)
    y_test = scaler_y.inverse_transform(np.reshape(y_test,(len(y_test),1)))
    predict = scaler_y.inverse_transform(predict)
#    print(type(predict))
#    print(predict) 
    plt.plot(predict, 'g:')
    plt.plot(y_test, 'r-')
    plt.show()



    

if __name__ == '__main__':
#    get_picture()  
    sam = processing()
    lstm(sam)