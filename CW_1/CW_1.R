a <- 3.592
b <- 0.04267

generate_arrays <- function(Temp) {
  x <- array()
  y <- array()
  
  x[1] <- b + 0.001
  for (i in 2 : 10000) {
    x <- c(x, b + 0.001 * i)
  }
  y <- (0.082 * Temp) / (x - b) - (a / (x * x))
  
  res <- list()
  res[[1]] <- x
  res[[2]] <- y
  return(res)
}

q <- list()
for (i in 1 : 4) {
  q[[i]] <- generate_arrays(i * 50)
}

plot(q[[1]][[1]], q[[1]][[2]], main = "vdW", xlab = "V", ylab = "p", type = "l", xlim = c(0, 10), ylim = c(0, 10))
for (i in 1 : 4) {
  points(q[[i]][[1]], q[[i]][[2]], type = "l", col= i, lwd = 2)
}

# x <- b + 0.05
# y <- (8.314 * Temp) / (x - b) - (a / (x * x))
