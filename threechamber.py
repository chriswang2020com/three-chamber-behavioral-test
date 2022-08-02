import pandas as pd
import numpy

import matplotlib

def read(path,columns):
    df = pd.read_csv(path)
    lst = df[columns].values
    lst = lst.reshape(-1,6)
    return lst

#predict function
def predict_f(mice):
    social = mice[3]-mice[2]
    novel = mice[-1]-mice[-2]
    if social*novel<0:
        if social > 0:
            return "R"
        else:
            return "L"
    else:
        return "replace"


#diff/sum function
def logp_f(mice,socialside):
    social = mice[3]-mice[2] #right minus left
    novel = mice[-1]-mice[-2] #right minus left
    habituation = (mice[1]-mice[0])/(mice[1]+mice[0])
    if socialside == "L":
        logp_value_social =  -social/(mice[3]+mice[2]) #left minus right
        logp_value_novel  =  novel/(mice[-1]+mice[-2])
    else:
        logp_value_social =    social/(mice[3]+mice[2]) 
        logp_value_novel  =  -novel/(mice[-1]+mice[-2]) #left minus right
    return habituation,logp_value_social, logp_value_novel

#diff function
def diff_f(mice,socialside):
    if socialside == "L":
        social = -(mice[3]-mice[2]) 
        novel = mice[-1]-mice[-2]
    else:
        social = mice[3]-mice[2] 
        novel = -(mice[-1]-mice[-2]) 


def logp(lst,info):
    result = list()
    for i in range(len(lst)):
        result.append(logp_f(lst[i],info[i]))
    return numpy.array(result)

def predict(lst):
    social_side=list()
    for each in lst:
        social_side.append(predict_f(each))
    return social_side

#visualization
def plot(result, chart_title,xticks=[0,1,1]):
    pd.DataFrame(result,columns = xticks).plot.box(title=chart_title,ylim=(-1,1))
