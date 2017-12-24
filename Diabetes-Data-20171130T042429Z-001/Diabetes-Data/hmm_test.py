import pandas as pd
from hmmlearn.hmm import GaussianHMM
import numpy as np

data = pd.read_csv('person1.csv')
print(data)
dates = np.array(data.iloc[:,-1])[1:0]
code = np.array(data.iloc[:,-3])[1:]

values = np.array(data.iloc[:,1])
print(values)
diff = np.diff(values)
X = np.column_stack([diff, code])

model = GaussianHMM(n_components=4, covariance_type='diag', n_iter=1000)
model.fit(X)
hidden_states = model.predict(X)

print("Transition matrix")
print(model.transmat_)
print()

print("Means and vars of each hidden state")
for i in range(model.n_components):
    print("{0}th hidden state".format(i))
    print("mean = ", model.means_[i])
    print("var = ", np.diag(model.covars_[i]))
    print()


text = diff[0:10]
codex = code[0:10]
print(codex)
spar = np.vstack((text, codex)).T
print(spar)
y_pred = model.predict(spar)

print(y_pred)

