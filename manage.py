#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#TODO: Projeto PROOF
# O objetivo deste challenge é desenvolver uma aplicação que nos permita obter uma lista de
# IPs de redes Tor (https://www.torproject.org/) a partir de fontes externas, distintas e
# apresentá-los de maneira unificada. Adicionalmente esta aplicação deve possibilitar a
# indicação de IPs de redes que NÃO queremos que apareçam na lista.
# O objetivo é desenvolver uma API REST que tenha os métodos detalhados a seguir:
# 1) Um endpoint GET que devolve todos os IPs de TOR obtidos das fontes externas
# detalhadas abaixo:
# ● https://www.dan.me.uk/tornodes
# ● https://torstatus.blutmagie.de
# 2) Um endpoint POST que receba um IP e o agregue à uma base de dados onde se
# encontram todos os IPs que não queremos que apareçam no output do endpoint 3
# (detalhado abaixo).
# 3) Um endpoint GET que devolve os IPs obtidos das fontes externas EXCETO os que
# se encontram na base de dados (IPs carregados utilizando o endpoint 2)
# A base de dados a ser utilizada fica à sua escolha.
# A aplicação desenvolvida deve executar em um container de Docker.

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proof.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
