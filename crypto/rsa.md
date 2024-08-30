## RSA
Salve! Questo è un tutorial su RSA.

Riprendiamo ciò che hai visto a lezione.
RSA è uno schema basato sull'aritmetica modulare.

Ho scelto due piccoli numeri primi. p = 19, q = 17.
Il loro prodotto sarà il modulo (n) che utilizzeremo per fare tutte le operazioni del caso.
n = ? 323
Corretto!

Ora, a noi interessa fare potenze modulo n: questo ci permetterà di cifrare e decifrare i nostri messaggi.
Prima di tutto scegli un numero, che sarà il nostro messaggio da cifrare.
m = ? 55

ϕ(n) è la funzione di Eulero: corrisponde al numero di invertibili modulo n, ossia a
quanti interi tra 1 ed n-1 sono coprimi con n. Nel caso in cui n = pq, ϕ(n) = (p-1)(q-1).
ϕ(n) = ? 288
Corretto!

Infatti in questo caso gli invertibili modulo n sono:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 205, 206, 207, 208, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 222, 223, 224, 225, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 241, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252, 253, 254, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 267, 268, 269, 270, 271, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 286, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322], len == 288.

Nota come calcolare ϕ(n) sia possibile solo grazie alla conoscenza dei fattori di n.
Sì, in questo caso siamo anche riusciti ad elencare esplicitamente tutti gli invertibili, ma
in generale p,q sono numeri molto molto grandi e l'unico modo (efficiente) è ricorrere alla formula.

La sicurezza di RSA è fondata proprio su questo fatto: impedire a tutti i costi ad un attaccante
di fattorizzare il modulo e dunque di recuperare ϕ(n).
Per questo motivo il modulo (n) è parte della chiave pubblica, mentre la sua fattorizzazione è privata.

Torniamo a noi: potenze modulo n. Abbiamo la base m = 55, scegli un esponente.
e = ? 13

Ottimo! Cifra ora il messaggio scelto con l'esponente pubblico scelto: c = m^e (mod n).

Nota: in Python qualcosa come c = m**e % n non va bene. Questo perché quella riga di codice calcola
dapprima tutto m**e (che spesso diventa enorme), per poi effettuare la riduzione modulo n.
Ci sono algoritmi più efficienti: se la curiosità ti infervora, prova a cercare "esponenziazione modulare".
Altrimenti, un'occhiata veloce alla documentazione relativa alla funzione pow() potrebbe esserti d'aiuto..
c = ? 225
Corretto!

Ottimo! Hai cifrato con successo il tuo messaggio. Ora vediamo come decifrarlo.

Naturalmente, vorremmo "effettuare la radice e-esima del nostro cifrato".
Questa, come potrai ormai immaginare, non corrisponde alla radice e-esima nei numeri reali.

Viene in nostro soccorso il Teorema di Eulero:
    Dati a,n interi coprimi, allora a^ϕ(n) = 1 (mod n).

Quindi in realtà, come hai potuto vedere nelle slides, fare la radice e-esima negli interi modulo n
corrisponde ad elevare il cifrato all'inverso modulare (rispetto a ϕ(n)) dell'esponente utilizzato!

Questo è il motivo per cui GCD(e, ϕ(n)) dev'essere uguale a 1. Altrimenti non è possibile invertirlo!
L'inverso dell'esponente pubblico si chiama esponente privato. Anche lui dev'essere mantenuto segreto!
d = ? 133
Corretto!


Ottimo! Infatti pow(c,d,n) == m = True

Da qui in avanti la strada che porta ad un'implementazione sicura di RSA è lunga e tortuosa: ci sarebbero moltissime
altre cose da dire, dettagli a cui stare attenti, casi limite da evitare. Sicuramente, ora sei in possesso delle basi
che ti servono per affrontare challenge un attimino più complesse di questa. Good job! :) flag{RSA_n0n_f4_p1u_C0s1_p4Ur4}
