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
Wenn der Aufzug in einer Art Fahrt-Schleife ist, wuerde er Anforderungen von den Stockwerken, die ausserhalb dieser Schleife liegen nie abarbeiten. Deshalb waere eine Implementierung von
von einer Logik, die Anforderungen von aussen in der Selben Fahrtrichtung auch immer Abarbeitet ebenfalls sinnvoll.
Dazu wäre die close taste zu implementieren.


Improvements:
Elevator Superposition, A on level K and B on level 3. CHECK
Algorithm according to time of the day, morning prio E level
Fast door closing no more dice rolling, but "internally dedicated door closing buttons"
Maybe the Elevator closest to a floor job can work on this job, not just A before B CHECK
And this being said, we can count the calls from a special floor, and if this special floor CHECK
generates a lot of calls, the elevators can use them as idle position??? 
That thing niels said, but wasnt understandable

Andorderungen von außen sollen vom nächsten Aufzug abgeholt werden. CHECK
