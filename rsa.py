def extended_gcd(x,y):

    if y == 0:

        return (x,1,0)

    else:

        (d,a,b) = extended_gcd(y,x%y)

        return (d,b,a-(x//y)*b)

def int2Text(number, size):
    """Convert an integer into a text string"""
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")
	

c = 702983809686207307929080504282035515942764423461887687279629448607545018502670286774422553871331959328092894043210081504815838432896140510335963782292582827771
p = 36659958889316033379863699694708695212044687353964657895037312652619368433204333
q = 34054239919915990986667907747697535324526165678900405646668045371919481669852523
e = 65537
mod = p * q
phi = (p-1)*(q-1)
priv_key = extended_gcd(e, phi)[1] * -1
out = (pow(c,priv_key, mod))
print(hex(out)[2:-1].decode('hex'))
