#r
py_4=print
li=[1,2,3,4]
py_4(4 in li);
tpl=(1,2,3,4);
py_4(5 in li);
py_4(4 in tpl)
st={1,2,3,4};
py_4(4 in st);
py_4(5 in st)
dt={1:'one',2:'two',3:'three'}
py_4(3 in dt)
py_4(4 in dt)
py_4('one' in dt)
py_4('two' in dt.values())
py_4(1 in dt.keys())
st={3,5,3,1,7,8}
##Loop in list
for i in li:
    py_4(i);
py_4('\n')
##Loop in tuple
for i in tpl:
    py_4(i)
##Loop in diction
for i in dt:
    py_4(i)
py_4('\n')
##Loop in Set
for i in st:
    py_4(i)
py_4(i)

##Iterator
city='Dhaka';
city_itr=iter(city)
py_4(city_itr)
py_4(type(city_itr))
py_4(next(city_itr))
py_4(next(city_itr))
py_4(next(city_itr))
py_4(next(city_itr))
py_4(next(city_itr))
py_4('\n')
for i in city:
    py_4(i);

class my_range:
    def __init__(self,n):
        self.index=0;
        self.max_index=n-1;
    def __iter__(self):
        return self;
    def __next__(self):
        if self.index<=self.max_index:
            self.index=self.index+1;
            return self.index-1
        else:
            raise StopIteration();
        
if __name__=="__main__":
    for i in my_range(5):
        py_4(i);
    
    
## if for loop don't work
if __name__=="__main__":
    it=my_range(5);
    while True:
        try:
            py_4(it.__next__());
            ##py_4(next(it))
        except StopIteration:
            break;
li=[1,2,3];
it=iter(li);
py_4(type(it));
py_4(it)
name='Rifat'
sit=iter(name);
py_4(type(sit))
py_4(sit)
tup=(1,3,5,7);
tup_it=iter(tup);
py_4(type(tup_it));
py_4(tup_it);
