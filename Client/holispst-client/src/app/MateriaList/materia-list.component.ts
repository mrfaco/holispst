import {Component,Injectable} from '@angular/core'
import {MateriaComponent} from '../Materia/materia.component'
import {Http,Response} from '@angular/http'
import {Observable} from 'rxjs/Observable'
import 'rxjs/add/operator/map'


@Component(
    {
        selector:'materia-list',
        templateUrl:'./materia-list.component.html'
    }
)

@Injectable()
export class MateriaList{

    materias: MateriaComponent[];
    errorMessage:string;

    constructor(private _http:Http){}

    ngOnInit(): void {
        this.GetFromApi().subscribe
        (mat=>this.materias=mat,error=>this.errorMessage=<any>error);
        console.log(this.errorMessage)
    }

    GetFromApi(): Observable<MateriaComponent[]> {
        return this._http.get('http://localhost:5000/Materias/')
        .map((response:Response)=><MateriaComponent[]>response.json());
    }
}