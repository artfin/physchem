require(MESS)

a <- 3.592
b <- 0.04267

generate_arrays <- function(Temp) {
  x <- array()
  y <- array()
  
  x[1] <- b + 0.00001
  for (i in 2 : 50000) {
    x <- c(x, b + 0.00001 * i)
  }
  
  for (i in 1 : 10000) {
    x <- c(x, tail(x, 1) + 0.001 * i)
  }
  y <- (0.082 * Temp) / (x - b) - (a / (x * x))
  
  res <- list()
  res[[1]] <- x
  res[[2]] <- y
  return(res)
}

q <- list()
for (i in 1 : 15) {
  q[[i]] <- generate_arrays(235 + i * 5)
  cat("Generated: ", i, "\n")
}

T_critical <- 

# Plotting isothermes
plot(q[[5]][[1]], q[[5]][[2]], main = "vdW", xlab = "V", type = "l", ylab = "p", xlim = c(0, 3), ylim = c(0, 100), lwd = 2)
for (i in 6 : 10) {
  points(q[[i]][[1]], q[[i]][[2]], type = "l", col= i, lwd = 2)
}

# spinodal <- array()
# spinodal <- a * (q[[1]][[1]] - 2 * b) / (q[[1]][[1]]^3)
# points(q[[1]][[1]], spinodal, type = "l", col = 1, lwd = 2)

# maxima <- q[[1]][[2]][which(diff(sign(diff(q[[1]][[2]])))==-2) + 1]
# minima <- q[[1]][[2]][which(diff(sign(diff(q[[1]][[2]])))==+2) + 1]

binoidal_points <- list()
binoidal_points_counter <- 1

for (counter in 1 : 15) {
  maxima <- q[[counter]][[2]][which(diff(sign(diff(q[[counter]][[2]])))==-2) + 1]
  minima <- q[[counter]][[2]][which(diff(sign(diff(q[[counter]][[2]])))==+2) + 1]

  if (length(maxima) != 0 && length(minima) != 0 && minima > 0) {
    for (s in 1 : 3000) {
      # current height
      h <- minima + s * (maxima - minima) / 1000
      
      err <- 0.3
      res <- list()
      res[[1]] <- c(0, 0)
      for (i in 1 : length(q[[counter]][[2]])) {
        if (abs(q[[counter]][[2]][i] - h) < err) {
          res[[length(res) + 1]] <- c(q[[counter]][[1]][i], q[[counter]][[2]][i])
        }
      }
      res[[1]] <- NULL
      
      # deleting all near by dots
      for (i in 1 : (length(res) - 1)) {
        if (abs(res[[i]][1] - res[[i + 1]][1]) < 0.01) {
          res[[i]] <- c(0,0)
        }
      }
      
      # isolating intersection points
      intersection <- list()
      k <- 1
      for (i in 1 : length(res)) {
        if (res[[i]][1] != 0 && res[[i]][2] != 0) {
          intersection[[k]] <- c(res[[i]][1], res[[i]][2])
#          points(intersection[[k]][1], intersection[[k]][2], col = "blue", pch = 20)
          k <- k + 1
        }
      }

      
      # finding out the number of intersection point on x-axis 
      intersection_number <- array()
      for (i in 1 : length(intersection)) {
        intersection_number[i] <- which(intersection[[i]][1] == q[[counter]][[1]])
      }
      
      if (length(intersection_number) > 2) {
        # trimming dots representing left and right humps
        x_trimmed_left <- q[[counter]][[1]][intersection_number[1] : intersection_number[2]]
        y_trimmed_left <- q[[counter]][[2]][intersection_number[1] : intersection_number[2]]
        
        x_trimmed_right <- q[[counter]][[1]][intersection_number[2] : intersection_number[3]]
        y_trimmed_right <- q[[counter]][[2]][intersection_number[2] : intersection_number[3]]
        
        # finding humps' surfaces
        s_under_left <- auc(x_trimmed_left, y_trimmed_left, type = 'spline')
        s_under_right <- auc(x_trimmed_right, y_trimmed_right, type = 'spline')
        
        s_in_left <- q[[counter]][[2]][intersection_number[1]] * (q[[counter]][[1]][intersection_number[2]] - 
                                                                    q[[counter]][[1]][intersection_number[1]]) - s_under_left
        s_in_right <- s_under_right - q[[counter]][[2]][intersection_number[2]] * (q[[counter]][[1]][intersection_number[3]] - 
                                                                                     q[[counter]][[1]][intersection_number[2]])
        
        cat(s, ":  ", s_in_left - s_in_right, "\n")
        if (abs(s_in_left - s_in_right) < 0.05) {
          cat("Found it! \n")
          abline(h = h, col = counter, lwd = 2)
          cat("h: ", h, "\n")
          cat("s1: ", s_in_left, "\n")
          cat("s2: ", s_in_right, "\n")
          
          # filling binoidal-points-list
          binoidal_points[[binoidal_points_counter]] <- c(q[[counter]][[1]][intersection_number[1]], 
                                                          q[[counter]][[2]][intersection_number[1]])
          binoidal_points[[binoidal_points_counter + 1]] <- c(q[[counter]][[1]][intersection_number[3]],
                                                              q[[counter]][[2]][intersection_number[3]])
          binoidal_points_counter <- binoidal_points_counter + 2
          break
        } 
      }
    }
  } else {
    if (length(minima) != 0) {
      cat("This is wrong isotherm! \n")
    } else {
      cat("We are above critical temperature! \n")
    }
  }
}


x <- array()
y <- array()

for (i in 1 : length(binoidal_points)) {
  x <- c(x, binoidal_points[[i]][1])
  y <- c(y, binoidal_points[[i]][2])
  points(binoidal_points[[i]][1], binoidal_points[[i]][2], pch = 20, col = "blue")
}
x <- x[-1]
y <- y[-1]

func <- splinefun(x, y, method="natural",  ties = mean)
x_for_binoidal <- seq(0, 1, by = 0.01)
points(x_for_binoidal, func(x_for_binoidal), col = "green", type = "l", lwd = 2)
points(x, y, col = "green", pch = 20)
