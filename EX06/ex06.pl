% Marcus on mees
mees(marcus).
mees(jaan).
mees(francesco).

% Marcus on Popmej elanik
elanik(marcus, pompej).

% Marcus sündis aastal 40
synni_kp(marcus, 40).
synni_kp(jaan, 1977).
synni_kp(francesco, 1989).

% Kõik mehed on surelikud.
surelik(X):-
    mees(X).

% Ükski surelik ei ela rohkem kui 150 aastat
surnud_vanus(X, Vanus):-
    surelik(X),
    Vanus > 150.    

% Praegu on aasta 2019. Kas Marcus on elus?
surnud_aasta(X, Aasta):-
    surelik(X),
    synni_kp(X, Synni_aasta),
    Vanus = Aasta - Synni_aasta,
    surnud_vanus(X, Vanus).

% Kõik Pompej elanikud surid vulkaanipurske tagajärjel aastal 79
surnud_pompej_vulkaan(X):-
    elanik(X, pompej),
    not(surnud_aasta(X, 79)).

% Kas Jaan on surnud?
% Kas Francesco on surnud?
surnud(X):-
    surnud_aasta(X, 2019);
    surnud_pompej_vulkaan(X).