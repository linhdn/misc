My senior classmate `vn.linkedin.com/in/quannguyenhoang` tagged me on Facebook to this challenge, from Geeky.vn.

# Round 1: Register
```
Syntax: register <email> <key>
email: your email address, make sure it's correct to reserve your spot
key: the first { [ (prls636 - prime36) << 7 ] - 1 } digits after decimal of Pi, in MD5
```
At first, like all others, I was deciced by the `prime`, although I was more than aware about `hexatridecimal`. Nevertheless, the next morning, while waiting for bus on the way to work, I solved it. Anyway, the way to find that exact digits after decimal of `pi` was quite unexpectedly difficult.

Personally, even before solving the riddle, I thought that the implementation gave too open space for brutforcing, from the algorithm (with good strategy, no more than 10'000), to the fact that they did not have XSS attack defense, i.e. one could easily curl -X POST -d "<param>" <url>
