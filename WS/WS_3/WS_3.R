Temperature <- c(1.635, 1.640, 1.645, 1.650, 1.655, 1.660, 1.665, 1.670, 1.090, 1.080,
                 1.080, 1.085, 1.095, 1.110, 1.115, 1.120, 1.130, 1.130, 1.135, 1.140)

time <- seq(1,20,1) * 30

plot(time, Temperature, type = "l", lwd = 2, col = "darkorchid", main = "??????????? ????????",
     xlab = "?????, ?", ylab = "???????????")
points(time, Temperature, pch = 19, col = "darkolivegreen4")

fit1 <- lm(Temperature[1:8] ~ time[1:8])
abline(fit1, lty = 2, lwd = 2, col = "orange")

fit2 <- lm(Temperature[9:20] ~ time[9:20])
abline(fit2, lty = 2, lwd = 2, col = "orange")

fit3 <- lm(Temperature[8:9] ~ time[8:9])
time_middle = (time[8] + time[9]) / 2
time_middle_temp = fit3$coefficients[2] * time_middle  + fit3$coefficients[1]
points(time_middle, time_middle_temp, pch = 19, col = "blue4")
abline(v = time_middle, lty = 2, lwd = 2, col = "coral")

time_middle_temp_up = fit1$coefficients[2] * time_middle + fit1$coefficients[1]
time_middle_temp_down = fit2$coefficients[2] * time_middle + fit2$coefficients[1]
points(time_middle, time_middle_temp_up, pch = 19, col = "blue4")
points(time_middle, time_middle_temp_down, pch = 19, col = "blue4")

delta = time_middle_temp_up - time_middle_temp_down
text(320, 1.38, "0.599 ????????????? \n ??????", col = "black", cex = 0.75)

16.14 / (39 + 35.5) / 4.2 * 1000
2090 * 0.6 / 51.58
