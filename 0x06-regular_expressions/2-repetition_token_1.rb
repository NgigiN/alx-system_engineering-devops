#!/usr/bin/env ruby
#Ruby script that accepts one argument and passes it to a regex
#no b and a single b

puts ARGV[0].scan(/hb?tn/).join
