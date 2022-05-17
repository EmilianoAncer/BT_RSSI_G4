#kalman gain = p/(r+p)
#estimate uncertianty update p = (1 - k)p(prev)
def KalmanFilter(measurments):
    x = measurments[1]
    r = ((max(measurments) - min(measurments))/2)
    r = r*r
    p = 100
    last_arr = []
    for i in range(len(measurments)):
        k_gain = p/(p + r)
        x = x + k_gain*(measurments[i] - x)
        p = (1 - k_gain)*p
        if i >= (len(measurments) - len(measurments)/10):
            last_arr.append(x)
    return (sum(last_arr) / len(last_arr))
