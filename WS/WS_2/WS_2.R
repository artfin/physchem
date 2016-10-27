# benzene
# Хроматон N-aw + 15% carbowax 1500

g <- 2.595 # gr
t_dead <- 0.33
Temp <- c(323, 328, 333, 338, 343)
Flux <- 20 # ml/min
T_room <- 294

times <- list()
times[[1]] <- c(1.82, 1.82, 1.82)
sd(times[[1]]) / mean(times[[1]])*100  # 0%

times[[2]] <- c(1.56, 1.55, 1.56)
sd(times[[2]]) / mean(times[[2]]) * 100 # 0.37%

times[[3]] <- c(1.35, 1.35, 1.35)
sd(times[[3]]) / mean(times[[3]]) * 100 # 0%

times[[4]] <- c(1.18, 1.18, 1.18)
sd(times[[4]]) / mean(times[[4]]) # 0%

times[[5]] <- c(1.04, 1.04, 1.04)
sd(times[[5]]) / mean(times[[5]]) # 0% 

times_mean <- array()
for (i in 1 : length(times)) {
  times_mean[i] <- mean(times[[i]])
}

vg <- array()
vg <- (times_mean - t_dead) / g * Flux * Temp / T_room

lnvg <- array()
lnvg <- log(vg, base = exp(1))

plot(1/Temp, lnvg, type = "l", col = "darkorchid", lwd = 2, lty = 2)
points(1/Temp, lnvg, col = "coral", pch = 19)
fit <- lm((1/Temp) ~ lnvg)
abline(fit, lwd = 4)

c1 <- as.numeric(fit$coefficients[1])
c2 <- as.numeric(fit$coefficients[2])
