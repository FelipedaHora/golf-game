import math

#calcula a trajetória de uma bola lançada com uma certa potência e ângulo em um determinado instante de tempo.
def ballPath(startx, starty, power, ang, time):
    angle = ang  # ângulo do lançamento
    velx = math.cos(angle) * power  # componente x da velocidade
    vely = math.sin(angle) * power  # componente y da velocidade

    distX = velx * time  # distância percorrida no eixo x
    distY = (vely * time) + ((-9.8 * (time ** 2)) / 2)  # distância percorrida no eixo y, considerando a gravidade

    newx = round(distX + startx)  # nova posição x
    newy = round(starty - distY)  # nova posição y

    return (newx, newy)  # retorna a nova posição da bola


#calcula a velocidade final da bola após um certo tempo, dado o ângulo e a potência inicial.
def findPower(power, angle, time):
    velx = math.cos(angle) * power  # componente x da velocidade inicial
    vely = math.sin(angle) * power  # componente y da velocidade inicial

    vfy = vely + (-9.8 * time)  # componente y da velocidade final
    vf = math.sqrt((vfy**2) + (velx**2))  # magnitude da velocidade final

    return vf  # retorna a velocidade final


#calcula o ângulo da trajetória da bola, dado a potência inicial e o ângulo de lançamento.
def findAngle(power, angle):
    vely = math.sin(angle) * power  # componente y da velocidade
    velx = math.cos(angle) * power  # componente x da velocidade

    ang = math.atan(abs(vely) / abs(velx))  # calcula o ângulo da trajetória usando arcotangente

    return ang  # retorna o ângulo da trajetória


#calcula o tempo máximo que a bola estará no ar, dado a potência inicial e o ângulo de lançamento.
def maxTime(power, angle):
    vely = math.sin(angle) * power  # componente y da velocidade inicial
    time = ((power * -1) - (math.sqrt(power**2))) / -9.8  # calcula o tempo total de voo

    return time / 2  # retorna a metade do tempo total de voo
