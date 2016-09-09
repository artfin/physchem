a <- 3.592
b <- 0.04267

generate_arrays <- function(Temp) {
  x <- array()
  y <- array()
  
  x[1] <- b + 0.0001
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
for (i in 1 : 1) {
  q[[i]] <- generate_arrays(245 + i * 15)
}

plot(q[[1]][[1]], q[[1]][[2]], main = "vdW", xlab = "V", ylab = "p", type = "l", xlim = c(0, 3), ylim = c(0, 100))
for (i in 1 : 1) {
  points(q[[i]][[1]], q[[i]][[2]], type = "l", col= i, lwd = 2)
}

spinodal <- array()
spinodal <- a * (q[[1]][[1]] - 2 * b) / (q[[1]][[1]]^3)
points(q[[1]][[1]], spinodal, type = "l", col = 1, lwd = 2)

maxima <- q[[1]][[2]][which(diff(sign(diff(q[[1]][[2]])))==-2) + 1]
minima <- q[[1]][[2]][which(diff(sign(diff(q[[1]][[2]])))==+2) + 1]

abline(h = maxima, col = "red", lwd = 2) 
abline(h = minima, col = "red", lwd = 2) 

med <- (maxima + minima) / 2
abline(h = med, col = "green", lwd = 2)

err <- 0.3
res <- list()
res[[1]] <- c(0, 0)
for (i in 1 : length(q[[1]][[2]])) {
  if (abs(q[[1]][[2]][i] - med) < err) {
    res[[length(res) + 1]] <- c(q[[1]][[1]][i], q[[1]][[2]][i])
  }
}
res[[1]] <- NULL

for (i in 1 : length(res)) {
  if (res[[i]][1] - res[[i]])
}

for (i in 1 : length(res)) {
  points(res[[i]][1], res[[i]][2], col = "blue", lwd = 2)
}


require(MESS)
auc(q[[1]][[1]], q[[1]][[2]], type = 'spline')

######################

x <- seq(-3,3,0.01)
y1 <- dnorm(x,0,1)
y2 <- 0.5*dnorm(x,0,1)
plot(x,y1,type="l",bty="L",xlab="X",ylab="dnorm(X)")
points(x,y2,type="l",col="red")
polygon(c(x,rev(x)),c(y2,rev(y1)),col="skyblue")





















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

