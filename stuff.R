a <- (27/64) * 8.314^2 * 633.4^2 / (4.52 * 10^6)
b <- 8.314 * 633.4 / (8 * 4.52 * 10^6)

8.314 * 298 * 2 / (10 - 2 * 1.456 * 10^(-1))
4 * 25.88 / 100
510.38 * 10^3 - 1.0352 * 10^5

2 * 8.314 * 298 / 10

p <- array()
for (i in 1 : 4) {
  p[i] <- 0.25 * i * 1.01325
}

pv <- array()
pv[1] <- 0.700292
pv[2] <- 0.700133
pv[3] <- 0.699972
pv[4] <- 0.699810

pv <- pv * 1.01325

v <- array()
for (i in 1 : 4) {
  v[i] <- pv[i] / p[i]
}

n <- 1 / 32
a <- 1.378
b <- 31.83 * 10^(-3)
Temp <- 273

R <- array()
for (i in 1 : 4) {
  R[i] <- (pv[i] + (n^2 * a) / v[i]) * (v[i] - n * b) / (n * Temp * v[i])
}
R <- R * 100
mean(R) # 8.321125
sd(R)   # 0.0009756598

fit <- lm(pv ~ p)
x <- -0.0006428

b * n - a / (n * 8.314 * 273)

R <- (a * n) / (b *n - x) / Temp
###############################################
library(rootSolve)

p_0 <- 3 * 1.01325
a <- 5.536
b <- 30.49 * 10^(-3)

fun <- function(x) {
  res <- 1/3 * p_0 * x^3 + 1/3 * p_0 * b * x^2 - a/2 * x + 3/4 * a * b
  return(res)
}

curve(fun(x), -10, 10)
abline(h = 0, lty = 3)

uni <- uniroot.all(fun, c(-10, 10))

# CO2
a <- 3.592
b <- 0.0426

Temp <- 300
p <- 1
x <- p * b

cubic_fun <- function(y) {
  res <- y^3 - (x + 100 * 8.314 * Temp) * y^2 + a * x * y - a * x^2
  return(res)
}
uni <- uniroot.all(cubic_fun, c(-100, 100))
