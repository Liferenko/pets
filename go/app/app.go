package main

import (
    "html/template"
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
    // fmt.Fprint(w, "(c) Pavels Liferenkols")




    // html/template

    const tpl = `
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>{{.Title}}</title>
        </head>
        <body>
            {{ tange .Items }}<div>{{ . }}</div>{{ else }}<div><strong>no rows</strong></div>{{end}}
        </body>
        </html>
    `





















    check := func(err error) {
        if err != nil {
            log.Fatal(err)
        }
    }
    t, err := template.New("webpage").Parse(tpl)
    check(err)

    data := struct {
            Title string
            Items []string
    }{
            Title: "Моя страница",
            Items: []string{ "Мои фотки", "Мой бложик", },
    }

    err = t.Execute(os.Stdout, data)
    
    check(err)
    noItems := struct {
            Title string
            Items []string
    }{
            Title: "Моя другая страница",
            Items: []string{},
    }

    err = t.Execute(os.Stdout, noItems)
    check(err)

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



































