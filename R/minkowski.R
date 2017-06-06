getFuzzyValue <- function(A, index) {
  if (index <= length(A)) {
    return(A[index])
  }
  return(0)
}

sim <- function(A, B, r) {
  numberOfElements = max(length(A), length(B))
  sum = 0
  for(i in 1:numberOfElements) {
    subtraction = getFuzzyValue(A, i) - getFuzzyValue(B, i)
    sum = sum + (abs(subtraction) ** r)
  }
  metric = sum ** (1 / r)
  return(1 - (metric / numberOfElements))
}