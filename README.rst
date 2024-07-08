.. SPDX-License-Identifier: AGPL-3.0-or-later

----

.. figure:: porthon.png
   :alt: Porthon
   :color: red
   :width: 100%
   :align: center

----

**Porthon** é uma linguagem que foi criada com o propósito de aprendizagem. Ela ajudará muitos pequenos programadores a começar a programar. Ela é uma linguagem de programação brasileira, desenvolvida por um brasileiro, e futuramente será totalmente em português.


Um pedido
---------

Por favor, quem ver este projeto, contribua:

- Adicionando arquivos
- Editando arquivos

**Muito obrigado!**

____________________________________________________________________________________________________________________________________________________________________________________________________________________

Como usar?
==========

Execute o main.py juntamente com o nome do projeto:

``py main.py <arquivo>.ptpy``

Bibliotecas
===========

Ver `Bibliotecas Porthon <https://github.com/Matheus-Schwebel/bibliotecas-porthon/>`_, no GitHub

Exemplos
--------

Com a biblioteca `matematica <https://github.com/Matheus-Schwebel/bibliotecas-porthon/tree/main/matematica>`_:

.. code-block:: python

   de matematica importar *
   de sistema importar *

   a = 90

   b = 80

   b_divisao = 3

   calcsoma = soma(a, b)

   imprimir(calcsoma)

   calcsubtrai = subtrair(a, b)

   imprimir(calcsubtrai)

   calcmultip = multiplicar(a, b)

   imprimir(calcmultip)

   calcdiv = dividir(a, b_divisao)

   imprimir(calcdiv)

   imprimir(pi)

Com a biblioteca `sistema <https://github.com/Matheus-Schwebel/bibliotecas-porthon/tree/main/sistema>`_:

..  code-block:: python

   de sistema importar *

   # Imprimir também é uma função da biblioteca sistema

   imprimir(listar_argumentos())

   imprimir(nome_sistema_operacional())

   lista = listar_arquivos()

   imprimir(lista)

   criar_diretorio("teste")

   remover_arquivo("remover.txt")

Com a biblioteca `mapas <https://github.com/Matheus-Schwebel/bibliotecas-porthon/tree/main/mapas>`_:

.. code-block:: python

   # meu_mapa.ptpy

   importar mapas

   # Criar um mapa centrado em São Paulo
   mapa = mapas.criar_mapa(-23.5505, -46.6333)

   # Adicionar marcador para São Paulo no mapa
   mapas.adicionar_marcador(mapa, -23.5505, -46.6333, 'São Paulo')

   mapas.salvar(mapa, arquivo_html="mapa.html")
