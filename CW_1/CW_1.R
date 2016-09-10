require(MESS)

a <- 3.592
b <- 0.04267

generate_arrays <- function(Temp) {
  x <- array()
  y <- array()
  
  x[1] <- b + 0.00001
  for (i in 2 : 100000) {
    x <- c(x, b + 0.001 * i)
  }
  y <- (0.082 * Temp) / (x - b) - (a / (x * x))
  
  res <- list()
  res[[1]] <- x
  res[[2]] <- y
  return(res)
}

q <- list()
for (i in 1 : 5) {
  q[[i]] <- generate_arrays(245 + i * 15)
  cat(i, "\n")
}

plot(q[[1]][[1]], q[[1]][[2]], main = "vdW", xlab = "V", ylab = "p", type = "l", xlim = c(0, 3), ylim = c(0, 100))
for (i in 1 : 5) {
  points(q[[i]][[1]], q[[i]][[2]], type = "l", col= i, lwd = 2)
}

# spinodal <- array()
# spinodal <- a * (q[[1]][[1]] - 2 * b) / (q[[1]][[1]]^3)
# points(q[[1]][[1]], spinodal, type = "l", col = 1, lwd = 2)

# maxima <- q[[1]][[2]][which(diff(sign(diff(q[[1]][[2]])))==-2) + 1]
# minima <- q[[1]][[2]][which(diff(sign(diff(q[[1]][[2]])))==+2) + 1]

for (counter in 1 : 5) {
  maxima <- q[[counter]][[2]][which(diff(sign(diff(q[[counter]][[2]])))==-2) + 1]
  minima <- q[[counter]][[2]][which(diff(sign(diff(q[[counter]][[2]])))==+2) + 1]

  if (length(maxima) != 0 && length(minima) != 0) {
    for (s in 1 : 1000) {
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
          points(intersection[[k]][1], intersection[[k]][2], col = "blue", pch = 20)
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
        if (abs(s_in_left - s_in_right) < 0.5) {
          cat("Found it! \n")
          break
        } 
      }
    }
  } else {
    cat("We are above critical temperature! \n")
  }
}

#  abline(h = maxima, col = counter, lwd = 2) 
#  abline(h = minima, col = counter, lwd = 2) 
  abline(h = h, col = counter, lwd = 2)
  cat("h: ", h, "\n")
}
