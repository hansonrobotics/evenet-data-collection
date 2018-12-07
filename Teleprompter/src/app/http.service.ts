import { Injectable } from '@angular/core';
import 'rxjs/add/operator/map';
import { Observable } from 'rxjs/Observable';
import { HttpClient } from '@angular/common/http';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class HttpService {
  private url = "http://localhost:9900";
  constructor(private http: HttpClient) {



  }

  set_server_url(url:any){
  	this.url = url;
  }

  send_data(data:any){
  	let encoded_data = JSON.stringify({ data });
  	console.log("encoded_data about to send", encoded_data);
    let headers = new Headers({ 'Content-Type':  'application/json' });
    let options = new RequestOptions({ headers: headers });
    const httpOptions = {
		  headers: new HttpHeaders({
		    'Content-Type':  'application/json;charset=utf-8',
		    'Access-Control-Allow-Headers':'Content-Type',
		    'Access-Control-Allow-Methods':'GET',
		    'Access-Control-Allow-Origin':'*'
		  })
		};

    return this.http.post(this.url,encoded_data).map(
            (res: Response) => res.json() || {}
        );
  }
}
