import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule,JsonpModule } from '@angular/http';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import {WebSocketService} from "./web-socket.service"
import {HttpService} from "./http.service"
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    JsonpModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [WebSocketService,HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
