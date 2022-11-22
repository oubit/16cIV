# Combate

Batalla vs Combate vs Intercambio vs Turno (`renombrar turno a movimiento`)


## Iniciativa
Tirada de todos los participantes.
Puede ser talento Iniciativa, o habilidad Cognición-Ejecutiva.

La diferencia de valor de iniciativas. Si el pasivo no realiza tirada de iniciativa, el valor es 5.

## Maniobra

Toda área/subárea/talento debe tener calculado sus valores:
- Activo: 
    - Suma de puntos a nivel de área -> subárea -> talento -> objeto
    - Cuando se lleva la iniciativa, se inicia la acción
    - Determinar el formato de dados que quieras
        - p.e. mi talento me da 15 puntos, uso 2d6
        - dependerá de si vamos a asegurar o lo vemos fácil
- Pasivo: 
    - Valor calculado según los puntos de activo
    - Cuando NO se lleva la iniciativa, se es receptor de una acción
    - Sirve como valor de éxito.

Solo el que es activo realiza tirada de maniobra. Solo una tirada al comienzo del combate.
El que recibe determina su valor pasivo en base a su habilidad y modificadores:
- Situación
- Vitalidad

Los 1s eliminan los éxitos
- Si al final >0 éxitos: hay éxito en la acción. Si hubiera muchos éxitos podría considerarse golpe especial??
- Si al final 0 éxitos: no hay éxito y se pierden puntos 2 de iniciativa por intercambio.
- Si al final >0 fracasos: se considera pifia y se cambia la iniciativa. 
    En función del número de 1s o situación, el master podría determinar mayor penalización tipo:
    - Modificador a la situación (flanqueo, despistado, sorpresa...)
    - Pierde valor pasivo derivado de la pifia

Coherencia Pifia
- Tamaño de dado es coherente??
- Número de dados es coherente??
- Con menos dados, estás forzando más, y sin embargo menos probabilidad de 1, pero cuando sales, seguramente suponga pifia.
    Ejemplo con 12 puntos
    - 1d12: probabilidad de pifia = 1/12 siempre = 8%
    - 2d6: probabilidad de pifia = depende de la FD. 
        - Si es 3 => 1/6*2/6 + 1/36 = 3/36 = 1/12 = 8%
        - Si es 4 => 1/6*3/6 + 2/36 = 5/36 = 14%
- Se solventa con: si solo se tira un dado, la pifia es 1/2.

Crítico/Golpe especial
- Todo éxitos
- Al menos un valor máximo + 20 en d20
    - No es coherente con tamaño de dados

## Ejecución
El resto se gestiona con dado de ejecución d20.

La clave está en que sea ágil para:
- Recalcular iniciativa
    - d20
    - Éxitos:
        - Hay éxitos, se mantiene la iniciativa
        - No hay éxitos, baja un valor
        - Hay pifia, hay cambio de iniciativa con valor 5.
    - Más sencillo limitarlo al dado, pero podría entrar la cosa en bucle infinito
    
- Movimientos tácticos para cambiar combate
    - d20
    - Cambio de iniciativa

## Resolución
Cuando hay cambio de iniciativa, es nuevo combate, se invierte el pasivo y activo y hay nueva tirada.


## Ejemplo

- Activo: 2d6 y sale un 5 y un 4.
- Pasivo: tiene un 4