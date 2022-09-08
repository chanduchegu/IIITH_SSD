function func()
{
    // e.preventDefault();
    // console.log("hello");
    let rollNo=document.getElementById("RollNumber").value;
    let studentname=document.getElementById("StudentName").value;
    console.log(rollNo);
    console.log(studentname);
    let table=document.getElementById("table");
    var row=table.insertRow(-1);
    var newRollno=row.insertCell(0);
    var newStudnetName=row.insertCell(1);
    newRollno.innerHTML=rollNo;
    newStudnetName.innerHTML=studentname;
}
function deleteFunc()
{
    let l=document.getElementById("table").rows.length;
    if(l!=1)
        document.getElementById("table").deleteRow(-1);
}