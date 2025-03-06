{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMUMs5cxA8K5ZLn7jKeHTi5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MarD100/CS-PROYECTO-FINAL/blob/main/calculadoraambiental.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mN-9Q2BPFK7i"
      },
      "outputs": [],
      "source": [
        "def calcular_huella_completa():\n",
        "    print(\"Calculadora de Huella Ambiental Completa 🌱\\n\")\n",
        "\n",
        "    # Entrada de datos\n",
        "    try:\n",
        "        km_transporte = float(input(\"¿Cuántos kilómetros recorres en coche, moto o auto por semana? \"))\n",
        "    except ValueError:\n",
        "        print(\"Entrada inválida. Se asume 0 km.\")\n",
        "        km_transporte = 0.0\n",
        "\n",
        "    tipo_combustible = input(\"¿Qué tipo de combustible usas? (gasolina/diésel/eléctrico/otro): \").lower()\n",
        "\n",
        "    try:\n",
        "        consumo_electricidad = float(input(\"¿Cuántos kWh consumes al mes en casa? \"))\n",
        "    except ValueError:\n",
        "        print(\"Entrada inválida. Se asume 0 kWh.\")\n",
        "        consumo_electricidad = 0.0\n",
        "\n",
        "    energia_renovable = input(\"¿Usas energía renovable en casa? (sí/no): \").lower()\n",
        "    tipo_dieta = input(\"¿Qué tipo de dieta sigues? (vegana/vegetariana/omnívora): \").lower()\n",
        "\n",
        "    try:\n",
        "        kg_residuos = float(input(\"¿Cuántos kilogramos de residuos generas por semana? \"))\n",
        "    except ValueError:\n",
        "        print(\"Entrada inválida. Se asume 0 kg.\")\n",
        "        kg_residuos = 0.0\n",
        "\n",
        "    try:\n",
        "        porcentaje_reciclaje = float(input(\"¿Qué porcentaje de tus residuos reciclas? (0-100): \"))\n",
        "    except ValueError:\n",
        "        print(\"Entrada inválida. Se asume 0% reciclado.\")\n",
        "        porcentaje_reciclaje = 0.0\n",
        "\n",
        "    if porcentaje_reciclaje < 0 or porcentaje_reciclaje > 100:\n",
        "        print(\"Porcentaje fuera de rango, se asume 0% reciclado.\")\n",
        "        porcentaje_reciclaje = 0.0\n",
        "\n",
        "    # Cálculo de huella de transporte\n",
        "    factores_combustible = {\"eléctrico\": 0.05, \"gasolina\": 0.21, \"diésel\": 0.25}\n",
        "    factor_transporte = factores_combustible.get(tipo_combustible, 0.2)\n",
        "    huella_transporte = km_transporte * factor_transporte * 52\n",
        "\n",
        "    # Cálculo de huella de energía\n",
        "    factor_energia = 0.1 if energia_renovable == \"sí\" else 0.5\n",
        "    huella_energia = consumo_electricidad * factor_energia * 12\n",
        "\n",
        "    # Cálculo de huella de alimentación\n",
        "    factores_dieta = {\"vegana\": 1.5, \"vegetariana\": 2.0, \"omnívora\": 3.5}\n",
        "    factor_dieta = factores_dieta.get(tipo_dieta, 3.5)\n",
        "    huella_alimentacion = factor_dieta * 365\n",
        "\n",
        "    # Cálculo de huella de residuos\n",
        "    fraccion_reciclaje = porcentaje_reciclaje / 100\n",
        "    huella_residuos = (kg_residuos * 52) * (1 - fraccion_reciclaje) * 0.9\n",
        "\n",
        "    # Cálculo total de huella anual\n",
        "    huella_total = huella_transporte + huella_energia + huella_alimentacion + huella_residuos\n",
        "\n",
        "    # Evaluación de la huella ambiental\n",
        "    if huella_total < 2000:\n",
        "        evaluacion = \"Tu huella ambiental es adecuada. ¡Buen trabajo! 🌟\"\n",
        "    elif 2000 <= huella_total < 4000:\n",
        "        evaluacion = \"Tu huella ambiental es moderada, pero podrías mejorar algunos hábitos. 🛠\"\n",
        "    else:\n",
        "        evaluacion = \"Tu huella ambiental es alta. Sería recomendable tomar medidas para reducirla. ⚠\"\n",
        "\n",
        "    # Mostrar resultados\n",
        "    print(\"\\nResumen de tu huella ambiental anual:\")\n",
        "    print(f\"Transporte: {huella_transporte:.2f} kg CO2\")\n",
        "    print(f\"Energía en el hogar: {huella_energia:.2f} kg CO2\")\n",
        "    print(f\"Alimentación: {huella_alimentacion:.2f} kg CO2\")\n",
        "    print(f\"Residuos: {huella_residuos:.2f} kg CO2\")\n",
        "    print(f\"\\nTu huella de carbono anual es aproximadamente: {huella_total:.2f} kg de CO2\")\n",
        "    print(evaluacion)\n",
        "    print(\"¡Gracias por contribuir al medio ambiente!\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    calcular_huella_completa()"
      ]
    }
  ]
}