#!/bin/ruby

s = gets.strip
t = gets.strip
k = gets.strip.to_i

firstN = 0
for i in 0..t.length
    if s[i] != t[i]
        firstN = i
        break
    elsif i == t.length - 1
        firstN = t.length
    end
end

nDel = s.length - firstN
nApp = t.length - firstN
result = ((k - nDel - nApp) % 2 == 0 && k >= nDel + nApp) || k > s.length + t.length
puts result ? 'Yes': 'No'
        