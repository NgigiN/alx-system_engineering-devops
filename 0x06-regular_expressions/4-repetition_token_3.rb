#!/usr/bin/env ruby
#Ruby script that accepts one argument and passes it to a regular expression
#matching method
#can miss a t or have many t's but not any other letter
#Should not contain square brackets

puts ARGV[0].scan(/hbt*n/).join
