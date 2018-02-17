package main

import (
	"fmt"
	"net/http"
)

func index_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Wow, go is great!")
}

func about_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "It is written by Rachel!")
}

func main() {
	http.HandleFunc("/", index_handler)
	http.HandleFunc("/about/", about_handler)
	http.ListenAndServe(":8000", nil)
}
