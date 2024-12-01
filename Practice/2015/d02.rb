DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]
t=''
s1=0
s2=0

File.open("#{DAY}.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    l=l.scan(/-?\d+/).map &:to_i
    #l=l.split.map &:to_i
    #l=l.chars.map &:to_i
    #l=l.split
    #l=l.to_i
    #l=l.chars
    
    r+=[l]
    #t+=l
    l,w,h = l
    a=[2*l*w , 2*w*h , 2*h*l]
    s1+= a.sum+a.min/2

    s2+=[l,w,h].min(2).sum*2 + l*w*h
  }
}

p s1,s2