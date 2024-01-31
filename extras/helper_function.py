{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN9z1ZLlS8bwYusqiIg6D2z",
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
        "<a href=\"https://colab.research.google.com/github/Abhilash-Bee/Abhilash-Bee/blob/main/extras/helper_function.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "id": "OmBkd8I6kvpV"
      },
      "outputs": [],
      "source": [
        "# Common Dependencies\n",
        "import tensorflow as tf\n",
        "import matplotlib.pyplot as plt\n",
        "import matplotlib.image as mpimg\n",
        "\n",
        "\n",
        "\n",
        "# Dowload and unzip the file from `url`\n",
        "def unzip_file(url: str) -> str:\n",
        "  \"\"\"\n",
        "  Downloads and unzips the file.\n",
        "\n",
        "  Args:\n",
        "  url - url of the file to be downloaded and unzip\n",
        "\n",
        "  Returns:\n",
        "  Path of dataset directory\n",
        "  \"\"\"\n",
        "\n",
        "  path = tf.keras.utils.get_file(origin=url, extract=True)\n",
        "  print(f'{path[-4]} has been successfully extracted.')\n",
        "  return path[:-4]\n",
        "\n",
        "\n",
        "\n",
        "# Plot loss and accuracy curve\n",
        "def plot_loss_accuracy_curve(history, figsize=(7, 10), savefig=False) -> None:\n",
        "  \"\"\"\n",
        "  Plots the loss and accuracy curve on training and validation history.\n",
        "\n",
        "  Args:\n",
        "  history - history of the model\n",
        "  figsize - defaults to `(8, 17)`\n",
        "  savefig - defaults to `False`, if `True`, saves the image as `.png`\n",
        "  \"\"\"\n",
        "\n",
        "  fig, ax = plt.subplots(2, 1, figsize=figsize, sharex=True)\n",
        "\n",
        "  loss = [history.history['loss'], history.history['val_loss']]\n",
        "  accuracy = [history.history['accuracy'], history.history['val_accuracy']]\n",
        "  loss_accuracy = [loss, accuracy]\n",
        "  labels = ['Loss', 'Accuracy']\n",
        "  epoch = tf.range(1, len(history.history['loss']) + 1)\n",
        "\n",
        "  for i in range(2):\n",
        "    ax[i].set_title(labels[i] + ' Vs Epoch Curve')\n",
        "    ax[i].plot(epoch, loss_accuracy[i][0], label = 'Training ' + labels[i])\n",
        "    ax[i].plot(epoch, loss_accuracy[i][1], label = 'Validation ' + labels[i])\n",
        "    ax[i].set_ylabel(labels[i])\n",
        "    if i == 0:\n",
        "      ax[i].legend(loc='upper right')\n",
        "    else:\n",
        "      ax[i].legend(loc='upper left')\n",
        "\n",
        "  ax[1].set_xlabel('Epoch')\n",
        "\n",
        "\n",
        "\n",
        "# Importing Dependencies\n",
        "from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay\n",
        "\n",
        "# Plot confusion matrix\n",
        "def plot_confusion_matrix(y_true, y_pred, figsize=(10, 10), class_names=None) -> None:\n",
        "  \"\"\"\n",
        "  Plots confusion matrix on the true and predicted label.\n",
        "\n",
        "  Args:\n",
        "  y_true - Acutal (True) Label\n",
        "  y_pred - Predicted Label\n",
        "  figsize - Defaults to `(10, 10)`\n",
        "  class_names - Defaults to `None`, provide class_names to change x and y labels\n",
        "  \"\"\"\n",
        "\n",
        "  cm = confusion_matrix(y_true=y_true, y_pred=y_pred)\n",
        "  fig, ax = plt.subplots(figsize=figsize)\n",
        "  disp = ConfusionMatrixDisplay(cm, display_labels=class_names)\n",
        "  disp.plot(ax=ax, xticks_rotation='vertical', cmap=plt.cm.Blues)\n",
        "\n",
        "\n",
        "\n",
        "# Importing Dependencies\n",
        "import os\n",
        "\n",
        "# Walk through the directory\n",
        "def walk_through_directory(filepath: str) -> None:\n",
        "  \"\"\"\n",
        "  Provides number of folders and number of filenames along with filepath by\n",
        "  running recursively into the subdirectories of filepath.\n",
        "\n",
        "  Args:\n",
        "  filepath - path of the directory\n",
        "  \"\"\"\n",
        "\n",
        "  for dirpath, dirnames, filenames in os.walk(filepath):\n",
        "    print(f\"There are {len(dirnames)} folders and {len(filenames)} in this '{dirpath}' directory path.\")\n",
        "\n",
        "\n",
        "\n",
        "# Importing Dependencies\n",
        "import datetime\n",
        "\n",
        "# Create the tensorboard callback\n",
        "def tensorboard_callbacks(directory: str, experiment_name: str) -> object:\n",
        "  \"\"\"\n",
        "  Creates a tensorboard callback and provides message if the tensorboard callback\n",
        "  is successfully saved in the path.\n",
        "\n",
        "  Args:\n",
        "  directory - folder name of the tensorboard callback\n",
        "  experiment_name - sub-folder inside the directory of the current experiment\n",
        "\n",
        "  Returns:\n",
        "  Tensorboard object\n",
        "  \"\"\"\n",
        "\n",
        "  log_dir = directory + '/' + experiment_name + '/' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S')\n",
        "  callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)\n",
        "  print(f'Saving the tensorboard callbacks in {log_dir}')\n",
        "  return callback\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "vPaL-SQKnwip"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "6c_PY_bbmW7E"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cIURl4VWpIbJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "XCGU-Bvmnhy9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "GwD7aHKinAZF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "QkW6Zy_Rmnxx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2GLcUNuEpkdN",
        "outputId": "d14eb2dd-91fb-4ab0-e7ed-c6e1f0e33dc1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "QUQx_wWipnUW"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}