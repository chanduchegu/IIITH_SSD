select dep_loc.Dnumber,x.Dname,count(dep_loc.Dnumber) from DEPT_LOCATIONS as dep_loc,
(select dep.Essn,d.Dname,d.Dnumber from DEPARTMENT as d,DEPENDENT as dep 
where d.Mgr_ssn=dep.Essn and dep.Sex='F' group by  dep.Essn,d.Dname,d.Dnumber having count(dep.Essn)>=2) as x 
where x.Dnumber=dep_loc.Dnumber group by dep_loc.Dnumber,x.Dname;