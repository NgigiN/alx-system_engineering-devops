#!/usr/bin/env ruby
#Should output [SENDER], [RECEIVER], [FLAGS] with country codes if present

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
