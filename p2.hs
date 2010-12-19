fib 1 = 1
fib 2 = 2
fib n = (fib (n-1)) + (fib (n-2))

main = putStrLn $show $ map fib [1..100]
