context("minkowski")

test_that("Similarity should be one for same fuzzy set", {
  
  A <- c(1, 0, 0.5, 0.9, 0.7)
  expect_equal(sim(A, A, 2), 1)
  
})


test_that("Similarity should be one for same fuzzy set", {
  
  A <- c(1, 0, 0.5, 0.9, 0.7)
  expect_equal(sim(A, A, 3), 1)
  
})