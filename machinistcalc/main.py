def calculate_speed(rpm, sfm, d):
    if rpm is None:
        rpm = (sfm * 3.82) / d
    return rpm

def calculate_feed(rpm, fpt, z):
    ipm = rpm * fpt * z
    return ipm

def calculate_sfm(rpm, d):
    sfm = (rpm * d) / 3.82
    return sfm

def calculate_ipt(ipm, rpm, z):
    ipt = (ipm / rpm) / z
    return ipt

def calculate_mrr(ipm, woc, doc):
    mrr = ipm * woc * doc
    return mrr

def calculate_afpt(ipm, d, woc):
    afpt = ipm * ((d / woc) ** 0.5)
    return afpt

def calculate_hp(mrr, mf):
    hp = mrr * mf
    return hp