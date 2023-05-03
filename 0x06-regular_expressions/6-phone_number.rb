#!/usr/bin/env ruby
#A ruby script that accpets one argument and passes it to the regex method
#Must match a 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
