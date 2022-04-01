function newPar = resample(par, n)

w = cat(2, par(:).w); 
len= length(w);
keep= zeros(1,len);
select = rand(1,len);
select = cumsum(select); 

w= cumsum(w);
ctr=1; 
for i=1:len
   while ctr<=len & select(ctr)<w(i)
       keep(ctr)= i;
       ctr=ctr+1; 
   end
end

end