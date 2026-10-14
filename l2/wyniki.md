# c1
Poprawnym przesunięciem jest 233. Jest ono prawidłowe, ponieważ po wyświetleniu początku odszyfrowanego tekstu tylko dla tego przesunięcia otrzymujemy czytelny wynik.

Okazało się, że samo sprawdzenie, czy wszystkie odszyfrowane znaki mieszczą się w odpowiednim zakresie, nie wystarcza do stwierdzenia, czy wynik jest poprawny. Nawet przy tak niewielkiej trudności można jednak stosunkowo łatwo odszyfrować szyfr Cezara.

# c2
Dla tekstu 'BRAMABRAMABRAMA' i klucza 'SZYFR' szyfrowanie generuje powtarzającą się sekwencję bajtów. Wynika to z faktu, że w oryginalnym tekście co pięć znaków powtarza pięć tych samych bytów. W efekcie trzykrotnie szyfrujemy słowo 'BRAMA' kluczem 'SZYFR'.

Możliwość występowania takich powtórzeń może ułatwić odgadnięcie klucza. Jeśli określony wzorzec w tekście powtarza się wielokrotnie, a my miniej więciej jakie słowa tam powino być, możemy to wykorzystać aby odgadnąć klucza.

# c3

Drugie szyfrowanie tym samym kluczem efektywnie odszyfrowuje wiadomość. Wynika to z faktu, że wykorzystujemy operację XOR, która zastosowana dwukrotnie z tą samą wartością przywraca orginalną wartość.

Lista kandydatów na klucz wraz z obliczoną entropią odszyfrowanej wiadomości:

Klucz          Entropia
[116,  97, 116]  4.39
[110, 101, 103]  7.43
[109,  99, 110]  7.45
[111, 120, 111]  7.45
[116, 110, 120]  7.45


Poprawnym kluczem jest [116, 97, 116]. Tekst pisany ma stosunkowo niską entropię, a klucz jest krótki, dlatego mogliśmy przetestować wszystkie możliwe kombinacje i znaleźć wynik o najniższej entropii, który odpowiada orginalnemu tekstowi.

Można również zauważyć, że po odszyfrowaniu wiadomości przy użyciu drugiego najlepszego klucza otrzymujemy tekst o entropii zbliżonej do entropii ciągu losowych bajtów.