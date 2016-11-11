light_speed = 2.99792458 * 10^10
B = 89740.46 * 10^6 / light_speed / 2
plank = 6.62607004 * 10^(-34)
mu = 6 *  19/ (19 + 6) * 1.660539040 * 10^(-27)
l = sqrt(plank / (8 * pi^2 * light_speed * mu * B))

mu1 = 6 * 19 / (19 + 6) * 1.660539040 * 10^(-27)
mu2 = 7 *  19/ (19 + 7) * 1.660539040 * 10^(-27)
B1 = plank / (8 * pi^2 * light_speed * mu1 * l^2) * light_speed * 2 / 10^6
B2 = plank / (8 * pi^2 * light_speed * mu2 * l^2) * light_speed * 2 / 10^6

18702.04 - 18617.98 = 84.06
Be = (18702.04 + 84.06) *  2.99793 * 10^(-4)
mu = 137.905 * 15.994 / (137.905 + 15.994) * 1.660539040 * 10^(-27)
l = sqrt(plank / (8 * pi * light_speed * mu * Be)) * 10^10

(10*20023.21 - 200198.22) / 990
(20 * 10011.62 - 1000 * 0.0342 - 200029.16) / (2 * 10 * 64)

I = (12 * 0.7^2 + 14 * 1.85^2 + 12 * 0.7^2 + 12 * 1.9^2 + 9) * 1.660539040 * 10^(-27) * 10^-20
B3 =  plank / (8 * pi^2 * light_speed * I) * light_speed  / 10^6

calculate_rotational_constant <- function(I) {
  B = plank / (8 * pi^2 * light_speed * I) * light_speed  / 10^6
  print(B)
  return(B)
}

# CO2
I4 = 16 * 1.2^2 * 2 * 1.660539040 * 10^(-27) * 10^(-20) 
B4 = calculate_rotational_constant(I4) # 10.967 GHz

# CS2
I5 = 32 * 1.6^2 * 2 * 1.660539040 * 10^(-27) * 10^(-20)
B5 = calculate_rotational_constant(I5) # 3.085 GHz

# CSO
I6 = (32 * 1.6^2 + 16 * 1.2^2) * 1.660539040 * 10^(-27) * 10^(-20)
B6 = calculate_rotational_constant(I6) # 4.815 GHz

(- 16 * 2 * 1.202 * cos(130.6/360*pi) + 35 * 1.84) / (35 + 16 + 16 + 14)
Iaa = (35 * 1.243^2 + 14 * 0.597^2 + 16 * 1.092^2 * 2) * 1.660539040 * 10^(-27) * 10^(-20)
Ibb = (16 * 1.092^2 * 2) * 1.660539040 * 10^(-27) * 10^(-20)
Icc = Iaa + Ibb

A = calculate_rotational_constant(Iaa)
B = calculate_rotational_constant(Ibb)
C = calculate_rotational_constant(Icc)

com = (12 * 1.2 + 2.8 * 32) / (12 + 32 + 16)
I = (12 * (com - 1.2)^2 + 16 * com^2 + 32 * (2.8 - com)^2) * 1.660539040 * 10^(-27) * 10^(-20)
calculate_rotational_constant(I)
