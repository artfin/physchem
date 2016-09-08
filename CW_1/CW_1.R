a <- 3.592
b <- 0.04267

generate_arrays <- function(Temp) {
  x <- array()
  y <- array()
  
  x[1] <- b + 0.001
  for (i in 2 : 5000) {
    x <- c(x, b + 0.001 * i)
  }
  y <- (0.082 * Temp) / (x - b) - (a / (x * x))
  
  res <- list()
  res[[1]] <- x
  res[[2]] <- y
  return(res)
}

q <- list()
for (i in 1 : 10) {
  q[[i]] <- generate_arrays(230 + i * 15)
}

plot(q[[1]][[1]], q[[1]][[2]], main = "vdW", xlab = "V", ylab = "p", type = "l", xlim = c(0, 3), ylim = c(0, 100))
for (i in 1 : 10) {
  points(q[[i]][[1]], q[[i]][[2]], type = "l", col= i, lwd = 2)
}

find_extremum <- function(x, y) {
  min <- array(0, dim = 1)
  max <- array(0, dim = 1)
  
  for (i in 2 : (length(x) - 1)) {
    if (y[i] > y[i - 1] && y[i] < y[i + 1]) {
      max <- c(max, x[i])
    }
    if (y[i] < y[i - 1] && y[i] < y[i + 1]) {
      min <- c(min, x[i])
    }
  }
  
  min <- min[-1]
  max <- max[-1]
  
  res <- list()
  res[[1]] <- min
  res[[2]] <- max
  return(res)
}

s <- find_extremum(q[[1]][[1]], q[[1]][[2]])

c <- array()
n <- array()

R <- 8.31
for (i in 1 : 100) {
  n[i] <- i
  c[i] <- (1.5 * n[i] * R - 2.5 * R) / (n[i] - 1) 
}
plot(n, c, type = "l")


