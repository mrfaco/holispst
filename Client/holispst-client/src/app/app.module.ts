import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import {MateriaComponent} from "./Materia/materia.component"
import {MateriaList} from "./MateriaList/materia-list.component"
import {Navbar} from "./Navbar/navbar.component"

@NgModule({
  declarations: [
    AppComponent,
    MateriaComponent,
    MateriaList,
    Navbar
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent,MateriaList,Navbar]
})
export class AppModule { }
