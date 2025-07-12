Dragan Marius,312CB
Magazinul a fost realizat in limba romana.

	Tema contine urmatorele fisiere:
-app.py
-Dockerfile
-fisier Json
-folder static:pozele produselor
-folder templates:paginile html(base,cart,checkout,success,contact,index)
-requirements

Informatiile din requirements au fost scrise folosind comanda pip freeze > requirements.txt.Comenzile  docker build -t iap1-tema ./ si docker run -p 5000:5000 -it iap1-tema eu le-am rulat cu sudo.Stiu ca poate nu e cel mai frumos site,nu sunt foarte creativ dar sper ca tema mea sa fie apreciata:)))

	Fisier app.py

    Am importat modulele necesare pentru crearea aplicatiei Flask,sabloanele HTML(render_template),sesiune(session),fisierele JSON(json) si manipularea fisierelor(os)
app=Flask(__name__) si app.secret_key='supersecretkey' creeaza instanta aplicatiei si seteaza o cheie secreta pentru gestionarea sesiunii.Apoi am facut o lista de dictionare care reprezinta produsele disponibile in magazinul meu,ParkAuto.Fiecare produs are:id,nume,pret,imagine(din folderul static).Urmeaza apoi functiile. Am inceput cu o functie auxiliara get_cart_item_count care returneaza toate produsele pe care clientul le are in cos.
Functia index afiseaza pagina cu produsele disponibile si se foloseste de sablonul index.html. Functia add_to_cart(product id).Adauga in cos un produs cu id-ul acela si mareste cantitatea.Functia cart parcurge produsele din cos si calculeaza subtotalurile si totalul final si trimite in cart.html.Functia checkout arata formularul daca se foloseste metoda GET si creeaza un dictionar order cu datele clientului si produsele pe care acesta le-a comandat daca se foloseste POST.Aceasta salveaza comanda in order.json si goleste cosul.Se redicretionaza catre success.Functiile increaza_qty si decrease_ytq maresc/scad cantitatea unui produs din cos.La cantitatea =0 produsul se elimina cu totul din cos.Functia contact afiseaza pagina de contact a magazinului. Functia success afiseaza confirmarea comenzii.In josul fisierului se afla comanda if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0') care porneste serverul Flask accesibil pe toate interfetele.

	Fisier Dockerfile

   Comanda FROM python:3.10-slim alege o imagine de baza pentru reducerea dimensiunii containerului.Comanda WORKDIR /app creeaza si seteaza directorul de lucru iar comenzile run copy cmd vor fi executate in acest director.Apoi am instalat pachetele de sistem necesare pentru biblioteci Python din requirements.txt si la final se curata lista de pachete. Apoi am copiat toate fisierele din directorul curent in directorul de lucru.Am instalat toate bibiliotecile Python necesare.Am folosit portul 5000 ca port implicit si la final va rula app.py la startul containerului.

	Folder templates

      Fisier base.html
   Acest fisier contine antetul,bara de navigatie, footer-ul si zona de continut. Am folost block content.Pagina mea contine link-uri catre stiluri CSS externe. Navbar-ul contine link-uri catre:Acasa,cos,contact. In pagina se regaseste si footer-ul si se xxtinde in toate celelalte fisiere HTML prin {% extends "base.html" %}.
      Fisier index.html
   Acest fisier afiseaza produsele disponibile intr-o grila de carduri si contine titlul,un for care genereaza cardurile cu imagine,nume,pret si butonul de adaugare in cos. Datele despre produse sunt trimise de app.py din lista de products.
      Fisier cart.html
   Acest fisier afiseaza produsele care au fost adaugate in cos si permite modificarea cantitatilor.Este fornat din tabel cu coloane despre produs,cantitate,pret unitar,subtotal si butoane de adaugare/scadere produse;totalul comenzii si butoane pentru finalizare comanda si continuare cumparaturi.
       Fisier checkout.html
    Acest fisier contine un formular in care utilizatorul introduce datele de livrare si datele despre metoda de plata.Este structurat astfel:lista cu produse,pretul total,formular cu campurile:nume,email,numar de telefon,adresa si metoda de plata; si butonul de trimite comanda.Toate aceste campuri sunt obligatorii de completat!!
       Fisier contact.html
    Acest fisier contine informatiile de contact ale magazinului si un formular simplu de trimitere mesaj.Este compus din adresa,numar de telefon,adresa de email,programul de lucru si formular cu urmatoarele campuri:nume,mesaj si buton trimitere.
        Fisier success.html
   Pagina este afisata dupa ce comanda a fost trimisa cu succes si contine:mesaj de multumire,text informativ despre emailul de confirmare si buton catre pagina principala.