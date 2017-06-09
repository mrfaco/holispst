import {Component} from '@angular/core'


@Component({
    selector:'materia',
    templateUrl:'./materia.component.html'
})


export class MateriaComponent{
    Id:number;
    Name:string;
    Price:number;
    Stock:number;
    Date:string;


    constructor(id:number,name:string,price:number,stock:number,datemodified:string){
        this.Id=id;
        this.Name=name;
        this.Price=price;
        this.Stock=stock;
        this.Date=datemodified;
    }
}
