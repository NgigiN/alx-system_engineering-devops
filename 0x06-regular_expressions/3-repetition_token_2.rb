#!/usr/bin/env ruby
#accepts one argument and passes it to the regular epxression matching method
#has atleast one 't'

puts ARGV[0].scan(/hbt+n/).join
