# Teleprompter


## Preprocessing

- To replace the caracter

go to ```app.component.ts``` file

find ```replace_char(char)``` function and add the caracter you want to add 

    ```
    
    replace_char(c){
            var value = "";
		    if (c == "0"){
		       value = " zero ";
		    }
		    else if(c == "1"){
		      value = " one ";
		    }
		    else if(c == "2"){
		      value = " two ";
		    }

         return value

       }
    ```
- To do your own preprocessing 

Go to ``` do_other_preprocessing(text)```  function, this function accepts the script text and you can do your own preprocessing inside this function
 

 ``` 

 do_other_preprocessing(text){
     
      Do your preprocessing here.
      
      return text
  }

  ```

# Running Teleprompter 
This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 6.0.8.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.



## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
