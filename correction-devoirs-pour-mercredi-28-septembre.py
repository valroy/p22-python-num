# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: "Python-num\xE9rique - introduction"
# ---

# %% [markdown]
# # devoirs pour le 28/09

# %% [markdown]
# ## devoirs pas rendus

# %% [markdown]
# lora.allamand  
# martin.coste (pas répondu questionnaire)    
# maxime.darrambide  
# etienne.debricon  
# valentin.exbrayat  
# clemence.jung  
# adrien.le_marchand  
# yoan.richard  
# jean-sidati.thepaut  
# valentin.wellenstein  
#
# tristan.montalbetti (problème de portable)  
# aissatou.toure (excusée changement de groupe)

# %% [markdown]
# seuls martin.coste et yoan.richard n'avaient rien fait  
# les autres c'était des problèmes normaux de repos 

# %% [markdown]
# ## corrections

# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# %% [markdown]
# ### mauvaise taille des pixels

# %%
Im[0, 0]

# %%
Im = np.random.randint(0, 256, size=(10, 10, 3))

# il faut 3 canaux R, G et B (il en manque donc 2)
plt.imshow(Im, cmap="Wistia") # R, G ou B ?

# %%
plt.imshow(Im, cmap='Reds')
plt.show()
plt.imshow(Im, cmap='Greens')
plt.show()
plt.imshow(Im, cmap='Blues')
plt.show()
;

# %% [markdown]
# ### mauvais type des pixels

# %%
type(image)

# %%
image=np.random.randint(0, 256, size=(10, 10, 3)) # vu plusieurs fois
plt.imshow(image);

# %% [markdown]
# le type par défaut est un `np.int64` (64 bits soit 8 bytes/octets)

# %% [markdown]
# la taille des éléments est:

# %%
image.itemsize # 8 octets

# %% [markdown]
# le type des éléments est:

# %%
image.dtype

# %% [markdown]
# le nombre en octets (bytes) du tableau est:

# %%
image.nbytes

# %%
# #np.random.randint?

# %% [markdown]
# alors qu'un `np.uint8` suffit:

# %%
image2_uint8 = np.random.randint(0,256,size=(10,10,3), dtype=np.uint8)

# ou encore
image_uint8 = image.astype(np.uint8)

image2_uint8.nbytes, image2_uint8.nbytes

# %%
image_uint8 is image

# %%
image_uint8.base is None

# %%
image.base is None

# %% [markdown]
# on gagne sur une image de 10 x 10

# %%
(image.nbytes - image_uint8.nbytes) # octets - bytes

# %% [markdown]
# soit 7 octets par élément (et on a 100 éléments):

# %%
image.itemsize - image_uint8.itemsize

# %% [markdown]
# #### une subtilité

# %% [markdown]
# attention à la PEP8...

# %%
image = np.random.randint(0, 256, size=(10, 10, 3))

# %%
# # image.astype?

# %% [markdown]
# ```
# copy : bool, optional
#     By default, astype always returns a newly allocated array.
# ```
#
# mais
# ```
#     If this is set to false, and the `dtype`, `order`, and `subok`
#     requirements are satisfied, the input array is returned instead
#     of a copy.
# ```

# %%
image.dtype

# %% [markdown]
# un type `uint64` tient sur la même taille d'éléments que `int64`

# %%
image.astype(np.uint64) is image # astype par défaut copie l'espace mémoire

# %%
image.astype(np.int64, copy=False) is image # astype par défaut copie l'espace mémoire

# %% [markdown]
# mais à taille exacte uniquement... non là c'est pas bon

# %%
image.astype(np.int32, copy=False) is image

# %% [markdown]
# ### ne pas mélanger les types `python` list et `numpy` `ndarray`

# %% [markdown]
# et jamais de boucle `for` si on peut utiliser une fonction `numpy`

# %% [markdown]
# fait par un élève et copié par un autre   
# ne pas copier sans comprendre svp !

# %%
import matplotlib.pyplot as plt
L=[]
for k in range (10):
    T=[]
    for l in range (10):
        T. append(np.random.randint(0,256,3))  
    L.append(T)    
plt.imshow(L)

# %%
L=[]
for k in range (10):
    T=[]
    for l in range(10):
        T.append(np.random.randint(0,256,3))
    L.append(T)
plt.imshow(L)

# %%
type(L), type(L[0]), type(L[0][0])

# %% [markdown]
# passer à `np.random.randint` la taille `size=(10, 10, 3)` et donc le type

