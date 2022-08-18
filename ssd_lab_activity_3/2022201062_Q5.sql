select one.Mgr_ssn,one.Dnumber,count(one.Mgr_ssn) from DEPENDENT,
(select DEPARTMENT.Mgr_ssn , DEPARTMENT.Dnumber from DEPARTMENT,DEPT_LOCATIONS 
where DEPARTMENT.Dnumber=DEPT_LOCATIONS.Dnumber 
group by DEPT_LOCATIONS.Dnumber 
having count(DEPT_LOCATIONS.Dnumber)>2) as one where DEPENDENT.Essn=one.Mgr_ssn group by one.Mgr_ssn,one.Dnumber;