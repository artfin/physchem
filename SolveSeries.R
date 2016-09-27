beta <- 1
delta <- 2
N <- 20

func <- function(x, lim1, lim2, lim3) {
  summ <- 0
  for (m in 1 : lim1) {
    for (n in 1 : lim2) {
      for (p in 1 : lim3) {
        summ <- summ + 1/ ( (2*m + 1)^2 * (2*n + 1)^2 * (2*p + 1)^2 * ( (2*m + 1)^2 + beta^2 * (2*n + 1)^2 + delta^2 *
                (2*p + 1)^2 + x^2 / pi^2 ) )  
      }
    }
  }
  
  res <- 1 - (8/pi)^3 * x^2 * summ
  return(res)
}

x <- seq(-100, 100, 1)
plot(x, func(x, 10, 10, 10), type = "l", col = "darkorchid", lwd = 2)
# points(x, func(x, 10, 10, 10), pch = 19, col = "skyblue")
abline(h = 0, col = "coral", lwd = 2, lty = 2)

generate_points <- function(n, x1, x2) {
  
  points <- list()
  
  for (counter in 1 : n) {
    points[[counter]] <- array(0, dim = 2)
    points[[counter]][1] <- (x2 - x1) / n * counter + x1 
    points[[counter]][2] <- func(points[[counter]][1], N, N, N)
  }  
  
  return(points)
}

iterative_step <- function(y, x1, x2, ndots) {
  
  points <- generate_points(ndots, x1, x2)
  
  x_plot <- array()
  y_plot <- array()
  for (counter in 1 : length(points)) {
    x_plot[counter] <- points[[counter]][1]
    y_plot[counter] <- points[[counter]][2]
  }
  plot(x_plot, y_plot, type = "l", col = "darkorchid", lwd = 2)
  abline(h = y, col = "coral", lwd = 2, lty = 2)
  
  diff <- array()
  for (counter in 1 : length(points)) {
    diff[counter] <- points[[counter]][2] - y
  }
  
  if (min(abs(diff)) > 0) {
    min_counter <- which(diff == min(abs(diff)))     
  } else {
    min_counter <- which(diff == - min(abs(diff)))
  }
  
  arr <- array()
  arr[1] <- min(abs(diff))
  arr[2] <- -min(abs(diff))
  for (counter_1 in 1 : length(arr)) {
    for (counter_2 in 1 : length(diff)) {
      if(diff[counter_2] == arr[counter_1]) {
        min_counter <- counter_2
        break
      }
    }
  }
  
  points(points[[min_counter]][1], points[[min_counter]][2], col = "skyblue", pch = 19)
  
  res <- list()
  res[[1]] <- points[[min_counter]][1]
  res[[2]] <- points[[min_counter]][2]
  return(res)
}

find_solution <- function(y, xlim1, xlim2, precision) {
  res <- array(0)
  
  cat("------------\n")
  cat("Xlim_1: ", xlim1, "\n")
  cat("Xlim_2: ", xlim2, "\n")
  interim <- iterative_step(y, xlim1, xlim2, 1000)
  res[1] <- interim[[1]]
  cat("Stage 1: ", res[1], "\n")
  cat("------------\n")
  
  xlim_1_new <- floor(res[1])
  xlim_2_new <- floor(res[1]) + 1
  
  cat("------------\n")
  cat("Xlim_1: ", xlim_1_new, "\n")
  cat("Xlim_2: ", xlim_2_new, "\n")
  interim <- iterative_step(y, xlim_1_new, xlim_2_new, 1000)
  res[2] <- interim[[1]]
  cat("Stage 2: ", res[2], "\n")
  cat("------------\n")
  
  cycle_counter <- 1  
  while(abs(tail(res, 1) - tail(res, 2)[1]) > precision) {
    cat("------------\n")
    xlim_1_new <- floor(tail(res, 1) * 10^(cycle_counter)) / 10^(cycle_counter)
    xlim_2_new <- xlim_1_new + 10^(- cycle_counter)
    
    cat("Xlim_1_new: ", xlim_1_new, "\n")
    cat("Xlim_2_new: ", xlim_2_new, "\n")
    
    interim <- iterative_step(y, xlim_1_new, xlim_2_new, 1000)
    res[2 + cycle_counter] <- interim[[1]]
    cat("Stage", cycle_counter + 2, ": ", res[2 + cycle_counter], "\n")
    cycle_counter <- cycle_counter + 1
    cat("------------\n")
  }
  
  cat("Func from last res: ", func(res[length(res)], N, N, N), "\n")
}

# x from -0.5 to 1
res <- find_solution(0.37, 1, 100, 0.0001)
