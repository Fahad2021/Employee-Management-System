import { Component, OnInit,Input } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-emp',
  templateUrl: './add-edit-emp.component.html',
  styleUrls: ['./add-edit-emp.component.css']
})
export class AddEditEmpComponent implements OnInit {

  constructor(private service:SharedService) { }
  @Input() emp:any;
  EmployeeId:string;
  EmployeeName:string;
  Department:string;
  DateofJoining:string;
  PhotoFileName:string;
  PhotoFilePath:string;

  DepartmentsList:any=[];


  ngOnInit(): void {
    this.loadDepartmentList();
   
  }

  loadDepartmentList(){
    this.service.getAllDeaprtmentNames().subscribe((data:any)=>{
      this.DepartmentsList=data;

      this.EmployeeId=this.emp.EmployeeId;
      this.EmployeeName=this.emp.EmployeeName;
      this.Department=this.emp.Department;
      this.DateofJoining=this.emp.DateofJoining;
      this.PhotoFileName=this.emp.PhotoFiileName;
      this.PhotoFilePath=this.service.PhotoUrl+this.PhotoFileName;
    });
  }

  addEmployee(){
    var val={
      EmployeeId:this.EmployeeId,
      EmployeeName:this.EmployeeName,
      Department:this.Department,
      DateofJoining:this.DateofJoining,
      PhotoFileName:this.PhotoFileName
    };

      this.service.addEmployee(val).subscribe(res=>{
        alert(res.toString());
      });
    }

  updateEmployee(){
    var val={
      EmployeeId:this.EmployeeId,
      EmployeeName:this.EmployeeName,
      Department:this.Department,
      DateofJoining:this.DateofJoining,
      PhotoFiileName:this.PhotoFileName
    };

      this.service.updateEmployee(val).subscribe(res=>{
        alert(res.toString());
      });
    }

    UploadPhoto(event){
      var file=event.target.files[0];
      const formData:FormData=new FormData();
      formData.append('Uploadfile',file,file.name);

      this.service.UploadPhoto(formData).subscribe((data:any)=>{
        this.PhotoFileName=data.toString();
        this.PhotoFilePath=this.service.PhotoUrl+this.PhotoFileName;

      })

    }
  }