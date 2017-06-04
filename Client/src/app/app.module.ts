import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {MateriaListComponent} from './materia/materia-list.component';

import { AppComponent }  from './app.component';

@NgModule({
  imports: [ BrowserModule ],
  declarations: [ AppComponent, MateriaListComponent ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
