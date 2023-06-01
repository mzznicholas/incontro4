# Incontro 4

**Attenzione**: il file `tester.py` viene utilizzato per stampare il risulatato dei test, non va modificato e non è utile allo svolgimento dell'esercizio

## Social Network
Si vuole realizzare un programma per simulare un piccolo social network. 
Parte fondamentale del programma è l'utente (`User`), composto da:
- `name (str)`: il nome
- `friends (set)`: l'insieme degli amici
- `hobbies (set[str])`: l'insieme degli hobby dell'utente (stringhe)

Successivamente, implementare la classe `SocialNetwork` composta da un insieme di utenti chiamato `users` e dai seguenti metodi:
- `register_user(self, user: User)`: aggiunge l'utente al social network
- `add_friend(self, user1: User, user2: User)`: viene scambiata l'amicizia tra i due utenti (ricorda che l'amicizia è bidirezionale)
- `remove_friend(self, user1: User, user2: User)`: viene **rimossa** l'amicizia tra i due utenti (ricorda che l'amicizia è bidirezionale)
  - `print_hobbies_counter(self)`: stampa, per ogni hobby, il numero complessivo di utenti a cui piace quel determinato hobby. Ad esempio:
    ```
    Cucina: 8
    Giardinaggio: 5
    Golf: 7
    ```
    **Extra**: esegui la stampa in ordine alfabetico.

- `suggest_a_friend(self, user: User) -> User`: si cerchi l'utente con il numero maggiore di hobby in comune con lo user passato come parametro (attenzione, non devono essere già amici e..?)

## RPN
Una calcolatrice **R**everse **P**olish **N**otation è un (vero) tipo di calcolatrice che permette di computare operazioni matematiche senza l'uso di parentesi. 
L'utente digita un numero e premere **enter**, in questo caso il numero viene inserito in memoria. Se, invece, preme uno dei tasti operazione (+, -, /, *) allora vengono estratti dalla memoria gli ultimi numeri inseriti, viene effettuata l'operazione e il risultato inserito in memoria.
Ad esempio, l'espressione `2 * (5 + (4 / 2))` diventa:
```
2
5
4
2
/
+
*
```

La calcolatrice possiede un campo `memory` per memorizzare i numeri inseriti. **Quale struttura potremmo usare per rappresentare la memoria della calcolatrice?**

Viene richiesto di completare la classe RPN con i seguenti metodi:
- `enter(self, number: float)`: il numero indicato viene aggiunto in memoria
- `last(self) -> float`: viene ritornato l'ultimo numero inserito in memoria, senza rimuoverlo. Se non ce ne sono, ritorna `0.0` 
- `sum(self) -> float`: esegue la somma tra gli ultimi due numeri inseriti in memoria (penultimo + ultimo), inserisce il risultato in memoria e ritorna il risultato. Se i numeri in memoria non sono sufficienti, sollevare un `ValueError`
- `diff(self) -> float`: come sum ma con una sottrazione (penultimo - ultimo)
- `mul(self) -> float`: come sum ma con una moltiplicazione (penultimo * ultimo)
- `div(self) -> float`: come sum ma con una sottrazione (penultimo / ultimo). Se il secondo addendo è 0.0, sollevare un `ZeroDivisionError`
- `clear(self)`: svuota la memoria della calcolatrice

Viene già implementato un main di collaudo con alcuni test automatici, **superare tutti i test non significa essere sicuri che il programma sia corretto al 100%**. Alla fine dei test, è possibile interagire con la calcolatrice inserendo numeri (utilizzare il "." per i decimali) ed effettuando operazioni.

## Tournament
Si vuole creare un programma che simula lo svolgersi di un torneo a squadre ad eliminazione diretta (siamo interessati solo al vincitore finale).

Ogni `Team` si compone di:
- `name (str)`: il nome del team
- `exp (int)`: il grado di esperienza del team

Inoltre, completare i seguenti metodi:
- `__str__(self) -> str`: ritorna la stringa nella forma `Team NAME (EXP)`
- `__lt__(self, other) -> bool`: dove due team vengono confrontati per il livello di esperienza

Successivamente, viene richiesto di completare la classe `Tournament`. La classe possiede un campo `teams` che rappresenta le squadre in gara. **Utilizza una coda per questo campo**.

Inoltre, vengono richiesti i seguenti metodi:
- `register_team(self, team: Team)`: il team viene aggiunto al torneo
- `is_finished(self) -> bool`: viene ritornato `True` se il torneo è finito, ovvero è rimasta solo una squadra in gioco. Altrimenti, viene ritornato `False`
- `get_next_two_teams(self)`: vengono estratti due teams dalla memoria e ritornati (come tupla)
- `play_match(self, team1, team2) -> Team`: viene giocata la partita tra le due squadre. Il giocatore con esperienza più alta avrà 2/3 di possibilità di vittoria mentre l'altro solo 1/3. Solo la squadra vincente resterà nel torneo. Inoltre, ritornare la squadra vincitrice (**Hint**: usare random.randint)
- `get_winner(self) -> Team`: viene ritornato il team vincitore, ovvero l'unico rimasto

Viene già implementato un main di collaudo, se il programma è corretto dovrebbe vincere il **Team E**.




