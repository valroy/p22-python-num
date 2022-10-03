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
# # correction devoirs pour le 5 octobre (numpy TP image)

# %% [markdown]
# ## corrections

# %% [markdown]
# ### sauver son image

# %%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# %%
import matplotlib.pyplot as plt
Im = np.random.randint(0, 256, size=(10, 10, 3), dtype=np.uint8)
plt.imshow(Im)
Im.dtype, Im.shape

# %%
plt.imsave('toto.png', Im)

# %%
Ims = plt.imread('toto.png')
plt.imshow(Ims)
plt.show()
print(f'image writeable ? {Ims.flags.writeable}')
print(f'type: {Ims.dtype}\n   min {Ims.min()} - max {Ims.max()}')
print(f'shape: {Ims.shape} (RGBA)')

print(f'first pixel: {Ims[0, 0]}\n   (see the 1. for transparency)')
plt.imshow(Ims[0, 0].reshape(1, 1, 4))
plt.show()

# %% [markdown]
# by default:
# - `float32`
# - `0 <= pixel <= 1`
# - `RGBA` i.e. `(rows, cols, 4)` et non `(rows, cols, 3)` avec transparence à `1`

# %% [markdown]
# vous le voulez entre `0` et `255` en `uint8` en RGB (sans A) ? 

# %% scrolled=true
Ims_uint8 = (Ims[:, :, 0:3]*255).astype(np.uint8)

Ims_uint8.dtype, Ims_uint8.shape

# %% [markdown]
# ### github et le sha-1

# %% [markdown]
# on génère un `sha-1` pour le texte "il fait beau"
#
# par exemple en faisant: `echo "il fait beau" | git hash-object --stdin`
#
# 1. on écrit (`echo`) "il fait beau" sur l'entrée standard `stdin`
#
#
# 1. avec le `|` (*pipe*) on passe le résultat de cette commande à la commande suivante
#
#
# 1. qui demande à la commande `git` d'appliquer la fonction `hash-object` à ce qu'il trouve sur l'entrée standard `stdin`
#

# %%
# ! echo "il fait beau" | git hash-object --stdin

# %% [markdown]
# on refait le calcul du sha-1 sur le **même** texte: on obtient **exactement le même** sha-1  
# (heureusement c'est fait exactement pour cela: trouver un identifiant unique pour un objet)

# %%
# ! echo "il fait beau" | git hash-object --stdin

# %% [markdown]
# on modifie même très légèrement le texte: on obtient un sha-1 **complètement différent**  
# (ouf)

# %%
# ! echo "il fait  beau" | git hash-object --stdin # 2 espaces après fait

# %% [markdown]
# un sha-1 de github est constitué de: 40 caractères hexadécimaux  
# les 16 caractères de `0` à `9`, puis de `a` à `f`

# %%
len('a0b5e3f6a0aeade26cf8033bcf51246a4eac28db')

# %%
