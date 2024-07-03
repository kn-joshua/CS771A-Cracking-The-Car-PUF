import numpy as np
import sklearn
from sklearn import linear_model
from scipy.linalg import khatri_rao
import time as tm

#Functions for defining various types of classifiers
def LinearSVCmodel(phiC,y_train):
  my_model = sklearn.svm.LinearSVC(loss='squared_hinge', C=0.01, tol=1e-5,penalty='l2')
  my_model.fit(phiC, y_train)
  w = my_model.coef_[0]
  b = my_model.intercept_[0]
  return w,b

def Logisticmodel(phiC, y_train):
  my_model = sklearn.linear_model.LogisticRegression(C=0.01,tol=1e-5,penalty='l2')
  my_model.fit(phiC, y_train)
  w = my_model.coef_[0]
  b = my_model.intercept_[0]
  return w,b

def Ridgemodel(phiC, y_train ):
  my_model = sklearn.linear_model.RidgeClassifier(alpha=0.5)
  my_model.fit(phiC, y_train)
  w = my_model.coef_[0]
  b = my_model.intercept_[0]
  return w,b


#Function to train the data
def my_fit( X_train, y_train ):

    # X_train has 32 columns containing the challeenge bits
    # y_train contains the responses


    my_model=linear_model.LogisticRegression()
    my_model.fit(my_map(X_train),y_train)
    w=my_model.coef_[0]
    b=my_model.intercept_[0]
    return w,b

#Map function to creat features on which linear models can be used
def my_map( X ):
    feat=np.zeros((X.shape[0],528),dtype='int')
    u=np.hstack((1-2*X,np.ones((X.shape[0],1),dtype='int')))
    for i in range(30,-1,-1):
      u[:,i]=np.multiply(u[:,i],u[:,i+1])
    for p in range(0,X.shape[0]):
      v=u[p,:].reshape(33,1)
      result=np.triu(v*v.T,k=1)
      feat[p]=result[result!=0]
    return feat

#Training is done 5 times and the average accuracy is calculated along with the train time,test time and feature size
Z_trn = np.loadtxt( "train.dat" )
Z_tst = np.loadtxt( "test.dat" )

n_trials = 5

d_size = 0
t_train = 0
t_map = 0
acc = 0


for t in range( n_trials ):
	tic = tm.perf_counter()
	w,b = my_fit( Z_trn[:, :-1], Z_trn[:,-1] )
	toc = tm.perf_counter()
	t_train += toc - tic
	d_size += w.shape[0]

	tic = tm.perf_counter()
	feat = my_map( Z_tst[:, :-1] )
	toc = tm.perf_counter()
	t_map += toc - tic

	scores = np.dot(feat,w) + b
	pred = np.zeros_like( scores )
	pred[scores > 0] = 1
	acc += np.average( Z_tst[ :, -1 ] == pred )


d_size /= n_trials
t_train /= n_trials
t_map /= n_trials
acc /= n_trials

print( d_size, t_train, t_map, 1 - acc ,acc*100)