# %% [markdown]
# ### attention aux bornes

# %%
import matplotlib.pyplot as plt
mat = np.random.randint(0, 255, (10,10,3))  
plt.imshow(mat)

# %%
# # np.random.randint?

# %% [markdown]
# ```
# Return random integers from the "discrete uniform" distribution of
# the specified dtype in the "half-open" interval [`low`, `high`).
#
# ```
# `high` is not included

# %% [markdown]
# ### antonin.franck

# %% [markdown]
# ### `u` pour proposer des entiers non-signés à numpy

# %%
# votre code ici
mat = np.array([[  0,   8,  34,   8],
     [255,  61, 128, 254]],np.int16) # np.uint16
mat
Mat = np.array([[  0,   8,  34,   8],
     [255,  61, 128, 254]],np.int8)
Mat
#l'entier n'est pas assez grand pour coder 255, 128 et 254
#je ne sais pas comment proposer des entiers non signés à Python

# %%
T = np.empty((3,5),np.int8)
T
# il contient des entiers aléatoires (et beaucoup de 0)

# %%
# votre code
import math
r = 10
theta = np.linspace(0 , 2*math.pi , 10000)
x = r*np.sin(theta)
y = r*np.cos(theta)
plt.axis('equal')
plt.plot(x,y)
plt.show()


# %% [markdown]
# oui $2\pi$ est bien inclus
# ```
# Returns `num` evenly spaced samples, calculated over the
# interval [`start`, `stop`].
# ```
#

# %%
# # np.linspace?

# %%
# votre code ici
def scalar_function(x):
    return x**3 + 2*x**2 - 5*x + 1
X=np.ndarray((3,1,2))
print(X)
Y=scalar_function(X)
print(Y)

# %%
np.power # c'est bien une ufunc


# %%
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
absolute(-4)
X=np.ndarray((2,5,6))
absolute(x)


# %% scrolled=true
tab = np.array([10, -30, 56.5])
absolute(tab)

# %% [markdown]
# *problème*   
# (attention `tab` n'est pas  le bon dans le résultat suivant)  
# l'expression x >= 0 appliquée à tab rend le tableau array([False, True, False])
#
#
#
# if appliqué au tableau de booléens [False, True, False] ne sait pas quoi faire
# alors il propose des solutions
#
# if est-il vrai quand tous les éléments sont vrais ? np.all(x)
# if est-il vrai quand au moins un élément du tableau est vrai ? np.any(x)
#

# %%
absolute_vect = np.vectorize(absolute)

# %%
absolute_vect(tab)

# %%
np.abs, abs # l'une est une ufunc l'autre non...


# %% [markdown]
# ### temps de mise au carré
#
# créez un tableau numpy des 10000 premiers entiers
#
# avec numpy.arange
#
# calculez le temps d'exécution de l'élévation au carré des éléments
#
# %timeit 1+1
#
# avec un for-python
#
# avec une compréhension Python
#
# de manière vectorisée avec **2
#
# de manière vectorisée avec np.power
#
# de manière vectorisée avec np.square
#
# quelles sont les manières de faire les plus rapides ?

# %%
X = np.arange(0,10000,1)

# %%
X

# %%
type(X)

# %% [markdown]
# les bons

# %%
# %timeit X**2

# %%
# %timeit X*X

# %%
# %timeit np.power(X, 2)

# %%
# %timeit np.square(X) # optimisé pour 2

# %% [markdown]
# les pas bons

# %%
[e*e for e in X][0:10]

# %%
# %timeit [e*e for e in X]

# %%
l = [0]*len(X)

# %%
# %%timeit
for i in range(len(l)):
    l[i] = X[i]*X[i]


# %%
def f(T):
    Y=[]
    for e in T:
        Y.append(e**2)
    return Y
# %timeit f(X)
    


# %% [markdown]
# ### juliette gohin

# %%
import numpy as np
from matplotlib import pyplot as plt
image=np.random.randint(0,255,(10,10,3),dtype=np.uint8) # super le uint juste le 256
plt.imshow(image)

# %% [markdown]
# ## 

# %%
from matplotlib import pyplot as plt

X = np.linspace(-np.pi, np.pi, 30) # ok np.pi est bien compris dans l'intervalle
Y = np.sin(X)
plt.plot(X, Y)

# %%
import matplotlib.pyplot as plt
Im = np.random.randint(0,256,size=(10,10))
plt.imshow(Im)
