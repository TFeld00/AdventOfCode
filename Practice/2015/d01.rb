DAY,_,_ = __FILE__.rpartition(?.)

require'prime'
require'z3'

r=[]
t=''
s=0

File.open("#{DAY}.txt", "r") { |f|
  f.each_line {|l|
    l=l.chomp
    r+=[l]
    t+=l
  }
}

p t.count(?()-t.count(?))

f=0
i=0
t.chars.map{|c|
  f+= c=='(' ? 1 : -1
  i+=1
  f<0 && (p i;exit(0))
}