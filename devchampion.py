                                                                                                                                                                                                                                                                                                                                                                                                nombre_d_enfants=[]
âges_des_enfants = [20,7,19,14,10,7,13,6,4,12,1,12,2,4,4,4,15,12,13,6,7,2,9,18,20,2,15,4,18,14,10,11,16,6,2,4,18,12,10,17,3,20,7,20,6,15,2,10,3,6,5,8]
for line in âges_des_enfants:
    if line >=5 and line <= 9:
        nombre_d_enfants.append(line)
print(len(nombre_d_enfants))