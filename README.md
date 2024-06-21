# Anàlsisi de la base de dades *NICS*

## Explicació general

Els següents arxius executen en seguit de funcions on s'analitza la base de dades de l'FBI al respecte de la comprobació d'antecedents previ a tenir una llicència i la venda d'armes. Però és important resltar la propia aclaració que fa l'FBI:


>Les dades simplement recopilen la quantitat de verificacions d'antecedents realitzades. L'FBI desaconsella l'ús d'aquestes dades per a analitzar les vendes d'armes, ja que realitzar una verificació d'antecedents no significa implícitament que es va comprar una arma de foc.


## Arxius i direcotirs

- `funcions.py`: Té totes les funcions que s'executen per analitzar les dades.
- `main.py`: Arxiu principal des d'on s'executa l'arxiu funcions.py i es veu en pantalla el resultat.
- `requeriments.txt`: Llista de dependències necessàries per executar el projecte.
- `readme.md`: L'arxiu on estàs ara mateix i que descriu el projecte. 

## Dependències

El projecte utilitza les següents llibreries que executant el *requeriment.txt* s'instal·laran.

- **Nota: És possible tenir algun problema amb la llibreria selenium. En aquest cas recomenem:**

`pip install folium selenium pillow`

- pandas
- matplotlib
- folium
- Pillow
- selenium

## Instal·lació

```
git clone https://github.com/Merinoide/UOC_PAC4_Programacio.git

cd Projecte

pip install -r requeriments.txt

python3 main.py

```


