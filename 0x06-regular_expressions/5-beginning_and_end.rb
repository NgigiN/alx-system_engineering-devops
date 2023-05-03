#!/usr/bin/env ruby
#A ruby script that accpets one argument and passes it to the regex method
#Exactly matches a string starting with 'h' and ends with 'n' with any single character between them

puts ARGV[0].scan(/[h].[n]/).join
