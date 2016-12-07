n <- 1/32
a <- 1.360
b <- 0.3913
(1.360 * n) / (273 * (0.3913 * n + 0.0006428))

p <- array()
pv <- array()
for (i in 1 : 4) {
  p[i] <- 0.25 * i
}
pv[1] <- 0.700292
pv[2] <- 0.700133
pv[3] <- 0.699972
pv[4] <- 0.699810

v <- pv / p
R <- array()
R <- (p + a * n^2 / v^2)*(v - n*b) / (n * 273)

fit <- lm(pv ~ p)
fit$coefficients
