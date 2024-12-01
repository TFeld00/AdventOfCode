DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]
t=''
s=0

File.open("#{DAY}.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    #l=l.scan(/-?\d+/).map &:to_i
    #l=l.split.map &:to_i
    #l=l.chars.map &:to_i
    #l=l.split
    #l=l.to_i
    #l=l.chars
    
    r+=[l]
    t+=l
  }
}

i=0
d=0
v=[]
s=[1,1i,-1,-1i]
r2=nil
t.scan(/(\w)(\d+)/).map{
  |a,b|
  b=b.to_i
  s= s.rotate(a==?R ? 1:-1)
  b.times{
    i+=s[0]
    v.index(i) && !r2 && (r2=i.rect.sum(&:abs))
    v<<i
  }
}
p i.rect.sum(&:abs), r2