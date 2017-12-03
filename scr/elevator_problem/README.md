# eprAufgabe4
Uni Goethe Elevator Problem


(a)Die Fahrt-Anforderungen werden in der Reihenfolge der Angabe bearbeitet, zuerst die am weitesten links stehende und die in der i-ten Eingabe vor der in der i+1. Eingabe.
(b)Die Anforderungen im Fahrkorb haben Vorrang vor den Anforderungen auf den Stockwerken, wenn diese Fahrt-Anforderungen im selben Takt auftreten undwerden in jedem Fall bedient.
(c)Fahrkorb Aubernimmt die Anforderungen mit hoeherer Prioritaet als (also vor)Fahrkorb B.(d)Wenn ein Fahrkorb keine offenen Anforderungen mehr hat,ubernimmt er sofort die naechste Anforderung von Stockwerken.
(e)Jeder Fahrkorb wechselt die Fahrtrichtung nur dann, wenn er mit der aktuellen Fahrtrichtung keine Anforderung mehr erfullen kann.

It is important to show the job which the elevator executes!!

Testing:
4h should not work

To do:
Wenn der Aufzug in einer Art Fahrt-Schleife ist, würde er Anforderungen von den Stockwerken, die außerhalb dieser Schleife liegen nie abarbeiten. Deshalb wäre eine Implementierung von
von einer Logik, die Anforderungen von außen in der Selben Fahrtrichtung auch immer Abarbeitet ebenfalls sinnvoll.
Dazu wäre die close taste zu implementieren.
