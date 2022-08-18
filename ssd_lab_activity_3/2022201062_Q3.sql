select mgr.Mgr_ssn,count(*) from WORKS_ON as wor,
(select dept.Mgr_ssn from DEPARTMENT as dept 
where dept.Dnumber in 
(select Dnum from PROJECT where Pname="ProductY")) as mgr  
where wor.Essn=mgr.Mgr_ssn group by mgr.Mgr_ssn ;