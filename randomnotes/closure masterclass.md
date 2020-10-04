
# Closure masterclass

## Functions are closures


  

## *Both of these are unnamed closures that could be thought of as // (String) -> Void or ()*

  

func doSomething() {

print(“foo”)

}

  
  

Func printName(name: String) {

print(name)

}

  
  ## *The following is a closure*

Let doSomethingClosure: () -> Void = {

print(“foo”)

}

  ## *Completion closure*

func doSomething(thenDoSomethingElse: (String) -> Void) {
print("Foo")

//We've finished the doSomething part, so call the somethingElse Closure

thenDoSomethingElse("Spencer")
}

### in another part of the app

doSomething { (name) in
print(name)
}

### Different way of doing the same thing above

doSomething(thenDoSomethingElse: PrintNameClosure)

doSomething(thenDoSomethingElse: printName)

## Data, Response, Error
Func dre(data: Data, response: URLResponse?, error: Error?) -> Void {

  

}

Func dreClosure: ( Data, URLResponse?, Error?) -> Void = { (data, response, error) in

print(data)

}

URLSession.shared.dataTask(with: url, completionHandler: fetchQuakesDRE(data:response:error:).resume?

 func fetchQuakesDRE(data: Data?, response: URLResponse?, error: Error?) {
 
 }
 
  

URLSession.shared.dataTask

  

If you press enter you get the closure syntax shown above

f\
