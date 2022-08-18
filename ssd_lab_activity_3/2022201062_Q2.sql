select concat(e2.Fname," ",e2.Minit," ",e2.Lname),e2.Ssn,e2.Dno,count(e2.Ssn) 
from EMPLOYEE as e1 ,EMPLOYEE as e2 
where e1.Super_ssn=e2.Ssn group by e2.Ssn,e2.Fname,e2.Minit,e2.Lname 
order by count(e2.Ssn);