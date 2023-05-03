#!/usr/bin/env ruby
#A ruby script that accpets one argument and passes it to the regex method
# Only matches capital letters

puts ARGV[0].scan(/[A-Z]+/).join
