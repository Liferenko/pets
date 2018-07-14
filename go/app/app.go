package main

import (
    "fmt"
    "github.com/julienschmidt/httprouter"
    "log"
    "net/http"
    "os"
)

func indexHandler(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprintf(w, "Поговаривают, что это и есть RESTful api")
}

func pavelLiferenko(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
    fmt.Fprint(w, "(c) Pavels Liferenkols")
}

func main() {
    router := httprouter.New()
    router.GET("/", pavelLiferenko)


    // print env
    env := os.Getenv("APP_NEW")
    if env == "production" {
        log.Println("-=Running api server in production mode!=-")
    } else {
        log.Println("-=Running api server in develop mode=-")
    }

    http.ListenAndServe(":8080", router)


}

